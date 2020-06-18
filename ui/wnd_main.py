from PySide2 import QtWidgets, QtCore
from .view_alldailies import AllDailiesView
from .view_activeshowselector import ActiveShowSelector
from .view_extendedinfo import ExtendedInfoPane

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

		self.view_alldailies = AllDailiesView()
		self.view_alldailies.setAutoFillBackground(True)
		
		self.view_listtool = QtWidgets.QWidget()
		self.view_listtool.setAutoFillBackground(True)

		self.view_monitors = QtWidgets.QWidget()
		self.view_monitors.setAutoFillBackground(True)

		self.tabs_main.addTab(self.view_alldailies, "All Dailies")
		self.tabs_main.addTab(self.view_listtool,   "List Tool")
		self.tabs_main.addTab(self.view_monitors,   "Monitors")

		# Extended info sidebar
		self.ui_extendedinfo = ExtendedInfoPane()
		self.split_main.addWidget(self.ui_extendedinfo)