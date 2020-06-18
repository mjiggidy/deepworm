from PySide2 import QtCore, QtWidgets
from ui import wnd_main
from upco_tools import upco_shot
import requests, sys, json


class Deepworm(QtWidgets.QApplication):

	def __init__(self):
		super().__init__()

		self.wnd_main = wnd_main.WindowMain()
		
		self.show_selector   = self.wnd_main.ui_activeshowselector
		self.view_alldailies = self.wnd_main.view_alldailies

		self.setupWidgets()
		
		self.wnd_main.show()
	
	def setupWidgets(self):

		self.show_selector.setShowList(self.getShowList())
		self.show_selector.cmb_activeshow.currentIndexChanged.connect(self.setCurrentShow)
		self.setCurrentShow()

	def getShowList(self):
		""" Get a list of shows and GUIDs """
		r = requests.get(f"http://127.0.0.1:5000/dailies/v1/shows")
		
		if r.status_code != 200:
			raise ConnectionError(f"({r.status_code}) Error connecting to API")

		return list(r.json())
	
	def getShotList(self, guid_show):
		r = requests.get(f"http://127.0.0.1:5000/dailies/v1/shots/{guid_show}")

		if r.status_code != 200:
			raise FileNotFoundError(f"({r.status_code}) Invalid show guid: {self.active_show_guid}")

		return (upco_shot.Shot(shot.get("shot"), shot.get("frm_start"), tc_end=shot.get("frm_end"), metadata=json.loads(shot.get("metadata"))) for shot in r.json())
	
	def setCurrentShow(self):
		self.show_selector.cmb_activeshow.setDisabled(True)

		showinfo = self.show_selector.getActiveShow()
		self.wnd_main.setWindowTitle(f"Deepworm - {showinfo.get('title')}")
		self.view_alldailies.setShotList(list(self.getShotList(showinfo.get("guid_show"))))

		self.show_selector.cmb_activeshow.setDisabled(False)

def main():

	app = Deepworm()
	sys.exit(app.exec_())

if __name__ == "__main__":

	main()