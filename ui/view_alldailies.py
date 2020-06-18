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
	
	def setShotList(self, shotlist=None):
		
		shotlist = shotlist or []

		headers = []
		{headers.extend(shot.metadata.keys()) for shot in shotlist}
		
		self.columns = ["Shot","Start","End","Scene","Take","Camroll","Soundroll"]
		{self.columns.append(x) for x in sorted(headers) if x not in self.columns}
		
		self.model_dailies = QtGui.QStandardItemModel()
		#self.model_dailies.setColumnCount(len(self.columns))
		self.model_dailies.setHorizontalHeaderLabels(self.columns)

		item_root = self.model_dailies.invisibleRootItem()
		for shot in shotlist:
			row = [shot.shot, str(shot.tc_start), str(shot.tc_end)]
			row.extend(str(shot.metadata.get(x,"")) for x in self.columns[3:])
			item_root.appendRow([QtGui.QStandardItem(x) for x in row])
		
		self.tree_alldailies.setModel(self.model_dailies)