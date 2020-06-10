#!/usr/bin/env python3

from PySide2 import QtUiTools, QtWidgets, QtCore
from ui.wnd_main import Ui_MainWindow
from upco_tools import upco_timecode
import sys, pathlib, requests, urllib, configparser

class MainWindow(QtWidgets.QMainWindow):

	def __init__(self):
		super(MainWindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

class Deepworm(QtWidgets.QApplication):

	def __init__(self, argv):
		super(Deepworm, self).__init__(argv)

		# Load config from file
		self.config = configparser.ConfigParser()
		self.loadConfig()
		self.api_base_url = f"http://{self.config['connection'].get('server_ip', '127.0.1.1')}:{self.config['connection'].get('server_port')}/dailies/v1/"

		# Load initial state
		self.setStyle(self.config["interface"].get("theme"))
		self.shows = []
		self.active_show = None

		# Set up main window
		self.wnd_main = MainWindow()
		self.wnd_main.show()
		self.wnd_main.ui.col_left.setCurrentIndex(self.wnd_main.ui.col_left.indexOf(self.wnd_main.ui.tab_alldailies))
		
		# Treeview
		self.wnd_main.ui.tree_alldailies.setAlternatingRowColors(True)

		# Set active show for program
		while True:
			try:
				self.populateShowInfo()
				break
			except ConnectionError as e:
				wnd_err = QtWidgets.QMessageBox.critical(self.wnd_main,
					"Connection Error",
					f"Unable to connect to server {self.config['connection'].get('server_ip', '127.0.1.1')}:{self.config['connection'].get('server_port')}:\n\n{e}",
					QtWidgets.QMessageBox.Retry|QtWidgets.QMessageBox.Abort,
					QtWidgets.QMessageBox.Abort)
				if wnd_err == QtWidgets.QMessageBox.Abort:
					break



		# Set event listener after initial setup handles this explicitly
		self.wnd_main.ui.cmb_activeshow.currentIndexChanged.connect(lambda x: self.changeShow(self.wnd_main.ui.cmb_activeshow.itemData(x)))
	
	def __del__(self):
		try:
			self.config["interface"].update({"lastshow":self.active_show_name})
			self.writeConfig()
		except Exception as e:
			sys.stderr.write(f"Error writing to config file: {e}")
	
	@property
	def active_show_guid(self):
		return self.active_show.get("guid_show")
	@property
	def active_show_name(self):
		return self.active_show.get("title")

	def populateShowInfo(self):
		self.shows = self.getShowList()

		# Active Show dropdown
		{self.wnd_main.ui.cmb_activeshow.addItem(x.get("title"), x.get("guid_show")) for x in self.shows}

		# Set active show for program
		if self.config["interface"].get("lastshow"):
			show_index = self.wnd_main.ui.cmb_activeshow.findText(self.config["interface"].get("lastshow"), QtCore.Qt.MatchFixedString)
			if show_index >= 0:
				self.wnd_main.ui.cmb_activeshow.setCurrentIndex(show_index)
		self.changeShow(self.wnd_main.ui.cmb_activeshow.itemData(self.wnd_main.ui.cmb_activeshow.currentIndex()))
		
	
	def getShowList(self):
		r = requests.get(f"{self.api_base_url}/shows")
		
		if r.status_code != 200:
			raise ConnectionError(f"({r.status_code}) Error connecting to API")

		return list(r.json())

	def loadConfig(self, path_config=pathlib.Path.home()/".config"/"deepworm.ini"):
		if not path_config.exists():
			self.config["connection"] = {
				"username": "",
				"password": "",
				"server_ip": "127.0.0.1",
				"server_port": "5000"
			}
			self.config["interface"] = {
				"theme": "fusion"
			}

			self.writeConfig(path_config)
		
		else:
			try:
				self.config.read(path_config)
			except Exception as e:
				sys.stderr.write(f"Unable to read config file from {path_config}: {e}")

	def writeConfig(self, path_config=pathlib.Path.home()/".config"/"deepworm.ini"):
		try:
			path_config.parent.mkdir(parents=True, exist_ok=True)
			with path_config.open('w') as file_config:
				self.config.write(file_config)
		except Exception as e:
			sys.stderr.write(f"Unable to write config file to {path_config}: {e}")
	
	def changeShow(self, guid_show):
		for x in self.shows:
			if x.get("guid_show") == guid_show:
				self.active_show = x

		if guid_show != self.active_show_guid:
			raise ValueError(f"Show not found for guid {guid_show}")

		r = requests.get(f"{self.api_base_url}/shots/{self.active_show_guid}")

		if r.status_code != 200:
			raise FileNotFoundError(f"({r.status_code}) Invalid show guid: {self.active_show_guid}")

		self.wnd_main.setWindowTitle(f"Deepworm - {self.active_show_name}")
		
		print(f"Changed show to {self.active_show_name} ({len(r.json())} shots)")
		self.loadAllDailies(r.json())
		#print(f"Changing show to {guid_show}")
	
	def loadAllDailies(self, dailies):
		self.wnd_main.ui.tree_alldailies.setSortingEnabled(False)

		i = self.wnd_main.ui.tree_alldailies.topLevelItemCount()
		while i > -1:
			self.wnd_main.ui.tree_alldailies.takeTopLevelItem(i)
			i -= 1

		for shot in dailies:
			self.wnd_main.ui.tree_alldailies.addTopLevelItem(QtWidgets.QTreeWidgetItem([
				shot.get("shot"),
				str(upco_timecode.Timecode(shot.get("frm_start"))),
				str(upco_timecode.Timecode(shot.get("frm_end")))
			]))
		self.wnd_main.ui.tree_alldailies.resizeColumnToContents(0)
		self.wnd_main.ui.lbl_dailiescount.setText(f"Showing {self.wnd_main.ui.tree_alldailies.topLevelItemCount()} shots")
		self.wnd_main.ui.tree_alldailies.setSortingEnabled(True)


def main(argv):

	app = Deepworm(argv)

	sys.exit(app.exec_())


if __name__=="__main__":

	main(sys.argv)

