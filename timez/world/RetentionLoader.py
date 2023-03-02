#---------------------------------------------------------------------------
#  Project:  Timez Clash
#  File:     RetentionLoader.py

#  Copyright 2023-2024 Cyndanera.  All rights reserved.
#  Author: Garrett Stewart
#  Date: 2/18/2023

#  These coded instructions, statements, and computer programs contain
#  proprietary information of Cyndanera LLC.
#  and are protected by Federal copyright law.  They may
#  not be disclosed to third parties or copied or duplicated in any form,
#  in whole or in part, without the prior written consent of Cyndanera.
#---------------------------------------------------------------------------

from . import WorldLoader
from . import RetentionSpec

class RetentionLoader(WorldLoader.WorldLoader):
    
    def __init__(self):
        WorldLoader.WorldLoader.__init__(self)
        
        self.spec = RetentionSpec.RetEntities
        self.ambiance = 'phase_7/audio/sfx/.ogg'
        self.basketExplode = 'phase_7/audio/sfx/.ogg'
        self.basketHit = 'phase_7/audio/sfx/Retention Boss Hit.ogg'
        self.basketIdle = 'phase_7/audio/sfx/Retention Boss Idle.ogg'
        self.basketMenace = 'phase_7/audio/sfx/.ogg'
        self.basketWakeUp = 'phase_7/audio/sfx/.ogg'
        self.basketWrong = 'phase_7/audio/sfx/Retention Boss Wrong.ogg'
        self.canisterOpen = 'phase_7/audio/sfx/Canister Open.ogg'
        self.crateDebris = 'phase_7/audio/sfx/Retention Crate Explode3'
        self.crateExplode = 'phase_7/audio/sfx/Retention Crate Explode Solo'
        self.doorExplode = 'phase_7/audio/sfx/.ogg'
        self.doorOpen = 'phase_7/audio/sfx/.ogg'
        self.doorSlide = 'phase_7/audio/sfx/.ogg'
        self.elevatorEnd = 'phase_7/audio/sfx/.ogg'
        self.elevatorDown = 'phase_7/audio/sfx/Retention Island Elevator Down.ogg'
        self.elevatorUp = 'phase_7/audio/sfx/Retention Island Elevator Up.ogg'
        self.flyingJawExplode = 'phase_7/audio/sfx/.ogg'
        self.flyingJawIdle = 'phase_7/audio/sfx/Flying Jaw Idle.ogg'
        self.flyingJawMenace = 'phase_7/audio/sfx/Flying Jaw Menace.ogg'
        self.helijawpterBite  = 'phase_7/audio/sfx/.ogg'
        self.helijawpterPortal = 'phase_7/audio/sfx/.ogg'
        self.laserFire = 'phase_7/audio/sfx/.ogg'
        self.laserHit = 'phase_7/audio/sfx/.ogg'
        self.piston = 'phase_7/audio/sfx/.ogg'
        self.projectileExplode = 'phase_7/audio/sfx/.ogg'
        self.robotHit = 'phase_7/audio/sfx/Retention Robot Hit.ogg'
        self.robotShatter = 'phase_7/audio/sfx/Retention Robot Shatter.ogg'
        self.robotStep = 'phase_7/audio/sfx/Trooper Footstep Slow.ogg'
        self.robotVoice = {
                           'phase_7/audio/sfx/Trooper Voice 1.ogg',
                           'phase_7/audio/sfx/Trooper Voice 2.ogg',
                           'phase_7/audio/sfx/b-alert.ogg'
                           }
        self.secretDoor = 'phase_7/audio/sfx/.ogg'
        self.secretDoorEnd = 'phase_7/audio/sfx/Retention Door Explode.ogg'
        self.shockWave = 'phase_7/audio/sfx/.ogg'
        self.switchPowerUp = 'phase_7/audio/sfx/Retention Elevator Switch Powerup.ogg'
        self.switchSteppedOn = 'phase_7/audio/sfx/Retention Elevator Switch Stepped On.ogg'
        self.water = 'phase_7/audio/sfx/Retention Water.ogg'
        self.xPickup = 'phase_3.5/audio/sfx/PreTest Pickup.ogg'
        self.walking1 = 'phase_7/audio/bgm/Retention Walking1.ogg'
        self.walking2 = 'phase_7/audio/bgm/RetentionWalking2.ogg'
        self.boss1 = 'phase_7/audio/bgm/Retention MiniBoss1.ogg'
        self.boss2 = 'phase_7/audio/bgm/Retention MiniBoss2.ogg'
        self.boss3 = 'phase_7/audio/bgm/Retention MiniBoss3.ogg'
        self.boss4 = 'phase_7/audio/bgm/Retention MiniBoss4.ogg'
        self.boss5 = 'phase_7/audio/bgm/Retention MiniBoss5.ogg'
        self.boss6 = 'phase_7/audio/bgm/Retention MiniBoss6.ogg'
        self.basket1 = 'phase_7/audio/bgm/Retention BasketBoss1.ogg'
        self.basket2 = 'phase_7/audio/bgm/Retention BasketBoss2.ogg'
        self.basket3 = 'phase_7/audio/bgm/Retention BasketBoss3.ogg'
        self.basket4 = 'phase_7/audio/bgm/Retention BasketBoss4.ogg'
        self.finale = 'phase_7/audio/bgm/.ogg'
        self.finalePrep = 'phase_7/audio/bgm/.ogg'
        self.pretest1 = 'phase_7/audio/bgm/.ogg'
        self.pretest2 = 'phase_7/audio/bgm/.ogg'

        self.waterSfx = None

    def load(self):
        WorldLoader.WorldLoader.load(self)

    def enter(self):
        WorldLoader.WorldLoader.enter(self)

    def unload(self):
        WorldLoader.WorldLoader.unload(self)
