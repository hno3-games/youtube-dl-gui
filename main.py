from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import QtGui
import sys
import os
import wx
from styles import styles_white_background, styles_black_background


class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.init()

    def init(self):
        self.video_download_preferences = ["Video + Audio", "Video only", "Audio only"]
        self.video_quality_preferences = ["Best", "Worst"]
        self.feedback_button = QPushButton()
        self.feedback_button.setStyleSheet(
            styles_black_background.button_new_page_style
        )
        feedback_icon = QtGui.QPixmap("icons/feedback.png")
        self.feedback_button.setIcon(QtGui.QIcon(feedback_icon))
        self.feedback_button.setIconSize(QtCore.QSize(32, 32))
        self.history_button = QPushButton(self)
        self.history_button.setStyleSheet(styles_black_background.button_new_page_style)
        history_icon = QtGui.QPixmap("icons/history.png")
        self.history_button.setIcon(QtGui.QIcon(history_icon))
        self.history_button.setIconSize(QtCore.QSize(32, 32))
        self.settings_button = QPushButton()
        self.settings_button.setStyleSheet(
            styles_black_background.button_new_page_style
        )
        settings_icon = QtGui.QPixmap("icons/settings.png")
        self.settings_button.setIcon(QtGui.QIcon(settings_icon))
        self.settings_button.setIconSize(QtCore.QSize(32, 32))
        self.add_button = QPushButton()
        self.add_button.setStyleSheet(styles_black_background.add_button_style)
        add_icon = QtGui.QPixmap("icons/plus.png")
        self.add_button.setIcon(QtGui.QIcon(add_icon))
        self.add_button.setIconSize(QtCore.QSize(32, 32))
        self.delete_button = QPushButton()
        self.delete_button.setStyleSheet(styles_black_background.delete_button_style)
        delete_icon = QtGui.QPixmap("icons/delete.png")
        self.delete_button.setIcon(QtGui.QIcon(delete_icon))
        self.delete_button.setIconSize(QtCore.QSize(32, 32))
        self.download_button = QPushButton()
        self.download_button.setStyleSheet(
            styles_black_background.download_button_style
        )
        download_icon = QtGui.QPixmap("icons/cloud.png")
        self.download_button.setIcon(QtGui.QIcon(download_icon))
        self.download_button.setIconSize(QtCore.QSize(32, 32))
        self.search_field = QLineEdit()
        self.search_field.setPlaceholderText("URL: ")
        self.search_field.setStyleSheet(styles_black_background.search_field_style)
        font = self.search_field.font()
        font.setPointSize(12)
        self.search_field.setFont(font)
        self.quality_combobox = QComboBox()
        self.quality_combobox.addItems(self.video_quality_preferences)
        self.preference_combobox = QComboBox()
        self.quality_combobox.setStyleSheet(styles_black_background.combobox_style)
        self.preference_combobox.setStyleSheet(styles_black_background.combobox_style)
        self.preference_combobox.addItems(self.video_download_preferences)
        self.main_v_box = QVBoxLayout()
        self.top_placement()
        self.center_placement()
        self.bottom_placement()
        self.setLayout(self.main_v_box)

    def top_placement(self):
        search_layout = QHBoxLayout()
        search_layout.addWidget(self.search_field)
        search_layout.addWidget(self.add_button)
        search_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.main_v_box.addLayout(search_layout)

    def center_placement(self):
        label = QLabel("Type the url and add a video!")
        label.setStyleSheet(styles_black_background.label_style)
        font = label.font()
        font.setPointSize(12)
        label.setFont(font)
        label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.main_v_box.addWidget(label)

    def bottom_placement(self):
        combobox_h_box = QHBoxLayout()
        combobox_h_box.addWidget(self.quality_combobox)
        combobox_h_box.addWidget(self.preference_combobox)
        combobox_h_box.addWidget(self.delete_button)
        combobox_h_box.addWidget(self.download_button)
        buttons_h_box = QHBoxLayout()
        buttons_h_box.addWidget(self.feedback_button)
        buttons_h_box.addWidget(self.history_button)
        buttons_h_box.addWidget(self.settings_button)
        v_box = QVBoxLayout()
        v_box.addLayout(combobox_h_box)

        v_box.addLayout(buttons_h_box)
        v_box.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom)
        self.main_v_box.addLayout(v_box)


class Settings_UI(QWidget):
    def __init__(self, parent=None):
        super(Settings_UI, self).__init__(parent)
        self.init()

    def init(self):
        pass


class History_UI(QWidget):
    def __init__(self, parent=None):
        super(History_UI, self).__init__(parent)
        self.init()

    def init(self):
        pass


class Feedback_UI(QWidget):
    def __init__(self, parent=None):
        super(Feedback_UI, self).__init__(parent)
        self.init()

    def init(self):
        pass


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setStyleSheet("background-color: rgba(255, 255, 255, .1);")
        app = wx.App(False)
        self.state = 0
        self.width, self.height = wx.GetDisplaySize()
        self.setGeometry(
            round((self.width / 2) - 800), round((self.height / 2) - 300), 1200, 600
        )
        self.setWindowTitle("YouTube Video Downloader")
        self.startMainMenu()

    def startMainMenu(self):
        self.window = Window(self)
        self.setWindowTitle("YouTube Video Downloader")
        self.window.feedback_button.clicked.connect(self.startFeedbackMenu)
        self.window.history_button.clicked.connect(self.startHistoryMenu)
        self.window.settings_button.clicked.connect(self.startSettingsMenu)
        self.setCentralWidget(self.window)
        self.showMaximized()

    def startHistoryMenu(self):
        self.ui_menu = History_UI(self)
        self.setWindowTitle("History")
        self.setCentralWidget(self.ui_menu)
        self.showMaximized()

    def startFeedbackMenu(self):
        self.feedback_menu = Feedback_UI(self)
        self.setWindowTitle("Feedback")
        self.setCentralWidget(self.feedback_menu)
        self.showMaximized()

    def startSettingsMenu(self):
        self.ui_menu = Settings_UI(self)
        self.setWindowTitle("Settings")
        self.setCentralWidget(self.ui_menu)
        self.showMaximized()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
