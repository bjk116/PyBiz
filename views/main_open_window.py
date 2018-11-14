from PyQt5.QtWidgets import QInputDialog, QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):               
        
        serverInitAct = QAction(QIcon('images/server.png'), '&Initialize Server', self)        
        serverInitAct.setShortcut('Ctrl+S')
        serverInitAct.setStatusTip('Start a new server on a port')
        serverInitAct.triggered.connect(self.startServer)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Server')
        fileMenu.addAction(serverInitAct)
        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Python Ignition 0.0.1')    
        self.show()