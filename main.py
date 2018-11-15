import sys
from PyQt5.QtWidgets import QApplication        
import start

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    s = start.setup()
    sys.exit(app.exec_())