from PyQt5.QtWidgets import QWidget
from PyQt5.uic.properties import QtGui


class SettingsWindow(QWidget):
    def __init__(self):
        super(SettingsWindow, self).__init__()

        self.HEIGHT = 300
        self.WIDTH = 500

        self.setUi()

    def setUi(self):
        self.setGeometry(50, 50, self.WIDTH, self.HEIGHT)
        self.setWindowTitle("Lost In Siberia - Settings")
        # self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.show()
