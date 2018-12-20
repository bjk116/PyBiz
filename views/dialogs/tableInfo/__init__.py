from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QLineEdit, QDialogButtonBox
import model as m


class tableInfoDialog(QDialog):
	"""
	tableInfoDialog: a class that encapuslates the  dialog window.  Allows user to input a new ignition window.

	"""
	idx = None

	def __init__(self, parent=None, idx = None, tableName = None, tableDescription = None):
		super(tableInfoDialog, self).__init__(parent)
		self.ui = uic.loadUi('views/dialogs/tableInfo/tableInfoDialog.ui', QDialog())

		# Initialize event functions and text fields
		self.ui.accepted.connect(self.saveToDb)
		self.ui.rejected.connect(self.cancelButton)

		if idx:
			self.idx = idx
			self.ui.idx.setText(str(idx))
		if tableName:
			self.ui.tableNameLE.setText(tableName)
		if tableDescription:
			self.ui.tableDescriptionLE.setText(tableDescription)

		self.ui.show()

	def cancelButton(self):
		print("message box possible? Are you sure you want to close? unsaved changes blah")
		self.ui.close()

	def saveToDb(self):
		tableName = self.ui.tableNameLE.text()
		tableDescription = self.ui.tableDescriptionLE.text()

		# updateQuery = "UPDATE windows SET tableName = %s, tableDescription = %s WHERE idx = %i;" % (tableName, tableDescription, self.idx)
		cnx = m.db()
		updateQuery = "UPDATE windows SET windowName = \"%s\", description = \"%s\" WHERE idx = %i;" % (tableName, tableDescription, self.idx)
		cnx.updateQuery(updateQuery)
		cnx.close()