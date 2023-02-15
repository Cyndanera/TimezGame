from . import WorldLoader
from . import Retention
from . import RetentionSpec

class RetentionLoader(WorldLoader.WorldLoader):
    
    def __init__(self):
        WorldLoader.WorldLoader.__init__(self)
        self.walkMusicFile = {'phase_7/audio/bgm/Retention Walking1.ogg', 'phase_7/audio/bgm/RetentionWalking2.ogg'}
        self.minibossMusicFile = {
            'phase_7/audio/bgm/Retention MiniBoss1.ogg',
            'phase_7/audio/bgm/Retention MiniBoss2.ogg',
            'phase_7/audio/bgm/Retention MiniBoss3.ogg',
            'phase_7/audio/bgm/Retention MiniBoss4.ogg',
            'phase_7/audio/bgm/Retention MiniBoss5.ogg',
            'phase_7/audio/bgm/Retention MiniBoss6.ogg'
        }
        self.basketbossMusicFile = {
            'phase_7/audio/bgm/Retention BasketBoss1.ogg',
            'phase_7/audio/bgm/Retention BasketBoss2.ogg',
            'phase_7/audio/bgm/Retention BasketBoss3.ogg',
            'phase_7/audio/bgm/Retention BasketBoss4.ogg'
        }
        self.scene = RetentionSpec.GlobalEntities

    def load(self):
        WorldLoader.WorldLoader.load(self)

    def unload(self):
        WorldLoader.WorldLoader.unload(self)
