from PySide2 import QtWidgets, QtGui

class AllDailiesView(QtWidgets.QWidget):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.lay_main = QtWidgets.QVBoxLayout()
		self.setLayout(self.lay_main)
		self.setupWidgets()
	
	def setupWidgets(self):
		self.lbl_summary = QtWidgets.QLabel("No show selected")
		self.lay_main.addWidget(self.lbl_summary)
		self.tree_alldailies = QtWidgets.QTreeView()
		self.lay_main.addWidget(self.tree_alldailies)
	
	def setShots(self, shotlist=None):
		
		shotlist = shotlist or []
		
		self.columns = ("Shot","Start","End")
		
		self.model_dailies = QtGui.QStandardItemModel()
		#self.model_dailies.setColumnCount(len(self.columns))
		self.model_dailies.setHorizontalHeaderLabels(self.columns)

		item_root = self.model_dailies.invisibleRootItem()
		for shot in shotlist:
			item_root.appendRow([
				QtGui.QStandardItem(shot.shot),
				QtGui.QStandardItem(str(shot.tc_start)),
				QtGui.QStandardItem(str(shot.tc_end))
			])
		
		self.tree_alldailies.setModel(self.model_dailies)