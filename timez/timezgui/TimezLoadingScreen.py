from direct.gui.DirectGui import *
from panda3d.core import *
from timez.timezbase import TimezGlobals
from timez.timezbase import TZLocalizer
import random


class TimezLoadingScreen:
    def __init__(self):
        self._TimezLoadingScreen__expectedCount = 0
        self._TimezLoadingScreen__count = 0

    def destroy(self):
        pass

    def tick(self):
        self._TimezLoadingScreen__count = self._TimezLoadingScreen__count + 1
