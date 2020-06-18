from PySide2 import QtWidgets

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