import pandas as pd
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem

class Table():
	"""
	Table: A class that handles the loading and manipulating data on the main window
	"""

	ui = None
	csv_data = None
	columns = None
	rows = None

	def __init__(self, ui, filePath = None, fileType = None):
		self.ui = ui

		if filePath is None and fileType is None:
			self.ui.tableWidget.setRowCount(10)
			self.ui.tableWidget.setColumnCount(10)

	def openCSV(self, filePath):
		if not filePath.endswith('.csv'):
			return "not a valid file type"
		else:	
		#  swith(type): csv, .xlsx, etc to go here later
			self.csv_data = pd.read_csv(filePath)
		# 	# Lets open up this bad boy in pandas and make a table that handles it
			print('shape' + str(self.csv_data.shape))
			self.rows = self.csv_data.shape[0] + 1
			self.columns = self.csv_data.shape[1]
			self.ui.tableWidget.setRowCount(self.rows)
			self.ui.tableWidget.setColumnCount(self.columns)

			# Should probably look at widgets nd shit, table should probably be a widget if I had to guess
			self.populateColumns()
			self.populateRows()

	def populateColumns(self):
		"""
		setColumns: function that sets the top row of the table to the column names of the df
		Arguments:
			csv_data: need to grab columns attribute off of it to do this properly
		Returns:
			Nothing, sets top row of table to column name
		"""
		currentCol = 0
		for column in self.csv_data.columns:
			self.ui.tableWidget.setItem(0, currentCol, QTableWidgetItem(column))
			currentCol += 1


	def populateRows(self):
		"""
		populateRows: populate the rows under a header if there is a header, or starting at zero if there is no header
		This breaks for anything more than a few hundred records.  So that's when we're going to go into dectiles ;)
		Arguments:
			df: dataframe of data
		Returns:
			nothing, sets table widget to have df columns names and some top 10 rows of data

		To-Do:
			Make the currentRow = 1 sometimes be currentRow = 0 if there is no column headers above it, so need to see how to check for that
		"""
		if self.rows < 10:
			currentCol = 0
			currentRow = 1
			for row in self.csv_data.itertuples():
				print("row: " + str(row))
				firstItem = True
				for item in row:
					if firstItem:
						firstItem = False
						continue
					print("Going to set " + str(item) + " to row: " + str(currentRow) + ", column: " + str(currentCol))
					self.ui.tableWidget.setItem(currentRow, currentCol, QTableWidgetItem(str(item)))
					currentCol +=1
				currentRow += 1
				currentCol = 1
			# only do first ten rows, and 10 columns max


		pass

	def changeFromRawDataToDectile(self):
		"""
		changeFromRawDataToDectile: a function that changes the view of a column.  Don't see the actual raw data, see the 10 dectiles
		Arguments:
			df: dataframe of data
			column: specific column to set to dectiles
		Returns:
			Nothing, gives you the 10 dectiles for the data in the columns
		"""

	def changeFromDectileToRawData(self):
		"""
		changeFromDectileToRawData: a function that changes the view from dectil back to the actual raw data
		Arguments:
			df: dataframe of data
			column: specific column to reset
		Returns:
			Nothing, gives you the 10 dectiles for the data in the columns
		"""

