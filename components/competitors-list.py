"""
YourLuckApp - Component Code: Competitors List
Author: Ian Saft Date: 02/15/2021

Code responsible for creating and styling the application competitors list and all its internal components
"""

from PySide2.QtGui import QFont, QIcon
from PySide2.QtWidgets import QFrame, QLabel, QPushButton, QListView, QListWidget

from theme import theme

class CompetitorsList(QFrame):
    def __init__(self, master=None):
        super().__init__(master)

# UNDER DEVELOPMENT...
