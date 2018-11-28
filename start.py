#See if I can refactor these following import statements, looks ugly
import os
import sys
from views.install import install
from views.main_window import main_window
from PyQt5.QtWidgets import QApplication

class setup(QApplication):
	"""
	This class serves as an object that can be used to initalize and control very basic high level information about the company.
	Arguments:
		None


	Attributes:
		installPath: the install path

	Methods:
		freshInstall: installs C:\\Program Files\\PyBiz and the few necessary text files
	"""
	installPath="C:\\Users\\karab\\Desktop\\temp\\PyBiz"
	settingsFile = installPath + "\settings.txt"
	installWindow = None
	mainWindow = None

	def __init__(self, parent=None):
		"""
		This funciton runs every single time the program runs.

		To-Do:
			The checking of if this is installed will have to be more 
		"""
		#Do we already have stuff about the business?  Lets find out!
		pyBizFolderExists = os.path.isdir(self.installPath)


		if pyBizFolderExists:
			#we already have a PyBiz folder installed
			#check for data
			print("There is a folder in " + self.installPath)
			# Delete later
			self.alreadyInstalled()
		else:
			#we gotta make one!
			print("There is not a folder in " + self.installPath)
			self.freshInstall()

	def freshInstall(self):
		"""
		freshInstall: method installs the appropriate directories and files if the user never used PyBiz before

		paramters:
			self: passed with every method in classes
		returns:
			nothing, sets the directory that this app will save setings/data info to
		"""

		print("starting freshInstall \n")
		app = QApplication(sys.argv)
		self.installWindow = install.Installer()
		app.exec_()
		print("we exited freshInstall start.py")
	
	def alreadyInstalled(self):
		"""
		alreadyInstalled: get setting values and open up the main window 

		parameters:
			self: passes entire instance of class to itself
		returns:
			nothing, opens up a hook to the main window with the settings
		"""
		app = QApplication(sys.argv)
		# Maybe pass in root path here to MainWindow?
		self.mainWindow = main_window.MainWindow()
		app.exec_()