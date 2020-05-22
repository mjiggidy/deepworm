# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wnd_main_commonext.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 750)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.lay_main = QWidget(MainWindow)
        self.lay_main.setObjectName(u"lay_main")
        self.verticalLayout_2 = QVBoxLayout(self.lay_main)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.grp_activeshow = QGroupBox(self.lay_main)
        self.grp_activeshow.setObjectName(u"grp_activeshow")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.grp_activeshow.sizePolicy().hasHeightForWidth())
        self.grp_activeshow.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.grp_activeshow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.cmb_activeshow = QComboBox(self.grp_activeshow)
        self.cmb_activeshow.setObjectName(u"cmb_activeshow")

        self.verticalLayout.addWidget(self.cmb_activeshow)


        self.verticalLayout_2.addWidget(self.grp_activeshow)

        self.split_main = QSplitter(self.lay_main)
        self.split_main.setObjectName(u"split_main")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.split_main.sizePolicy().hasHeightForWidth())
        self.split_main.setSizePolicy(sizePolicy1)
        self.split_main.setFrameShape(QFrame.NoFrame)
        self.split_main.setFrameShadow(QFrame.Plain)
        self.split_main.setLineWidth(1)
        self.split_main.setMidLineWidth(0)
        self.split_main.setOrientation(Qt.Horizontal)
        self.split_main.setHandleWidth(5)
        self.col_left = QTabWidget(self.split_main)
        self.col_left.setObjectName(u"col_left")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.col_left.sizePolicy().hasHeightForWidth())
        self.col_left.setSizePolicy(sizePolicy2)
        self.col_left.setAutoFillBackground(True)
        self.tab_alldailies = QWidget()
        self.tab_alldailies.setObjectName(u"tab_alldailies")
        self.tab_alldailies.setAutoFillBackground(True)
        self.verticalLayout_3 = QVBoxLayout(self.tab_alldailies)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lbl_dailiescount = QLabel(self.tab_alldailies)
        self.lbl_dailiescount.setObjectName(u"lbl_dailiescount")

        self.verticalLayout_3.addWidget(self.lbl_dailiescount)

        self.tree_alldailies = QTreeWidget(self.tab_alldailies)
        self.tree_alldailies.setObjectName(u"tree_alldailies")

        self.verticalLayout_3.addWidget(self.tree_alldailies)

        self.col_left.addTab(self.tab_alldailies, "")
        self.tab_listtool = QWidget()
        self.tab_listtool.setObjectName(u"tab_listtool")
        self.col_left.addTab(self.tab_listtool, "")
        self.tab_monitors = QWidget()
        self.tab_monitors.setObjectName(u"tab_monitors")
        self.col_left.addTab(self.tab_monitors, "")
        self.split_main.addWidget(self.col_left)
        self.verticalLayoutWidget = QWidget(self.split_main)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.col_right = QVBoxLayout(self.verticalLayoutWidget)
        self.col_right.setObjectName(u"col_right")
        self.col_right.setContentsMargins(0, 0, 0, 0)
        self.grp_extinfo = QGroupBox(self.verticalLayoutWidget)
        self.grp_extinfo.setObjectName(u"grp_extinfo")
        sizePolicy1.setHeightForWidth(self.grp_extinfo.sizePolicy().hasHeightForWidth())
        self.grp_extinfo.setSizePolicy(sizePolicy1)
        self.verticalLayout_6 = QVBoxLayout(self.grp_extinfo)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.tree_extinfo = QTreeWidget(self.grp_extinfo)
        self.tree_extinfo.setObjectName(u"tree_extinfo")

        self.verticalLayout_6.addWidget(self.tree_extinfo)


        self.col_right.addWidget(self.grp_extinfo)

        self.grp_export = QGroupBox(self.verticalLayoutWidget)
        self.grp_export.setObjectName(u"grp_export")
        self.horizontalLayout = QHBoxLayout(self.grp_export)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_exportmeta = QPushButton(self.grp_export)
        self.btn_exportmeta.setObjectName(u"btn_exportmeta")

        self.horizontalLayout.addWidget(self.btn_exportmeta)

        self.btn_exportproject = QPushButton(self.grp_export)
        self.btn_exportproject.setObjectName(u"btn_exportproject")

        self.horizontalLayout.addWidget(self.btn_exportproject)


        self.col_right.addWidget(self.grp_export)

        self.grp_restore = QGroupBox(self.verticalLayoutWidget)
        self.grp_restore.setObjectName(u"grp_restore")
        self.horizontalLayout_2 = QHBoxLayout(self.grp_restore)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_restorediva = QPushButton(self.grp_restore)
        self.btn_restorediva.setObjectName(u"btn_restorediva")

        self.horizontalLayout_2.addWidget(self.btn_restorediva)

        self.btn_restorelto = QPushButton(self.grp_restore)
        self.btn_restorelto.setObjectName(u"btn_restorelto")

        self.horizontalLayout_2.addWidget(self.btn_restorelto)


        self.col_right.addWidget(self.grp_restore)

        self.split_main.addWidget(self.verticalLayoutWidget)

        self.verticalLayout_2.addWidget(self.split_main)

        MainWindow.setCentralWidget(self.lay_main)
        self.mnu_main = QMenuBar(MainWindow)
        self.mnu_main.setObjectName(u"mnu_main")
        self.mnu_main.setGeometry(QRect(0, 0, 1024, 21))
        self.mnu_file = QMenu(self.mnu_main)
        self.mnu_file.setObjectName(u"mnu_file")
        self.menu_help = QMenu(self.mnu_main)
        self.menu_help.setObjectName(u"menu_help")
        MainWindow.setMenuBar(self.mnu_main)
        self.status_main = QStatusBar(MainWindow)
        self.status_main.setObjectName(u"status_main")
        self.status_main.setAcceptDrops(False)
        self.status_main.setSizeGripEnabled(True)
        MainWindow.setStatusBar(self.status_main)
        QWidget.setTabOrder(self.tree_extinfo, self.btn_exportmeta)
        QWidget.setTabOrder(self.btn_exportmeta, self.btn_exportproject)
        QWidget.setTabOrder(self.btn_exportproject, self.btn_restorediva)
        QWidget.setTabOrder(self.btn_restorediva, self.btn_restorelto)

        self.mnu_main.addAction(self.mnu_file.menuAction())
        self.mnu_main.addAction(self.menu_help.menuAction())

        self.retranslateUi(MainWindow)

        self.col_left.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Deep Worm", None))
        self.grp_activeshow.setTitle(QCoreApplication.translate("MainWindow", u"Active Show", None))
        self.lbl_dailiescount.setText(QCoreApplication.translate("MainWindow", u"No shots found.", None))
        ___qtreewidgetitem = self.tree_alldailies.headerItem()
        ___qtreewidgetitem.setText(8, QCoreApplication.translate("MainWindow", u"On LTO", None));
        ___qtreewidgetitem.setText(7, QCoreApplication.translate("MainWindow", u"On Diva", None));
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("MainWindow", u"Soundroll", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"Camroll", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"Take", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"Scene", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"End TC", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Start TC", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Shot", None));
        self.col_left.setTabText(self.col_left.indexOf(self.tab_alldailies), QCoreApplication.translate("MainWindow", u"All Dailies", None))
        self.col_left.setTabText(self.col_left.indexOf(self.tab_listtool), QCoreApplication.translate("MainWindow", u"List Tool", None))
        self.col_left.setTabText(self.col_left.indexOf(self.tab_monitors), QCoreApplication.translate("MainWindow", u"Monitors", None))
        self.grp_extinfo.setTitle(QCoreApplication.translate("MainWindow", u"Extended Info", None))
        ___qtreewidgetitem1 = self.tree_extinfo.headerItem()
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"Value", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Property", None));
        self.grp_export.setTitle(QCoreApplication.translate("MainWindow", u"Export Shots", None))
        self.btn_exportmeta.setText(QCoreApplication.translate("MainWindow", u"Export Metadata", None))
        self.btn_exportproject.setText(QCoreApplication.translate("MainWindow", u"Export Project File", None))
        self.grp_restore.setTitle(QCoreApplication.translate("MainWindow", u"Restore Shots", None))
        self.btn_restorediva.setText(QCoreApplication.translate("MainWindow", u"Restore from Diva", None))
        self.btn_restorelto.setText(QCoreApplication.translate("MainWindow", u"Pull from LTO", None))
        self.mnu_file.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
        self.menu_help.setTitle(QCoreApplication.translate("MainWindow", u"&Help", None))
    # retranslateUi

