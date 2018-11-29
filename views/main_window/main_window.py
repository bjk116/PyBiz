#This needs to go into templates
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QTableWidget,QTableWidgetItem
import pandas as pd
import views.main_window.mainTable as mainTable
import sys

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

	def __init__(self, parent=None):
		# Load UI
		print("running init Main Window")
		super(MainWindow, self).__init__(parent)
		self.ui = uic.loadUi('views/main_window/main_window.ui', QMainWindow())

		# To-Do: Get User here later
		user = "Brian"

		self.ui.actionOpen_CSV.triggered.connect(self.openCSVFile)
		# TO fix this rootpath should probably inherit from start.py?  Or Read from settings yea that makes more sense, read from settings based on
		# root path column info.  Or, auto make a folder like PyBiz\user\username
		self.rootPath = "C:"
		
		for p in sys.path:
			print("path" + p)

		print(sys.path[0])
		self.mainTable = mainTable.Table(self.ui)

		# Show Window
		self.ui.show()

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