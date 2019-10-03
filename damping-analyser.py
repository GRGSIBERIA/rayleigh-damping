import sys
import os.path
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import numpy as np
import matplotlib
import matplotlib.pyplot as plot
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from src.wavereader import WaveData

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


class TabAnalyseSpectrum(QWidget):
    def __init__(self, parent=None):
        super(TabAnalyseSpectrum, self).__init__(parent)
        self.__initInstances()
        self.__initLayout()
        self.__initEvent()

    
    def __initInstances(self):
        self.wavfileLabel = QLabel("WAV File", self)
        self.wavfileEdit = QLineEdit("", self)
        self.wavfileDialog = QPushButton("...", self)
        self.fftSampleLabel = QLabel("FFT Sample Size", self)
        self.fftSampleEdit = QLineEdit("1024", self)
        self.frameShiftLabel = QLabel("FFT Frame Shift", self)
        self.frameShiftEdit = QLineEdit("50", self)
        self.executeButton = QPushButton("Show Spectrogram", self)
        self.canvas = SpectrogramWidget(self)
        self.table = QTableWidget(self)
    

    def __initLayout(self):
        baselayout = QHBoxLayout(self)
        self.setLayout(baselayout)
        
        tabularFormLayout = QVBoxLayout(self)

        fftGridLayout = QGridLayout(self)
        fftGridLayout.addWidget(self.fftSampleLabel, 0, 0)
        fftGridLayout.addWidget(self.fftSampleEdit, 0, 1)
        fftGridLayout.addWidget(self.frameShiftLabel, 1, 0)
        fftGridLayout.addWidget(self.frameShiftEdit, 1, 1)
        tabularFormLayout.addLayout(fftGridLayout)

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


    def __showFileDialog(self):
        fname = QFileDialog.getOpenFileName(self, "Open WAV File", "./", "WAV(*.wav)")

        if len(fname) > 0:
            self.wavfileEdit.setText(fname[0])
        else:
            QMessageBox.critical(self, "ERROR", "Can't select a wev file")


    def __importWavIntoTable(self):
        fftSample = int(self.fftSampleEdit.text())
        frameShift = int(self.frameShiftEdit.text())
        path = self.wavfileEdit.text()

        if os.path.exists(path):
            self.wav = WaveData(path, fftSample, frameShift)
            self.table.setColumnCount(len(self.wav.hLabels))    # 列数
            self.table.setRowCount(len(self.wav.vLabels))       # 行数
            self.table.setHorizontalHeaderLabels(self.wav.hLabels)
            self.table.setVerticalHeaderLabels(self.wav.vLabels)

            for timeid, times in enumerate(self.wav.spectrogram):
                for ampid, amp in enumerate(times):
                    self.table.setItem(timeid, ampid, QTableWidgetItem(str(amp)))
        else:
            QMessageBox.critical(self, "ERROR", "Not valid a wav file")


    def __initEvent(self):
        self.wavfileDialog.clicked.connect(self.__showFileDialog)
        self.executeButton.clicked.connect(self.__importWavIntoTable)


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
