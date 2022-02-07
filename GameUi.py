from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QBoxLayout, QTextEdit, QListWidget, QPushButton, QListView, QGridLayout


class GameWindow(QWidget):
    opensw = pyqtSignal(name='openSettingsWindow')

    def __init__(self, am):
        super(GameWindow, self).__init__()

        # CONSTANTS INIT
        self.HEIGHT = 300
        self.WIDTH = 500

        # VARIABLES INIT
        self.am = am


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
            self.actions_view.addItem(f"{a.name}")

        # LAYOUT CONFIG
        self.layoutBox.addWidget(self.actions_view)
        self.layoutBox.addLayout(self.layoutGrid)
        self.layoutGrid.addWidget(self.submit_button, 1, 1)
        self.layoutGrid.addWidget(self.settings_button, 1, 2)
        self.layoutGrid.addWidget(self.clear_button, 1, 3)
        self.layoutBox.addWidget(self.log_view)
        self.show()

    def submitButtonEvent(self):
        action = self.am.findByName(self.actions_view.currentItem().text())

        self.log_view.insertPlainText(f"\n> {action}")
        action.activate()

        self.log_view.insertHtml(f"\n{self.am.player}")

        self.log_view.insertHtml(f"<script>document.getElementById('test').innerHTML = 'test'</script>")
        # self.log_view.insertPlainText("\n"+self.actions_view.currentItem().text())

    def settingsButtonEvent(self):
        self.opensw.emit()

    def clearButtonEvent(self):
        self.log_view.clear()



