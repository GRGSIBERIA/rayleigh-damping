import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sip
import matplotlib
import matplotlib.pyplot as plot
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.__initInstances()
        self.__initLayouts()

        self.executeButton.clicked.connect(self.__updateGraph)

        self.setGeometry(300, 50, 400, 350)
        self.setWindowTitle("Rayleigh Damping")
        
    def __updateGraph(self):
        omega1 = float(self.editFreqA.text()) * 2. * np.pi
        omega2 = float(self.editFreqB.text()) * 2. * np.pi
        damp1 = float(self.editDampA.text())
        damp2 = float(self.editDampB.text())
        alpha = (2. * omega1 * omega2 * (damp1 * omega2 - damp2 * omega1)) / (omega2**2. - omega1**2.)
        beta = (2. * (damp2 * omega2 - damp1 * omega1)) / (omega2**2. - omega1**2.)
        self.resultAlpha.setText(str(alpha))
        self.resultBeta.setText(str(beta))


    def __initInstances(self):
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

        self.labelAlpha = QLabel(self)
        self.labelAlpha.setText("α")
        self.resultAlpha = QLabel(self)
        self.resultAlpha.setText("0.0")

        self.labelBeta = QLabel(self)
        self.labelBeta.setText("β")
        self.resultBeta = QLabel(self)
        self.resultBeta.setText("0.0")

        self.fig = plot.figure()
        self.canvas = FigureCanvas(self.fig)
        self.axis = self.fig.add_subplot(111)

        self.executeButton = QPushButton("計算", self)


    def __initLayouts(self):
        vbox = QVBoxLayout(self)

        grid = QGridLayout(self)
        grid.setSpacing(10)

        grid.addWidget(self.labelFreqA, 1, 0)
        grid.addWidget(self.labelFreqB, 2, 0)
        grid.addWidget(self.labelDampA, 3, 0)
        grid.addWidget(self.labelDampB, 4, 0)
        grid.addWidget(self.labelAlpha, 5, 0)
        grid.addWidget(self.labelBeta, 6, 0)
        grid.addWidget(self.executeButton, 7, 0)

        grid.addWidget(self.editFreqA, 1, 1)
        grid.addWidget(self.editFreqB, 2, 1)
        grid.addWidget(self.editDampA, 3, 1)
        grid.addWidget(self.editDampB, 4, 1)
        grid.addWidget(self.resultAlpha, 5, 1)
        grid.addWidget(self.resultBeta, 6, 1)

        vbox.addLayout(grid)
        vbox.addWidget(self.canvas)

        self.setLayout(vbox)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
