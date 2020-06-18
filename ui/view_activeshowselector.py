from PySide2 import QtWidgets

class ActiveShowSelector(QtWidgets.QGroupBox):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.setupWidgets()
		self.policy_size = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
		self.setSizePolicy(self.policy_size)
	
	def setupWidgets(self):
		self.lay_main = QtWidgets.QVBoxLayout()
		self.setLayout(self.lay_main)
		
		self.cmb_activeshow = QtWidgets.QComboBox()
		self.lay_main.addWidget(self.cmb_activeshow)
	
	def setShowList(self, showlist):
		for show in showlist:
			self.cmb_activeshow.addItem(show.get("title"), show.get("guid_show"))
	
	def getActiveShow(self):
		return {"guid_show": self.cmb_activeshow.currentData(), "title": self.cmb_activeshow.currentText()}