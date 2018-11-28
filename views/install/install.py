#This needs to go into templates
from PyQt5.QtGui import QIcon
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QFileDialog
import os
import csv

class Installer(QMainWindow):
	"""
	This is a class that opens a main window and takes the user through installation

	Arguments:
		None
	
	Attributes:
		presetInstallDirectory: String, pre chosen install directory

	Methods:
		getPath: String, returns with a string path.  Can be closed, or fed an additional string of the next window to open

	"""

	currentPath = None

	def __init__(self, parent=None):
		# Load UI
		super(Installer, self).__init__(parent)
		self.ui = uic.loadUi('views/install/install.ui', QMainWindow())

		# Connect buttons and trigger events
		self.ui.next.enabled = self.canCreatePath()
		self.ui.userInputPath.textChanged.connect(self.canCreatePath)
		self.ui.chooseDirectoryBtn.clicked.connect(self.openFileDialog)
		self.ui.next.clicked.connect(self.setUpDirectory)

		# Show Window
		self.ui.show()
	
	def canCreatePath(self):
		"""
		self.canCreatePath: function determines if the next button is enabled/if the path is viable
		Arguments:
			self: entire class
		Returns:
			Nothing, sets the next button to enabled or not depending on if the path is viable
		"""
		self.currentPath = self.ui.userInputPath.text()

		try:
			print("checking path of: ", self.currentPath)
			pathViable = not (os.path.isdir(self.currentPath))
			self.ui.next.setEnabled(pathViable)
		except TypeError:
			self.ui.next.setEnabled(False)

	def openFileDialog(self):
		"""
		openFileDialog: function is triggered by the chooseDirectoryBtn QToolButton
		Arguments:
			self: entire class
		Returns:
			Nothing, sets the userInputPath to the new chose path
		"""
		# Get directory for install from user
		self.currentPath = QFileDialog.getExistingDirectory(self, 'Choose Parent Directory')
		self.currentPath = self.currentPath.replace('/','\\') + "\\" + "PyBiz"
		
		# Set it and check if next button is ok
		self.ui.userInputPath.setText(self.currentPath)
		self.canCreatePath()

	def setUpDirectory(self):
		"""
		nextInstallWindow: function sets up directory and opens up the main window
		Arguments:
			self: entire class
		Returns:
			Nothing, creates directory for PyBiz and moves foward
		"""
		print("making setUpDirectory in: ", self.currentPath)

		# To-Do: Put a dialog box here to get a user, a password, and a valid email address

		os.mkdir(self.currentPath)

		subfolders = ['data', 'bin', 'settings']
		for folder in subfolders:
			os.mkdir(self.currentPath + '\\' + folder)

		settings = self.currentPath + '\\' + 'settings' + '\\settings.csv'
		with open(settings, 'w') as csvfile:
			settingFields = ['Name', 'Company', 'Email']
			writer = csv.DictWriter(csvfile, fieldnames=settingFields)

			writer.writeheader()
			writer.writerow({'Name': 'Brian', 'Company': 'PSI Inc', 'Email': 'karabinchak.brian@gmail.com'})

		self.ui.close()
		print("successfully created folder")
		print("we eixted setupDirectory in install.py")
