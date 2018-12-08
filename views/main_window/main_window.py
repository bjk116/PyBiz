#This needs to go into templates
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QTableWidget,QTableWidgetItem
import pandas as pd
import views.main_window.mainTable as mainTable
import views.dialogs.addMenu.addWindowDialog as addWindow
import sys
import mysql.connector
from mysql.connector import errorcode

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
	mainTable = None
	db = None
	dialogs = []

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

		cnx = self.connectToDb()
		query = "SELECT windowName FROM windows"
		if cnx:
			cursor = cnx.cursor()
			cursor.execute(query)
			
			for windowName in cursor:
				print(windowName[0])
				self.ui.listOfWindows.addItem(windowName[0])
			
			cursor.close()
			cnx.close()


	def addWindow(self):
		print("open window dialog")
		self.dialogs.append(addWindow.addWindowDialog(refreshFunction = self.refreshListOfWindows()))

	def addTable(self):
		pass

	def addComponent(self):
		pass

	def openCSVFile(self):
		"""
		openCSVFile: A function that opens and then populates the main window with the .csv file data
		Arguments:
			self: pass in instance of class
		Returns:
			Nothing, populates the table in the window with .csv file data
		"""
		# Not sure what QFileDialog.options does, should look up
		options = QFileDialog.Options()
		filePath, _ = QFileDialog.getOpenFileName(self,"Open CSV...", "","All Files (*);;CSV Files (*.csv)", options=options)
		
		self.mainTable.openCSV(filePath)

	def connectToDb(self):
		"""
		connectToDb: connect to a MySQL database
		Arguments:

		Returns:
			self.db: connection to the database 
		"""
		try:
			cnx = mysql.connector.connect(user='brian',password='admin', host='127.0.0.1', database='production')
			print("connected")
			# Return a cursor object
			return cnx
		except mysql.connector.Error as err:
			if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
				print("Something is wrong with your user name or password")
				return ""
			elif err.errno == errorcode.ER_BAD_DB_ERROR:
				print("Database does not exist")
				return ""
			else:
				print(err)
				return ""
		else:
			cnx.close()
			return ""