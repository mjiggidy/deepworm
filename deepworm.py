#!/usr/bin/env python3

from PySide2 import QtUiTools, QtWidgets
from ui.wnd_main import Ui_MainWindow
import sys, pathlib

class MainWindow(QtWidgets.QMainWindow):

	def __init__(self):
		super(MainWindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

def main(argv):

	app = QtWidgets.QApplication(argv)

	wnd_main = MainWindow()
	wnd_main.show()

	sys.exit(app.exec_())


if __name__=="__main__":

	main(sys.argv)

