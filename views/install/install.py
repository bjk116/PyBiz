#This needs to go into templates
from PyQt5 import QtGui
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
import os

class chooseDirectory(QDialog):
	"""
	This is a class that opens a window that allows for choosing a direcotry
	Arguments:
		topText: String, what do you want it to say about the input
	
	Attributes:


	Methods:
		getPath: String, returns with a string path.  Can be closed, or fed an additional string of the next window to open

	"""

	def __init__(self, topText, presetDirectory, parent=None):
		super(chooseDirectory, self).__init__(parent)
		self.directoryWindow = uic.loadUi('views/install/install.ui', QDialog())
		#Check if C:\Program Files\PyBiz is available, and if not, disable the create directory button on start
		self.directoryWindow.createDirectoryBtn.enabled = self.canCreatePath()
		self.directoryWindow.userInputPath.text=presetDirectory
		self.directoryWindow.userInputPath.textChanged.connect(self.canCreatePath)
		self.directoryWindow.show()

	
	def canCreatePath(self):
		"""
		This function determins if the create button should be enabled
		Arguments:
			path: string, of path to put directory
		Returns:
			Boolean, true if you can create the directory there, false if you
		"""
		return not (os.path.isdir(self.directoryWindow.userInputPath.text))