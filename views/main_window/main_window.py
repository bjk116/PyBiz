#This needs to go into templates
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QTableWidget,QTableWidgetItem, QInputDialog, QLineEdit
import pandas as pd
import views.main_window.mainTable as mainTable
import views.dialogs.addMenu.addWindowDialog as addWindow
import sys
import model as m

class MainWindow(QMainWindow):
	"""
	MainWindow: a class that opens a main window and lets the user open csv files

	Arguments:
		None
	
	Attributes:
		rootPath: str, will be where that user's data is saved
		openCSV: 

	Methods:
		__init__: load ui, set up conditional texts and buttons, connect buttons to functions, and show ui

	"""

	rootPath = None
	openCSV = None
	windowData = None
	db = None
	dialogs = []
	viewTablesWidget = None

	def __init__(self, parent=None):
		# Load UI
		print("running init Main Window")
		super(MainWindow, self).__init__(parent)
		self.ui = uic.loadUi('views/main_window/main_window.ui', QMainWindow())

		# To-Do: Get User here later
		user = "Brian"

		# self.ui.actionOpen_CSV.triggered.connect(self.openCSVFile)
		self.ui.actionConnect_to_Database.triggered.connect(self.connectToDb)
		self.ui.actionAdd_Window.triggered.connect(self.addWindow)
		self.ui.actionAdd_Table.triggered.connect(self.addTable)
		self.ui.actionAdd_Component.triggered.connect(self.addComponent)
		self.ui.actionAdd_Relationship.triggered.connect(self.addRelationship)
		
		self.ui.listOfWindows.itemActivated.connect(self.listWindowItemActivated)
		self.refreshListOfWindows()
		# TO fix this rootpath should probably inherit from start.py?  Or Read from settings yea that makes more sense, read from settings based on
		# root path column info.  Or, auto make a folder like PyBiz\user\username
		self.rootPath = "C:"

		self.viewTablesWidget
		
		for p in sys.path:
			print("path" + p)

		print(sys.path[0])

		# Show Window
		self.ui.show()

	def addRelationship(self):
		pass

	def listWindowItemActivated(self):
		print("Item was activated")
		

	def refreshListOfWindows(self):
		print("Updating list of Windows")
		self.ui.listOfWindows.clear()

		cnx = m.db()
		queryData = cnx.selectAllFromTable("windows")

		if queryData:
			self.windowData = queryData

			for window in queryData:
				print(str(window))
				self.ui.listOfWindows.addItem(window[1])
			

		cnx.close()


	def addWindow(self):
		# self.dialogs.append(addWindow.addWindowDialog(refreshFunction = self.refreshListOfWindows()))
		tableName, okPressed = QInputDialog.getText(self, "Table Name","Table Name:", QLineEdit.Normal, "")
		if okPressed and tableName != '':
			tableDesc, okPressed2 = QInputDialog.getText(self, "Table Description","Description:", QLineEdit.Normal, "")
			if okPressed2 and tableDesc != '':
				
				cnx = m.db()
				cnx.insertIntoTable("windows", columns=["windowName", "description"], values=[tableName, tableDesc])
				cnx.cnx.close()
				self.ui.listOfWindows.addItem(tableName)

	def addTable(self):
		pass

	def addComponent(self):
		pass

	def connectToDb(self):
		pass