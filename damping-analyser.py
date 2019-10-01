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
        self.fig = plot.figure()
        self.spectrum = self.fig.add_subplot(212)
        self.waveform = self.fig.add_subplot(211)
        self.canvas = FigureCanvas(self.fig)
        self.__initFigure()


    def __initLayout(self):
        vbox = QVBoxLayout(self)
        vbox.addWidget(self.canvas)
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
        
        vbox = QVBoxLayout(self)

        hbox = QHBoxLayout(self)
        hbox.addWidget(self.wavfileLabel)
        hbox.addWidget(self.wavfileEdit)
        hbox.addWidget(self.wavfileDialog)
        vbox.addLayout(hbox)

        hbox = QHBoxLayout(self)
        hbox.addWidget(self.executeButton, alignment=(Qt.AlignRight))
        vbox.addLayout(hbox)

        vbox.addWidget(self.table)
        baselayout.addLayout(vbox)
        
        vbox = QVBoxLayout(self)
        vbox.addWidget(self.canvas)

        baselayout.addLayout(vbox)


class TabAnalyseDamping(QWidget):
    def __init__(self, parent=None):
        super(TabAnalyseDamping, self).__init__(parent)


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.__initInstances()
        self.__initLayout()
        self.__initEvent()

        self.setGeometry(300, 50, 600, 600)
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
