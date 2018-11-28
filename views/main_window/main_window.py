#This needs to go into templates
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QTableWidget,QTableWidgetItem
import pandas as pd

class MainWindow(QMainWindow):
	"""
	MainWindow: a class that opens a main window and lets the user open csv files

	Arguments:
		None
	
	Attributes:
		None

	Methods:
		__init__: load ui, set up conditional texts and buttons, connect buttons to functions, and show ui

	"""
	rootPath = None
	openCSV = None

	def __init__(self, parent=None):
		# Load UI
		super(MainWindow, self).__init__(parent)
		self.ui = uic.loadUi('views/main_window/main_window.ui', QMainWindow())

		# To-Do: Get User here later
		user = "Brian"

		self.ui.actionOpen_CSV.triggered.connect(self.openCSVFile)
		# TO fix this rootpath should probably inherit from start.py?  Or Read from settings yea that makes more sense, read from settings based on
		# root path column info.  Or, auto make a folder like PyBiz\user\username
		self.rootPath = "C:"

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
		fileName, _ = QFileDialog.getOpenFileName(self,"Open CSV...", "","All Files (*);;CSV Files (*.csv)", options=options)
		

		
		if fileName and fileName[-4:] == '.csv':
			print(fileName)

			csv_file = pd.read_csv(fileName)
			# Lets open up this bad boy in pandas and make a table that handles it
			print('shape' + str(csv_file.shape))
			self.ui.tableWidget.setRowCount(csv_file.shape[0])
			self.ui.tableWidget.setColumnCount(csv_file.shape[1])
			# Should probably look at widgets nd shit, table should probably be a widget if I had to guess
			# self.ui.tableWidget()