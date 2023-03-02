#---------------------------------------------------------------------------
#  Project:  Timez Clash
#  File:     Retention.py

#  Copyright 2023-2024 Cyndanera.  All rights reserved.
#  Author: Garrett Stewart
#  Date: 2/18/2023

#  These coded instructions, statements, and computer programs contain
#  proprietary information of Cyndanera LLC.
#  and are protected by Federal copyright law.  They may
#  not be disclosed to third parties or copied or duplicated in any form,
#  in whole or in part, without the prior written consent of Cyndanera.
#---------------------------------------------------------------------------

from timez.timezbase import TimezGlobals
from . import RetentionLoader

class Retention(RetentionLoader.RetentionLoader):
    
    def __init__(self):
        self.modelGui = None
        self.modelGuiPose = None
        RetentionLoader.RetentionLoader.__init__(self)

    def load(self):
        print('Loading Retention Resources.')
        RetentionLoader.RetentionLoader.load(self)
        self.modelGui = loader.loadModel('phase_3/models/gui/GUI-Box-Bkgd1')
        self.modelGuiPose = loader.loadModel('phase_7/models/gui/RoboBot_pose')
        self.modelGui.setScale(5, 5, 1)
        self.modelGuiPose.setScale(3, 1, 0.8)

    def enter(self):
        TimezGlobals.musicMode = TimezGlobals.MUSIC_MODE_BOSS
        print('Entering Retention...')
        self.modelGuiPose.setPos(0, -0.2, 0.3)
        self.modelGui.reparentTo(render)
        self.modelGuiPose.reparentTo(render)
        base.camera.reparentTo(self.modelGui)
        base.camera.setPos(0, 0, -20)
        RetentionLoader.RetentionLoader.enter(self)

    def unload(self):
        RetentionLoader.RetentionLoader.unload(self)