from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QBoxLayout, QTextEdit, QListWidget, QPushButton, QGridLayout

from UtilityComponents import utils
from GameComponents.Action import SubAction, BackAction


class GameWindow(QWidget):
    opensw = pyqtSignal(name='openSettingsWindow')

    def __init__(self, am):
        super(GameWindow, self).__init__()

        # CONSTANTS INIT
        self.HEIGHT = 300
        self.WIDTH = 500

        # VARIABLES INIT
        self.am = am
        self.sub_actions = None
        self.is_sub = False

        # WIDGETS INIT
        self.log_view = QTextEdit()
        self.actions_view = QListWidget()
        self.submit_button = QPushButton("Submit")
        self.settings_button = QPushButton("Settings")
        self.clear_button = QPushButton("Clear")

        # LAYOUT INIT
        self.layoutBox = QBoxLayout(QBoxLayout.TopToBottom, self)
        self.layoutGrid = QGridLayout()

        self.setUi()

    def setUi(self):
        '''
        Configuration of the widgets/layoutBox and showing the window
        '''
        # WINDOW CONFIG
        self.setGeometry(50, 50, self.WIDTH, self.HEIGHT)
        self.setWindowTitle("Lost In Siberia")
        # self.setWindowIcon(QtGui.QIcon('logo.png'))

        # WIDGETS CONFIG
        self.log_view.setAcceptRichText(True)
        self.log_view.setReadOnly(True)
        self.submit_button.clicked.connect(self.submitButtonEvent)
        self.settings_button.clicked.connect(self.settingsButtonEvent)
        self.clear_button.clicked.connect(self.clearButtonEvent)

        self.actions_view.setFixedHeight(46)
        # Debug sake
        for a in self.am.actions_list:
            self.actions_view.addItem(f"{a.desc}")

        # LAYOUT CONFIG
        self.layoutBox.addWidget(self.actions_view)
        self.layoutBox.addLayout(self.layoutGrid)
        self.layoutGrid.addWidget(self.submit_button, 1, 1)
        self.layoutGrid.addWidget(self.settings_button, 1, 2)
        self.layoutGrid.addWidget(self.clear_button, 1, 3)
        self.layoutBox.addWidget(self.log_view)
        self.show()

    def submitButtonEvent(self):
        action_desc = self.actions_view.currentItem().text()
        if not self.is_sub:
            action = utils.findAction(action_desc, self.am.actions_list)
        else:
            action = utils.findAction(action_desc, self.sub_actions)

        if isinstance(action, SubAction):
            self.sub_actions = action.activate()
            self.actions_view.clear()
            for a in self.sub_actions:
                self.actions_view.addItem(f"{a.desc}")
            self.is_sub = True
        elif isinstance(action, BackAction):
            self.sub_actions = None
            self.actions_view.clear()
            for a in self.am.actions_list:
                self.actions_view.addItem(f"{a.desc}")
            self.is_sub = False
        else:
            action.activate()
            self.log_view.insertPlainText(f"\n> {action}")
            self.log_view.insertHtml(f"\n{self.am.player}")


    def settingsButtonEvent(self):
        self.opensw.emit()

    def clearButtonEvent(self):
        self.log_view.clear()



