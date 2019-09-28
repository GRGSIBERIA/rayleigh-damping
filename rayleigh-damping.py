import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sip


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.labelFreqA = QLabel(self)
        self.labelFreqA.setText("低周波側の周波数 [Hz]")
        self.editFreqA = QLineEdit()

        self.labelFreqB = QLabel(self)
        self.labelFreqB.setText("高周波側の周波数 [Hz]")
        self.editFreqB = QLineEdit()

        self.labelDampA = QLabel(self)
        self.labelDampA.setText("低周波側の減衰比")
        self.editDampA = QLineEdit()

        self.labelDampB = QLabel(self)
        self.labelDampB.setText("高周波側の減衰比")
        self.editDampB = QLineEdit()

        grid = QGridLayout(self)
        grid.setSpacing(10)

        grid.addWidget(self.labelFreqA, 1, 0)
        grid.addWidget(self.labelFreqB, 2, 0)
        grid.addWidget(self.labelDampA, 3, 0)
        grid.addWidget(self.labelDampB, 4, 0)

        grid.addWidget(self.editFreqA, 1, 1)
        grid.addWidget(self.editFreqB, 2, 1)
        grid.addWidget(self.editDampA, 3, 1)
        grid.addWidget(self.editDampB, 4, 1)

        self.setLayout(grid)
        self.setGeometry(300, 50, 400, 350)
        self.setWindowTitle("Rayleigh Damping")
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
