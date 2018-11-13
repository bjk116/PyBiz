from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QLabel,
        QListView, QGridLayout, QHBoxLayout, QVBoxLayout, QApplication, QDialog)
import PyQt5.QtCore as Qt
import sys

def getForm(title, questions, handleSubmit):
	return FormWindow(title, questions, handleSubmit)

class FormWindow(QDialog):
	"""
	A class that returns a new window that has the form of questions, inputs, and a submit button.
	Currently, only allows text labels freely answered.

	Arguments:
		title: String, title of the window, typically title of the form
		questions: list of strings, of the form ['form question 1,' 'form question 2', ... 'form question n']
		handleSubmit: function that accepts a single list parameter, which will be the responses to the questions passed in
		
	Methods:
		onClick_submitBtn: handl
	"""
	def __init__(self, title, questions, handleSubmit):
		super(). __init__()

		#Later, make 500,500 determined on form size
		self.setWindowTitle(title)
		self.questions = questions
		self.handleSubmit = handleSubmit
		self.inputs = []

		self.initUI()

	def initUI(self):

		#Grid layout - 1 Column, multiple rows
		grid = QGridLayout()

		row = 0
		for question in self.questions:
			grid.addWidget(QLabel(question),row, 0)
			grid.addWidget(QLineEdit(),row,1)
			row += 1


		self.submitInputsBtn = QPushButton("Submit")
		grid.addWidget(self.submitInputsBtn, row, 0)

		self.submitInputsBtn.clicked.connect(self.handleSubmit)

		self.setLayout(grid)

	def run(self):
		#Calling show from QWidget class
		self.setGeometry(100, 200, 500, 500)
		self.show()