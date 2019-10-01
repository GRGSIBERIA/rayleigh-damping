import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import numpy as np


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setGeometry(300, 50, 400, 600)
        self.setWindowTitle("Damping Analyser")
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())