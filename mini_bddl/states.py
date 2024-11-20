from mini_behavior.states import *

ALL_STATES = [
    'atsamelocation',
    'deform',
    'detach',
    'hidden',
    'infovofrobot',
    'inhandofrobot',
    'inreachofrobot',
    'insameroomasrobot',
    'inside',
    'nextto',
    'noise',
    'onfloor',
    'onTop',
    'popup',
    'reattach',
    'takeout',
    'toggleable',
    'under',
    ''
    # 'touching', TODO: uncomment once implemented
]

# Touching
# ObjectsInFOVOfRobot,

DEFAULT_STATES = [
    'atsamelocation',
    'infovofrobot',
    'inhandofrobot',
    'inreachofrobot',
    'insameroomasrobot',
    'inside',
    'nextto',
    'onfloor',
    'onTop',
    'under'
]

# ATTENTION: Must change init function in BehaviorGrid class in mini_behavior/grid.py to accomodate for new sizes 
# in ABILITIES and FURNATURE_STATES
ABILITIES = [
    'cookable',
    'freezable',
    'openable',
    'playable',
    'sliceable',
    'soakable',
    'stainable',
    'toggleable',
]

FURNATURE_STATES = [
    'openable',
    'playable',
    'stainable',
    'toggleable',
]

# state (str) to state (function) mapping
STATE_FUNC_MAPPING = {
    'atsamelocation': AtSameLocation,
    'cleaningTool': CleaningTool,
    'coldSource': HeatSourceOrSink,
    'cookable': Cooked,
    'dustyable': Dusty,
    'freezable': Frozen,
    'heatSource': HeatSourceOrSink,
    'infovofrobot': InFOVOfRobot,
    'inhandofrobot': InHandOfRobot,
    'inreachofrobot': InReachOfRobot,
    'insameroomasrobot': InSameRoomAsRobot,
    'inside': Inside,
    'nextto': NextTo,
    'onfloor': OnFloor,
    'onTop': OnTop,
    'openable': Opened,
    'playable': Played,
    'sliceable': Sliced,
    'slicer': Slicer,
    'soakable': Soaked,
    'stainable': Stained,
    'toggleable': ToggledOn,
    'under': Under,
    'waterSource': WaterSource
    # 'touching', TODO: uncomment once implemented
}


########################################################################################################################

# FROM BDDL

# TEXTURE_CHANGE_PRIORITY = {
#     Frozen: 4,
#     Burnt: seed 10_3,
#     Cooked: seed 0_2,
#     Soaked: seed 0_2,
#     ToggledOn: 0,
# }

