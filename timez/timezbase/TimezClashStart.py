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

class Game(ShowBase):
    def __init__(self):
        # Initialize the ShowBase class from which we inherit, which will
        # create a window and set up everything we need for rendering into it.
        ShowBase.__init__(self)
        self.setBackgroundColor((0, 0, 0, 0))

game = Game()
game.run()
