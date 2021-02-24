"""
YourLuckApp - Main Code
Author: Ian Saft Date: 02/15/2021

Desktop application made with PySide2 to make sweepstakes between people.

Code responsible for creating and executing the main application.
"""

import sys
from PySide2 import QtCore
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget

from theme import theme

from components.titlebar import TitleBar


class UiMainWindow(object):
    def setup_ui(self, MainWindow):
        super().__init__()

        MainWindow.resize(theme.screenSettings.width, theme.screenSettings.height)

        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint) # Removing the standard title bar

        self.mainWidget = QWidget(MainWindow)
        self.mainWidget.setFixedSize(theme.screenSettings.width, theme.screenSettings.height)
        self.setStyleSheet(f"background-color: {theme.colors.white};")

        self.titlebar = TitleBar(self.mainWidget, MainWindow)
        self.titlebar.mouseMoveEvent = self.mouse_move_event
        
        
class App(QMainWindow, UiMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui(self)
        self.dragPos = QtCore.QPoint()
        self.mousePressEvent = self.mouse_press_event


    def mouse_press_event(self, event):                                 
        self.dragPos = event.globalPos()

        
    def mouse_move_event(self, event):                                 
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()


def run_app():
    app = QApplication.instance()

    if app is None:
        app = QApplication(sys.argv)

    mainWindow = App()
    mainWindow.show()
    app.exec_()


if __name__ == '__main__':
    print('[SUCCESS]: Running application.\n')
    run_app()
    sys.exit(0)
