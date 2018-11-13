#See if I can refactor these following import statements, looks ugly
import sys, os
sys.path.insert(0, os.path.abspath('..'))
import templates, views
from templates import windows
from views import install
from install import install

class setup():
	"""
	This class serves as an object that can be used to initalize and control very basic high level information about the company.

	Fields:
		installPath: the install path

	Methods:
		freshInstall: installs C:\\Program Files\\PyBiz and the few necessary text files
	"""
	installPath="C:\\Program Files\\PyBiz"
	settingsFile = installPath + "\\settings.txt"

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
		else:
			#we gotta make one!
			print("There is not a folder in " + self.installPath)
			self.freshInstall()

	def freshInstall(self):
		"""
		This method installs the appropriate directories and files if the user never used PyBiz before

		"""
		os.path.mkdir(self.installPath)
		os.chdir(self.installPath)
		folders = ['Projects', 'Expense Reports', 'Invoices', 'Quotes', 'Employees']
		
		for folder in folders:
			os.path.mkdir('\\'+folder)

		self.getCompanyInfo()

	def getCompanyInfo(self):
		"""
		Opens the first dialog box the user will ever see, to enter some basic information about the comapny
		"""
		install.app()