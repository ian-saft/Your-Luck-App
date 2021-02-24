"""
YourLuckApp - Theme Code
Author: Ian Saft Date: 02/15/2021

Code responsible for reading and organizing the application theme settings
"""

import json
import sys

def json_read(jsonFileAdress = None):

    try:
        jsonFile = open(jsonFileAdress, 'r', encoding='utf8')
        print("[SUCCESS]: Theme settings loaded.")
        return json.load(jsonFile)

    except Exception as error:
        print(f'\n[ERROR]: Error loading {jsonFileAdress} ({error})\n')
        sys.exit(0)


themeConfig = json_read('.//theme-config.json')


class Theme():
    def __init__(self):
        super().__init__()

        self.screenSettings = ScreenSettings()
        self.colors         = Colors()
        self.fontFamilys    = FontFamilys()
        self.fontSizes      = FontSizes()
        self.closeIcon      = CloseIcon()
        self.minimizeIcon   = MinimizeIcon()
        self.maximizeIcon   = MaximizeIcon()


class ScreenSettings():
    def __init__(self):
        super().__init__()

        self.title  = themeConfig['screen-settings']['title']
        self.width  = themeConfig['screen-settings']['width']
        self.height = themeConfig['screen-settings']['height']

        self.titlebarHeight = themeConfig['screen-settings']['titlebar-height']

        self.appIcon = themeConfig['images']['app-logo-icon']
        self.bgImg   = themeConfig['images']['background-image']


class Colors():
    def __init__(self):
        super().__init__()

        self.darkGreen   = themeConfig['colors']['dark-green']
        self.nightGreen  = themeConfig['colors']['night-green']
        self.mainGreen   = themeConfig['colors']['main-green']
        self.lightGreen  = themeConfig['colors']['light-green']
        self.yellowGreen = themeConfig['colors']['yellow-green']
        self.white       = themeConfig['colors']['white']


class FontFamilys():
    def __init__(self):
        super().__init__()

        self.textFont       = themeConfig['font-family']['text-font']
        self.tittleFont     = themeConfig['font-family']['tittle-font']
        self.buttonFont     = themeConfig['font-family']['button-font']
        self.buttonFontBold = themeConfig['font-family']['button-font-bold']


class FontSizes():
    def __init__(self):
        super().__init__()

        self.small  = themeConfig['font-size']['small']
        self.medium = themeConfig['font-size']['medium']
        self.large  = themeConfig['font-size']['large']


class CloseIcon():
    def __init__(self):
        super().__init__()

        self.default = themeConfig['images']['close-icon']['default']
        self.hover   = themeConfig['images']['close-icon']['hover']
        self.pressed = themeConfig['images']['close-icon']['pressed']


class MinimizeIcon():
    def __init__(self):
        super().__init__()

        self.default = themeConfig['images']['minimize-icon']['default']
        self.hover   = themeConfig['images']['minimize-icon']['hover']
        self.pressed = themeConfig['images']['minimize-icon']['pressed']


class MaximizeIcon():
    def __init__(self):
        super().__init__()

        self.default = themeConfig['images']['maximize-icon']['default']
        self.hover   = themeConfig['images']['maximize-icon']['hover']
        self.pressed = themeConfig['images']['maximize-icon']['pressed']


theme = Theme()     # Final theme object
