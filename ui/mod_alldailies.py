from PySide2 import QtWidgets

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
