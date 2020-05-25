#!/usr/bin/env python3

from PySide2 import QtUiTools, QtWidgets
from ui.wnd_main import Ui_MainWindow
from upco_tools import upco_timecode
import sys, pathlib, requests, urllib

API_BASE_URL = "http://127.0.0.1:5000/dailies/v1/"

class MainWindow(QtWidgets.QMainWindow):

	def __init__(self):
		super(MainWindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

class Deepworm(QtWidgets.QApplication):

	def __init__(self, argv):
		super(Deepworm, self).__init__(argv)

		# Load initial state
		self.shows = self.getShowList()
		self.active_show = None

		# Set up main window
		self.wnd_main = MainWindow()
		self.wnd_main.show()
		self.wnd_main.ui.col_left.setCurrentIndex(self.wnd_main.ui.col_left.indexOf(self.wnd_main.ui.tab_alldailies))
	
		# Active Show dropdown
		{self.wnd_main.ui.cmb_activeshow.addItem(x.get("title"), x.get("guid_show")) for x in self.shows}
		self.wnd_main.ui.cmb_activeshow.currentIndexChanged.connect(lambda x: self.changeShow(self.wnd_main.ui.cmb_activeshow.itemData(x)))

		self.wnd_main.ui.tree_alldailies.setAlternatingRowColors(True)

		# Set active show for program
		self.changeShow(self.wnd_main.ui.cmb_activeshow.itemData(self.wnd_main.ui.cmb_activeshow.currentIndex()))
	
	@property
	def active_show_guid(self):
		return self.active_show.get("guid_show")
	@property
	def active_show_name(self):
		return self.active_show.get("title")
	
	def getShowList(self):
		r = requests.get(f"{API_BASE_URL}/shows")
		
		if r.status_code != 200:
			raise FileNotFoundError(f"({r.status_code}) Error connecting to API")

		return list(r.json())

	def changeShow(self, guid_show):
		
		for x in self.shows:
			if x.get("guid_show") == guid_show:
				self.active_show = x

		if guid_show != self.active_show_guid:
			raise ValueError(f"Show not found for guid {guid_show}")

		r = requests.get(f"{API_BASE_URL}/shots/{self.active_show_guid}")

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

