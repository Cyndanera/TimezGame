from panda3d.core import *

from timez.timezbase import TimezGlobals
from direct.actor.Actor import Actor
from direct.task import Task
from direct.gui.DirectGui import *
from timez.timezbase import TZLocalizer
from .SelectACharacterGlobals import *
from direct.interval.IntervalGlobal import *
from direct.directnotify import DirectNotifyGlobal
from timez.world import Retention
import random


class SelectACharacter():
    notify = DirectNotifyGlobal.directNotify.newCategory('SelectACharacter')

    def __init__(self):
        self.phase = 3
        self.music = None
        self.character = None
        self.musicVolume = 1

    def getCharacter(self):
        return self.character

    def enter(self):
        self.notify.debug('Selecting a Character.')
        base.playMusic(self.music, looping=1, volume=self.musicVolume)

        self.unload()

        ret = Retention.Retention()
        ret.load()
        ret.enter()

    def exit(self):
        self.music.stop()

    def load(self):
        self.music = base.loader.loadMusic('phase_3.5/audio/bgm/CreatureCollectingBkgd.ogg')

    def unload(self):
        self.exit()
        del self.music

