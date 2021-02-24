"""
YourLuckApp - Component Code: Titlebar
Author: Ian Saft Date: 02/15/2021

Code responsible for creating and styling the application title bar and all its internal components
"""

from PySide2.QtGui import QIcon, QFont
from PySide2.QtWidgets import QFrame, QLabel, QPushButton

import sys

from theme import theme

class TitleBar(QFrame):
    def __init__(self, master=None, mainWindow=None):
        super().__init__(master)

        self.mainWindowIsHide = False

        self.setGeometry(0, 0, theme.screenSettings.width, theme.screenSettings.titlebarHeight)
        self.setStyleSheet(f"background-color: {theme.colors.darkGreen};")

        self.create_app_icon()
        self.create_app_title()
        self.create_close_button()
        self.create_resize_button(mainWindow)


    def create_app_icon(self):

        tittlebarIcon = QIcon(theme.screenSettings.appIcon)
        pixmapTittlebarIcon = tittlebarIcon.pixmap(theme.screenSettings.titlebarHeight, theme.screenSettings.titlebarHeight)

        self.labelTittlebarIcon = QLabel('Icon', self)
        self.labelTittlebarIcon.setPixmap(pixmapTittlebarIcon)
        self.labelTittlebarIcon.setGeometry(0, 0, theme.screenSettings.titlebarHeight, theme.screenSettings.titlebarHeight)

    
    def create_app_title(self):

        font = QFont(theme.fontFamilys.textFont)
        font.setPointSize(theme.fontSizes.small)

        self.labelTitle = QLabel(theme.screenSettings.title, self)
        self.labelTitle.setFont(font)
        self.labelTitle.move(25, 2)

        self.labelTitle.setStyleSheet(f"color: {theme.colors.white};")


    def create_close_button(self):

        self.cssCloseButton = self.set_css_top_button(
            imgDefault=theme.closeIcon.default, 
            imgHover=theme.closeIcon.hover, 
            imgPressed=theme.closeIcon.pressed
        )

        posx = theme.screenSettings.width - theme.screenSettings.titlebarHeight
        
        self.closeButton = QPushButton(self)
        self.closeButton.setGeometry(posx, 0, theme.screenSettings.titlebarHeight, theme.screenSettings.titlebarHeight)

        self.closeButton.setStyleSheet(self.cssCloseButton)

        def close_app():
            print('[WINDOW STATE]: CLOSED\n')
            print('[WARNING] Finished application.\n')
            sys.exit(0)

        self.closeButton.clicked.connect(close_app)


    def create_resize_button(self, window):

        self.cssMinimizeButton = self.set_css_top_button(
            imgDefault=theme.minimizeIcon.default, 
            imgHover=theme.minimizeIcon.hover, 
            imgPressed=theme.minimizeIcon.pressed
        )
        self.cssMaximizeButton = self.set_css_top_button(
            imgDefault=theme.maximizeIcon.default,
            imgHover=theme.maximizeIcon.hover,
            imgPressed=theme.maximizeIcon.pressed
        )

        posx = theme.screenSettings.width - (2 * theme.screenSettings.titlebarHeight)
        
        self.resizeButton = QPushButton(self)
        self.resizeButton.setGeometry(posx, 0, theme.screenSettings.titlebarHeight, theme.screenSettings.titlebarHeight)

        self.resizeButton.setStyleSheet(self.cssMinimizeButton)
        
        def resize_window():
            if not self.mainWindowIsHide:
                window.resize(theme.screenSettings.width, theme.screenSettings.titlebarHeight)

                print('[WINDOW STATE]: HIDDEN')

                self.resizeButton.setStyleSheet(self.cssMaximizeButton)
                self.mainWindowIsHide = True

            else:
                window.resize(theme.screenSettings.width, theme.screenSettings.height)

                print('[WINDOW STATE]: VISIBLE')

                self.resizeButton.setStyleSheet(self.cssMinimizeButton)
                self.mainWindowIsHide = False


        self.resizeButton.clicked.connect(resize_window)

        
    def set_css_top_button(self, imgDefault='', imgHover='', imgPressed=''):
        
        colorDefeault = theme.colors.darkGreen
        colorHover = theme.colors.lightGreen
        colorPressed = theme.colors.yellowGreen

        cssButtonStyle = (
            "QPushButton"
            "{"
                "background-color: " + colorDefeault + ";"
                "background-image: url(" + imgDefault + ");"
                "background-position: center;"
                "border: 0px"
            "}"
            "QPushButton:hover"
            "{"
                "background-color: " + colorHover + ";"
                "background-image: url(" + imgHover + ");"
                "background-position: center;"
            "}"
            "QPushButton:pressed"
            "{"
                "background-color: " + colorPressed + ";"
                "background-image: url(" + imgPressed + ");"
                "background-position: center;"
            "}"
        )
        return cssButtonStyle

