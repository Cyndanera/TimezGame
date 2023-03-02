from . import TimezGlobals
from direct.directnotify import DirectNotifyGlobal
from . import TimezLoader
from direct.gui import DirectGuiGlobals
from direct.gui.DirectGui import *
from panda3d.core import *
import sys
import os
import math
from timez.timezbase import TZLocalizer


class TimezBase():
    notify = DirectNotifyGlobal.directNotify.newCategory('TimezBase')

    def __init__(self):
        pass

    def playMusic(self, music, looping=0, interrupt=1, volume=None, time=0.0):
        pass
