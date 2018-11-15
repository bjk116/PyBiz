#See if I can refactor these following import statements, looks ugly
import os
from views.install import install

class setup():
	"""
	This class serves as an object that can be used to initalize and control very basic high level information about the company.

	Fields:
		installPath: the install path

	Methods:
		freshInstall: installs C:\\Program Files\\PyBiz and the few necessary text files
	"""
	installPath="C:\\Program Files\\PyBiz"
	settingsFile = installPath + "\settings.txt"
	installWindow = None

	def __init__(self):
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
			self.freshInstall()
		else:
			#we gotta make one!
			print("There is not a folder in " + self.installPath)
			self.freshInstall()

	def freshInstall(self):
		"""
		This method installs the appropriate directories and files if the user never used PyBiz before

		paramters:
			self: passed with every method in classes
		returns:
			nothing, sets the directory that this app will save setings/data info to
		"""

		freshInstall = install.chooseDirectory('Welcome to PyBiz!  Before we continue, please pick where you want to save program data.', 'C:\Program Files\PyBiz')

		# os.mkdir(self.installPath)
		
		# folders = ['Settings', 'Users', 'Data']
		
		# for folder in folders:
		# 	os.mkdir(self.installPath"\\"+folder)

		# To-Do: Everything beneath this I am realizing should be in its own fucking class window.fuck

		# chooseDirecory= install.chooseDirectory()
		

		#Get Directory with validation