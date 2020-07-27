from PySide2 import QtCore, QtWidgets
from upco_tools import upco_shot, upco_deepworm
import sys

class DailiesModel(QtCore.QAbstractItemModel):
	
	def __init__(self, in_nodes):
		super().__init__()
		self._root = CustomNode(None)

		for node in in_nodes:
			self._root.addChild(node)

		# use items = upco_shot.Shotlist()?
	
	def addChild(self, in_node, in_parent):					# in_parent is a QModelIndex to the parent
		if not in_parent or not in_parent.isValid():		# Will be not supplied or invalid if it's top-level
			parent = self._root								# Otherwise returns the object
		else:
			parent = in_parent.internalPointer()
		print("Adding child to model:",type(parent))
		parent.addChild(in_node)
	
	def rowCount(self, in_index):
		# Only need to return the length of the root items
		# in_index is a QModelIndex
		if in_index.isValid():
			return in_index.internalPointer().childCount()
		else:
			return self._root.childCount()

	def columnCount(self, in_index):
		# Thisll be them headers
		if in_index.isValid():
			return in_index.internalPointer().columnCount()
		
		return self._root.columnCount()
	
	def data(self, in_index, role):
		if not in_index.isValid():
			return None
		node = in_index.internalPointer()
		if role == QtCore.Qt.DisplayRole:
			return node.data(in_index.column())
		else:
			return None
	
	def index(self, in_row, in_column, in_parent=None):
		if not in_parent or not in_parent.isValid():
			parent = self._root
		else:
			parent = in_parent.internalPointer()
		
		print("Parent type is",type(parent))
		print("Queried by in_parent", type(in_parent))
		print(type(in_row), type(in_column))
		
		#if not QtCore.QAbstractItemModel.hasIndex(self, in_row, in_column, in_parent):
		if not self.hasIndex(in_row, in_column, in_parent):
			return QtCore.QModelIndex()
		
		child = parent.child(in_row)
		if child:
			#return QtCore.QAbstractItemModel.createIndex(self, in_row, in_column, child)
			return self.createIndex(in_row, in_column, child)
		else:
			return QtCore.QModelIndex()
	
	def parent(self, in_index):
		if in_index.isValid():
			p = in_index.internalPointer().parent()
			if p:
				#return QtCore.QAbstractItemModel.createIndex(self, p.row(), 0, p)
				return self.createIndex(p.row(), 0, p)
		return QtCore.QModelIndex()
	


# Dis a item
# So like a shot object
class CustomNode:
	
	def __init__(self, in_data):
		
		if type(in_data) == tuple:
			self._data = list(in_data)
		else:
			self._data = [in_data]

		self._columncount = len(self._data)
		self._children = []
		self._parent = None
		self._row = 0
	
	def data(self, in_column):
		if in_column >= 0 and in_column < len(self._data):
			return self._data[in_column]
		
	def columnCount(self):
		return self._columncount
	
	# How many child rows
	def childCount(self):
		return len(self._children)

	# Get a child item
	def child(self, in_row):
		if in_row >= 0 and in_row < self.childCount():
			return self._children[in_row]
	
	def parent(self):
		return self._parent
	
	def row(self):
		return self._row
	
	def addChild(self, in_child):
		in_child._parent = self
		in_child._row = len(self._children) # Add to end of rows I guess
		self._children.append(in_child)
		self._columncount = max(in_child.columnCount(), self._columncount)

	

	


class Deepworm(QtWidgets.QApplication):

	def __init__(self):
		super().__init__()

		self.wnd_main = QtWidgets.QMainWindow()
		self.tree_dailies = QtWidgets.QTreeView()

		items = []
		dw = upco_deepworm.DeepwormClient()
		shows = dw.getShowList()
		for show in shows:
			
			items.append(CustomNode(show.get("title")))
			
			print(f"Getting show list for {show.get('title')}")
			for shot in dw.getShotList(show.get("guid_show")):
			#	print(f"Adding {shot.shot}")
				items[-1].addChild(CustomNode((shot.shot, str(shot.tc_start), str(shot.tc_end))))
			print(f"Done with {show.get('title')}\n")
		self.model_dailies = DailiesModel(items)

		self.setupWidgets()
		
		self.wnd_main.show()
	
	def setupWidgets(self):
		self.tree_dailies.setModel(self.model_dailies)
		self.wnd_main.setCentralWidget(self.tree_dailies)
		self.tree_dailies.setSortingEnabled(True)


def main():

	app = Deepworm()
	sys.exit(app.exec_())

if __name__ == "__main__":

	main()