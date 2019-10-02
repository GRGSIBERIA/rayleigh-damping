import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import numpy as np
import matplotlib
import matplotlib.pyplot as plot
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class SpectrogramWidget(QWidget):
    def __init__(self, parent=None):
        super(SpectrogramWidget, self).__init__(parent)
        self.__initInstances()
        self.__initLayout()


    def __initFigure(self):
        self.spectrum.set_title("Spectrum")
        self.waveform.set_title("Waveform")
        self.fig.tight_layout()


    def __initInstances(self):
        self.fig = plot.figure(figsize=(4,3))
        self.spectrum = self.fig.add_subplot(212)
        self.waveform = self.fig.add_subplot(211)
        self.canvas = FigureCanvas(self.fig)
        self.__initFigure()


    def __initLayout(self):
        vbox = QVBoxLayout(self)

        vbox.addWidget(self.canvas)
        self.canvas.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)

        self.setLayout(vbox)


class TabAnalyseSpectrum(QWidget):
    def __init__(self, parent=None):
        super(TabAnalyseSpectrum, self).__init__(parent)
        self.__initInstances()
        self.__initLayout()

    
    def __initInstances(self):
        self.wavfileLabel = QLabel("WAV File", self)
        self.wavfileEdit = QLineEdit("", self)
        self.wavfileDialog = QPushButton("...", self)
        self.executeButton = QPushButton("Show Spectrogram", self)
        self.canvas = SpectrogramWidget(self)
        self.table = QTableWidget(self)
    

    def __initLayout(self):
        baselayout = QHBoxLayout(self)
        self.setLayout(baselayout)
        
        tabularFormLayout = QVBoxLayout(self)

        wavfieldLayout = QHBoxLayout(self)
        wavfieldLayout.addWidget(self.wavfileLabel)
        wavfieldLayout.addWidget(self.wavfileEdit)
        wavfieldLayout.addWidget(self.wavfileDialog)
        tabularFormLayout.addLayout(wavfieldLayout)

        executeLayout = QHBoxLayout(self)
        executeLayout.addWidget(self.executeButton, alignment=(Qt.AlignRight))
        tabularFormLayout.addLayout(executeLayout)

        tabularFormLayout.addWidget(self.table)
        baselayout.addLayout(tabularFormLayout)
        
        canvasLayout = QVBoxLayout(self)
        canvasLayout.addWidget(self.canvas)

        baselayout.addLayout(canvasLayout)


class TabAnalyseDamping(QWidget):
    def __init__(self, parent=None):
        super(TabAnalyseDamping, self).__init__(parent)


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.__initInstances()
        self.__initLayout()
        self.__initEvent()

        self.setGeometry(300, 50, 1024, 768)
        self.setWindowTitle("Damping Analyser")


    def __initInstances(self):
        self.tabs = QTabWidget()
        self.tabspec = TabAnalyseSpectrum(self)
        self.tabdamp = TabAnalyseDamping(self)
        self.tabs.addTab(self.tabspec, "spectrums")
        self.tabs.addTab(self.tabdamp, "damping")


    def __initLayout(self):
        baselayout = QVBoxLayout(self)
        baselayout.addWidget(self.tabs)
        self.setLayout(baselayout)


    def __initEvent(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
