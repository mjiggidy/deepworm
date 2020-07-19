from PySide2 import QtCore, QtWidgets
from ui import wnd_main
from upco_tools import upco_shot, upco_deepworm
import requests, sys, json, time, configparser, pathlib


class Deepworm(QtWidgets.QApplication):

	def __init__(self):
		super().__init__()

		self.config = configparser.ConfigParser()
		self.loadConfig()
		self.dw_client = upco_deepworm.DeepwormClient(host=self.config["connection"].get("server_ip"), port=self.config["connection"].get("server_port"))

		self.setStyle(self.config["interface"]["theme"])
		self.wnd_main = wnd_main.WindowMain()
		
		self.show_selector   = self.wnd_main.ui_activeshowselector
		self.view_alldailies = self.wnd_main.view_alldailies

		self.setupWidgets()
		
		self.wnd_main.show()
	
	def setupWidgets(self):

		self.show_selector.setShowList(self.getShowList())
		# Load last show from memory if applicable
		
		if self.config["interface"].get("lastshow"):
			show_index = self.show_selector.cmb_activeshow.findText(self.config["interface"].get("lastshow"), QtCore.Qt.MatchFixedString)
			if show_index >= 0: self.show_selector.cmb_activeshow.setCurrentIndex(show_index)
		
		self.show_selector.cmb_activeshow.currentIndexChanged.connect(self.setCurrentShow)
		self.setCurrentShow()

	def getShowList(self):
		""" Get a list of shows and GUIDs """
		return self.dw_client.getShowList()
	
	def getShotList(self, guid_show):
		return self.dw_client.getShotList(guid_show)
	
	def setCurrentShow(self):
		self.show_selector.cmb_activeshow.setDisabled(True)
		
		showinfo = self.show_selector.getActiveShow()
		self.wnd_main.statusBar().showMessage(f"Loading {showinfo.get('title')}...")
		
		time_start = time.time()

		self.view_alldailies.setShotList(list(self.getShotList(showinfo.get("guid_show"))))
		
		time_end = time.time() - time_start
		self.wnd_main.statusBar().showMessage(f"Loaded {showinfo.get('title')} in {time_end:.2f} seconds")
		self.wnd_main.setWindowTitle(f"Deepworm - {showinfo.get('title')}")
		self.config["interface"]["lastshow"] = showinfo.get("title")

		self.show_selector.cmb_activeshow.setDisabled(False)
	
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
	
	def __del__(self):
		try:
#			self.config["interface"].update({"lastshow":self.active_show_name})
			self.writeConfig()
		except Exception as e:
			sys.stderr.write(f"Error writing to config file: {e}")

def main():

	app = Deepworm()
	sys.exit(app.exec_())

if __name__ == "__main__":

	main()