from PySide2 import QtWidgets, QtCore
from .mod_alldailies import AllDailiesView

class WindowMain(QtWidgets.QMainWindow):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		# Setup initial widget and layout
		root = QtWidgets.QWidget()
		self.setCentralWidget(root)
		self.lay_main = QtWidgets.QVBoxLayout()
		root.setLayout(self.lay_main)

		# Status Bar
		self.status_bar = QtWidgets.QStatusBar()
		self.setStatusBar(self.status_bar)

		# Menu
		self.menu_bar = QtWidgets.QMenuBar()
		self.menu_file = QtWidgets.QMenu("&File")
		self.menu_help = QtWidgets.QMenu("&Help")
		self.menu_bar.addAction(self.menu_file.menuAction())
		self.menu_bar.addAction(self.menu_help.menuAction())
		self.setMenuBar(self.menu_bar)


		self.setupWidgets()
	
	def setupWidgets(self):
		
		self.resize(1024,640)

		# Active Show selector
		self.ui_activeshowselector = ActiveShowSelector("Active Show")
		self.lay_main.addWidget(self.ui_activeshowselector)

		# Splitter
		self.split_main = QtWidgets.QSplitter()
		self.split_main.setOrientation(QtCore.Qt.Horizontal)
		self.lay_main.addWidget(self.split_main)

		# Tabs
		self.tabs_main = QtWidgets.QTabWidget()
		self.policy_tabs = QtWidgets.QSizePolicy()
		self.policy_tabs.setHorizontalStretch(1)
		self.tabs_main.setSizePolicy(self.policy_tabs)
		self.split_main.addWidget(self.tabs_main)

		self.tab_alldailies = AllDailiesView()
		self.tab_alldailies.setAutoFillBackground(True)
		#self.tab_listtool = QtWidgets.QWidget()
		#self.tab_monitors = QtWidgets.QWidget()

		self.tabs_main.addTab(self.tab_alldailies, "All Dailies")
		#self.tabs_main.addTab(self.tab_listtool, "List Tool")
		#self.tabs_main.addTab(self.tab_monitors, "Monitors")

		# Extended info sidebar
		self.ui_extendedinfo = ExtendedInfoPane()
		self.split_main.addWidget(self.ui_extendedinfo)



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

class ExtendedInfoPane(QtWidgets.QWidget):
		
		def __init__(self, *args, **kwargs):
			super().__init__(*args, **kwargs)
			self.policy_size = QtWidgets.QSizePolicy()
			self.policy_size.setHorizontalPolicy(QtWidgets.QSizePolicy.Fixed)
			self.policy_size.setVerticalPolicy(QtWidgets.QSizePolicy.Expanding)
			self.policy_size.setHorizontalStretch(0)
			self.setSizePolicy(self.policy_size)
			self.setupWidgets()

		def setupWidgets(self):
			self.lay_main = QtWidgets.QVBoxLayout()
			self.lay_main.setContentsMargins(0,0,0,0)
			self.setLayout(self.lay_main)

			# Extended Info box
			self.grp_extendedinfo = QtWidgets.QGroupBox("Extended Info")
			self.lay_extendedinfo = QtWidgets.QVBoxLayout()
			self.grp_extendedinfo.setLayout(self.lay_extendedinfo)
			self.tree_extendedinfo = QtWidgets.QTreeView()
			self.lay_extendedinfo.addWidget(self.tree_extendedinfo)
			self.lay_main.addWidget(self.grp_extendedinfo)

			# Export Metadata box
			self.grp_exportmetadata = QtWidgets.QGroupBox("Export Metadata")
			self.lay_exportmetadata = QtWidgets.QHBoxLayout()
			self.grp_exportmetadata.setLayout(self.lay_exportmetadata)
			self.btn_exportale = QtWidgets.QPushButton("Export ALE")
			self.btn_exportcsv = QtWidgets.QPushButton("Export CSV")
			self.lay_exportmetadata.addWidget(self.btn_exportale)
			self.lay_exportmetadata.addWidget(self.btn_exportcsv)
			self.lay_main.addWidget(self.grp_exportmetadata)

			# Restore Media box
			self.grp_restoremedia = QtWidgets.QGroupBox("Restore Media")
			self.lay_restoremedia = QtWidgets.QHBoxLayout()
			self.grp_restoremedia.setLayout(self.lay_restoremedia)
			self.btn_restorediva = QtWidgets.QPushButton("Restore from Diva")
			self.btn_restorelto  = QtWidgets.QPushButton("Pull from LTO")
			self.lay_restoremedia.addWidget(self.btn_restorediva)
			self.lay_restoremedia.addWidget(self.btn_restorelto)
			self.lay_main.addWidget(self.grp_restoremedia)