from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QLineEdit, QDialogButtonBox
import mysql.connector
from mysql.connector import errorcode

class addWindowDialog(QDialog):
	"""
	addWindowDialog: a class that encapuslates the  dialog window.  Allows user to input a new ignition window.

	"""
	def __init__(self, parent=None, refreshFunction = None):
		super(addWindowDialog, self).__init__(parent)
		self.ui = uic.loadUi('views/dialogs/addMenu/addWindowDialog/addWindow.ui', QDialog())

		# initialize triggers
		self.ui.accepted.connect(self.addNewWindowToDb)
		self.ui.rejected.connect(self.cancelButton)

		# set refresh function
		self.refreshFunction = refreshFunction
		# validation stuff here too
		self.ui.show()

	def cancelButton(self):
		self.ui.close()

	def addNewWindowToDb(self):
		print("attempting to add") 
		windowName = self.ui.windowName.text()
		windowDescription = self.ui.windowDescription.text()
		# We should make this passed in later on
		con = mysql.connector.connect(user='brian', password='admin',
                                  host='127.0.0.1',
                                  database='production')
		c = con.cursor(buffered=True)

		query = "SELECT * FROM windows WHERE windowName = \"" + windowName + "\""
		print("query: " + query)

		# print("lenght of result: " + str(result.rowcount))
		c.execute(query)
		result=c.fetchone()
		
		if result:
			# Then we don't have a window and we can safely add this one
			# Print an error, we have an existing row
			pass
		else:
			print("no rows found")		
			addQuery = "INSERT INTO windows (windowName, description) VALUES (\"" + windowName + "\", \"" + windowDescription + "\");"
			print("No existing table, adding " + windowName)
			print("addQuery: " + addQuery)
			c.execute(addQuery)
			con.commit()
			c.close()
			con.close()

		exec(self.refreshFunction)