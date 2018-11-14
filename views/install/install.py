import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QDesktopWidget, QGridLayout, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
 
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'Welcome to Installing PyBiz!'
        self.left = 0
        self.top = 0
        self.width = 600
        self.height = 750
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        #Centers the screen on the desktop
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        grid = QGridLayout()
        grid.setSpacing(10)
        

        # Create textbox
        instructions = QLabel('Please pick what directory you would like PyBiz to be installed in')
        grid.addWidget(instructions, 1, 0)
        
        # Box for directories
        directoryPath = QLineEdit()
        grid.addWidget(directoryPath,1,1)

        # Create a button in the window
        submitDirectory = QPushButton('Next Window', self)
        grid.addWidget(submitDirectory,2,1)
        
        self.setLayout(grid)
        # connect button to function on_click
        # self.button.clicked.connect(self.on_click)
        self.show()
 
    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")