from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QLabel,
        QListView, QGridLayout, QHBoxLayout, QVBoxLayout, QApplication)
import PyQt5.QtCore as Qt

import sys
from templates import windows 


def handleSubmit(inputs):
	for i in inputs:
		print(i)

def init():
	print("Opening Initailize Server Window")
	questions = ["Port:", "Type", "Param 3"]
	serverWindow = windows.getForm("Initialize Server", questions, handleSubmit)
	serverWindow.setGeometry(100, 200, 500, 500)
	serverWindow.show()