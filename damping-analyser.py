import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import numpy as np


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
    

    def __initLayout(self):
        baselayout = QVBoxLayout(self)

        hbox = QHBoxLayout(self)
        hbox.addWidget(self.wavfileLabel)
        hbox.addWidget(self.wavfileEdit)
        hbox.addWidget(self.wavfileDialog)
        baselayout.addLayout(hbox)

        

        self.setLayout(baselayout)


class TabAnalyseDamping(QWidget):
    def __init__(self, parent=None):
        super(TabAnalyseDamping, self).__init__(parent)


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.__initInstances()
        self.__initLayout()
        self.__initEvent()

        self.setGeometry(300, 50, 400, 600)
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
