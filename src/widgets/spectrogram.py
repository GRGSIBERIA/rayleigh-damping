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
        self.spectrum.set_xlabel("-> Frequency [Hz]")
        self.waveform.set_xlabel("-> Time [sec]")
        self.spectrum.set_ylabel("-> Relative Amplitude")
        self.waveform.set_ylabel("-> Relative Amplitude")
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
