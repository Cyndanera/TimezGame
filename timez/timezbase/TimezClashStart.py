#---------------------------------------------------------------------------
#  Project:  Timez Clash
#  File:     TimezClashStart.py

#  Copyright 2023-2024 Cyndanera.  All rights reserved.
#  Author: Garrett Stewart
#  Date: 2/13/2023

#  These coded instructions, statements, and computer programs contain
#  proprietary information of Cyndanera LLC.
#  and are protected by Federal copyright law.  They may
#  not be disclosed to third parties or copied or duplicated in any form,
#  in whole or in part, without the prior written consent of Cyndanera.
#---------------------------------------------------------------------------
from direct.showbase.ShowBase import ShowBase
from direct.showbase.MessengerGlobal import *
from .TimezBaseGlobal import *
from direct.gui.DirectGui import *
from . import TimezLoader
from . import TZLocalizer
from . import TimezBase
from . import TimezGlobals
from timez.selectacharacter import SelectACharacter
from direct.gui import DirectGuiGlobals
from panda3d.core import *
import random
import sys
import os
import time
import builtins

class Game(ShowBase):
    name = 'timezclash'
    process = 'game'

    def __init__(self):
        loadPrcFile('config/dev.prc')

        # Initialize the ShowBase class from which we inherit, which will
        # create a window and set up everything we need for rendering into it.
        ShowBase.__init__(self)

        pollingDelay = 0.5
        print('TimezClashStart: Polling for game2 to finish...')
        time.sleep(pollingDelay)
        print('TimezClashStart: Game2 is finished.')
        print('TimezClashStart: Starting the game.')

        print('TimezClashStart: setting default font')

        # init
        TimezBase.TimezBase()

        if base.musicManagerIsValid:
            music = base.musicManager.getSound('phase_3/audio/bgm/tc_theme.ogg')
            if music:
                music.setLoop(1)
                music.setVolume(0.90000000000000002)
                music.play()
                music.stop()
                del music

        selection = SelectACharacter.SelectACharacter()
        selection.load()
        selection.enter()

game = Game()
game.run()