import sys

from PyQt5.QtWidgets import QApplication

from GameComponents.GameManager import GameManager
from UiComponents.GameUi import GameWindow
from GameComponents.Player import Player
from UiComponents.SettingsUi import SettingsWindow


def openSettings():
    global sw
    sw = SettingsWindow()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    p = Player("Sqaarf")
    am = GameManager(p)
    gw = GameWindow(am)
    sw = None
    gw.opensw.connect(openSettings)
    sys.exit(app.exec_())
