#!/usr/bin/env python3

from PySide2 import QtUiTools, QtWidgets
import sys, pathlib

def main(argv):

	app = QtWidgets.QApplication(argv)

	ui_file = pathlib.Path(pathlib.Path(__file__).parent, "ui", "wnd_main_commonext.ui")
	ui_loader = QtUiTools.QUiLoader()
	window = ui_loader.load(str(ui_file), None)
	window.show()

	sys.exit(app.exec_())


if __name__=="__main__":

	main(sys.argv)

