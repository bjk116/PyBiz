import sys
from PyQt5.QtWidgets import QApplication        
from util import start

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    start.setup()
    sys.exit(app.exec_())