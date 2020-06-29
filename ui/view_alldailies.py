from PySide2 import QtWidgets, QtGui

class AllDailiesView(QtWidgets.QWidget):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.lay_main = QtWidgets.QVBoxLayout()
		self.setLayout(self.lay_main)
		self.setupWidgets()
	
	def setupWidgets(self):
		self.lay_top = QtWidgets.QHBoxLayout()
		self.lay_main.addLayout(self.lay_top)
		self.lbl_summary = QtWidgets.QLabel("No show selected")
		self.lbl_summary.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed))
		self.lay_top.addWidget(self.lbl_summary)
		self.btn_choosecolumns = QtWidgets.QPushButton("Choose Columns")
		self.btn_choosecolumns.clicked.connect(self.chooseColumns)
		self.lay_top.addWidget(self.btn_choosecolumns)
		
		self.tree_alldailies = QtWidgets.QTreeView()
		self.lay_main.addWidget(self.tree_alldailies)
	
	def setShotList(self, shotlist=None):

		self.tree_alldailies.setSortingEnabled(False)
		
		shotlist = shotlist or []

		headers = []
		{headers.extend(shot.metadata.keys()) for shot in shotlist}
		
		self.columns = ["Shot","Start","End","Scene","Take","Camroll","Soundroll"]
		{self.columns.append(x) for x in sorted(headers) if x not in self.columns}
		
		self.model_dailies = QtGui.QStandardItemModel()
		self.model_dailies.setHorizontalHeaderLabels(self.columns)

		item_root = self.model_dailies.invisibleRootItem()
		for shot in shotlist:
			row = [shot.shot, str(shot.tc_start), str(shot.tc_end)]
			row.extend(str(shot.metadata.get(x,"")) for x in self.columns[3:])
			item_root.appendRow([QtGui.QStandardItem(x) for x in row])
		
		self.tree_alldailies.setModel(self.model_dailies)
		self.lbl_summary.setText(f"Showing all {self.model_dailies.rowCount():,} shots")

		self.tree_alldailies.resizeColumnToContents(0)
		self.tree_alldailies.setSortingEnabled(True)
	
	def chooseColumns(self):
		self.wnd_choosecolumns = ColumnChooser(self, [(not self.tree_alldailies.isColumnHidden(x), self.columns[x]) for x in range(len(self.columns))])
		if self.wnd_choosecolumns.exec_():
			self.setVisibleColumns([x.row() for x in self.wnd_choosecolumns.list_columns.selectedIndexes()])
	
	def setVisibleColumns(self, columns):
		for col in range(len(self.columns)):
			self.tree_alldailies.setColumnHidden(col, col not in columns)

class ColumnChooser(QtWidgets.QDialog):

	def __init__(self, parent, columns):
		super().__init__(parent)
		self.setModal(True)
		self.visibleColumns = []

		self.lay_main = QtWidgets.QVBoxLayout()
		self.setLayout(self.lay_main)

		self.list_columns = QtWidgets.QListWidget()
		self.list_columns.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.MultiSelection)
		{self.list_columns.addItem(x[1]) for x in columns}
		{self.list_columns.item(x).setSelected(columns[x][0]) for x in range(len(columns))}
		self.lay_main.addWidget(self.list_columns)

		self.box_save = QtWidgets.QDialogButtonBox()
		self.btn_ok = QtWidgets.QPushButton("Apply")
		self.btn_ok.setDefault(True)
		self.btn_ok.clicked.connect(self.accept)
		self.btn_cancel = QtWidgets.QPushButton("Cancel")
		self.btn_cancel.clicked.connect(self.reject)
		self.box_save.addButton(self.btn_ok, QtWidgets.QDialogButtonBox.ButtonRole.ApplyRole)
		self.box_save.addButton(self.btn_cancel, QtWidgets.QDialogButtonBox.ButtonRole.RejectRole)
		self.lay_main.addWidget(self.box_save)