import sys
import os.path
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import numpy as np
from src.wavereader import WaveData
from src.widgets.spectrogram import SpectrogramWidget

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
        self.saveButton = QPushButton("Save select cell datum into damping", self)
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
        tabularFormLayout.addWidget(self.saveButton)
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
