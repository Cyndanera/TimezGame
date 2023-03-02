#---------------------------------------------------------------------------
#  Project:  Timez Clash
#  File:     WorldLoader.py

#  Copyright 2023-2024 Cyndanera.  All rights reserved.
#  Author: Garrett Stewart
#  Date: 2/18/2023

#  These coded instructions, statements, and computer programs contain
#  proprietary information of Cyndanera LLC.
#  and are protected by Federal copyright law.  They may
#  not be disclosed to third parties or copied or duplicated in any form,
#  in whole or in part, without the prior written consent of Cyndanera.
#---------------------------------------------------------------------------

from panda3d.core import *
from timez.timezbase import TimezGlobals
import random

class WorldLoader():
    
    def __init__(self):
        self.music1 = None
        self.music2 = None
        self.music3 = None
        self.music4 = None
        self.music5 = None
        self.music6 = None
        self.music7 = None
        self.music8 = None
        self.music9 = None
        self.music10 = None
        self.music11 = None
        self.music12 = None
        self.music13 = None
        self.music14 = None
        self.music15 = None

    def load(self):
        # music
        if TimezGlobals.currentWorld == TimezGlobals.nameRetention:
            self.music1 = base.loader.loadMusic(self.walking1)
            self.music1.setLoop(True)
            self.music2 = base.loader.loadMusic(self.walking2)
            self.music2.setLoop(True)

            if TimezGlobals.basketBossTest:
                self.music3 = base.loader.loadMusic(self.basket1)
                self.music3.setLoop(True)
                self.music4 = base.loader.loadMusic(self.basket2)
                self.music4.setLoop(True)
                self.music5 = base.loader.loadMusic(self.basket3)
                self.music5.setLoop(True)
                self.music6 = base.loader.loadMusic(self.basket4)
                self.music6.setLoop(True)

            self.music3 = base.loader.loadMusic(self.boss1)
            self.music3.setLoop(True)
            self.music4 = base.loader.loadMusic(self.boss2)
            self.music4.setLoop(True)
            self.music5 = base.loader.loadMusic(self.boss3)
            self.music5.setLoop(True)
            self.music6 = base.loader.loadMusic(self.boss4)
            self.music6.setLoop(True)
            self.music7 = base.loader.loadMusic(self.boss5)
            self.music7.setLoop(True)
            self.music8 = base.loader.loadMusic(self.boss6)
            self.music8.setLoop(True)

            # sfx
            self.waterSfx = base.loader.loadSfx(self.water)
            self.waterSfx.setLoop(True)

    def unload(self):
        del self.music1
        del self.music2
        del self.music3
        del self.music4
        del self.music5
        del self.music6
        del self.music7
        del self.music8
        del self.music9
        del self.music10
        del self.music11
        del self.music12
        del self.music13
        del self.music14
        del self.music15

        if TimezGlobals.currentWorld == TimezGlobals.nameRetention:
            del self.watersfx

    def enter(self):
        if TimezGlobals.musicMode == TimezGlobals.MUSIC_MODE_WALK:
            musicTrack = random.randint(1, 2)
            if musicTrack == 1:
                self.music1.play()
            elif musicTrack == 2:
                self.music2.play()

        if TimezGlobals.musicMode == TimezGlobals.MUSIC_MODE_BASKET:
            musicTrack = random.randint(1, 4)
            if musicTrack == 1:
                self.music3.play()
            elif musicTrack == 2:
                self.music4.play()
            elif musicTrack == 3:
                self.music5.play()
            elif musicTrack == 4:
                self.music6.play()

        if TimezGlobals.musicMode == TimezGlobals.MUSIC_MODE_BOSS:
            musicTrack = random.randint(1, 6)
            if musicTrack == 1:
                self.music3.play()
            elif musicTrack == 2:
                self.music4.play()
            elif musicTrack == 3:
                self.music5.play()
            elif musicTrack == 4:
                self.music6.play()
            elif musicTrack == 5:
                self.music7.play()
            elif musicTrack == 6:
                self.music8.play()

        if TimezGlobals.currentWorld == TimezGlobals.nameRetention:
            self.waterSfx.play()
