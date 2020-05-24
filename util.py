from os import system, name

#--------------------------------------------------------------------
# DATA
#--------------------------------------------------------------------
locations = {\
    'empty' : {'name': 'an empty room', 'east': 'bedroom', 'north': 'temple',
        'deftext' : '\tThe stone floors and walls are cold and damp.\n' 
                    '\tTo the north is a temple, and to the east is a bedroom.',
        'contents': [],
        'win'     : ['candle','statue','bench']},
    'temple' : {'name': 'a small temple', 'east': 'torture', 'south': 'empty', 
        'deftext': '\tThis seems to be a place of worship and deep\n' 
                   '\tcontemplation. To the east is a gruesome looking\n' 
                   '\troom, and to the south is an empty room.', 
        'contents': ['bench', 'candle', 'bench', 'statue']},
    'torture': {'name': 'a torture chamber', 'west': 'temple', 'south': 'bedroom',
        'deftext' : '\tThere is a rack and an iron maiden against the wall \n'
                    '\tand some dark stains on the floor. To the south is \n'
                    '\ta bedroom, and the temple is to the west.',
        'contents': []},
    'bedroom' : {'name': 'a bedroom', 'north': 'torture', 'west': 'empty',
        'deftext' : '\tThis is clearly a bedroom, but no one has slept here \n'
                    '\tin a long time. To the west is the room where you awoke, \n'
                    '\tand to the north is the torture chamber.',
        'contents': ['sheets', 'bed']}}
        
class stats:
    health   = 100
    shield   =   0
    tactical =   0
    ultimate =   0
    ammo0    =   0
    ammo1    =   0
    ring     =  10

class weapons:
    melee   = ["Melee",    8,  0,  0]
    r301    = ["R-301",   15, 15, 15]
    mastiff = ["mastiff", 18, 12,  8]  

class attatchments:
    heavyMag   = ["Extended Heavy Magazine", 3]
    lightMag   = ["Extended Light Magazine", 3]
    stabalizer = ["Barrel Stabalizer",       2]
    stock      = ["Standard Stock",          2]
    bolt       = ["Shotgun Bolt",            2]
    optics     = ["HCOG Scope",              1]

class consumables:
    shieldCell    = ["Shield Cell",     25]
    shieldBattery = ["Shield Battery", 100]
    syringe       = ["Syringe",         25]
    medKit        = ["Med Kit",        100]

directions = ['north', 'south', 'east', 'west']

#initialization
current_location = locations['empty']

#--------------------------------------------------------------------
# FUNCTIONS
#--------------------------------------------------------------------
    # clear screen
def clear():
    if name == 'nt': 
        _ = system('cls')
        
        
    # user interface    
def displayUI():
    print('--------------------------------------------------------------------------------')
    print('| Health: {} | Shield {} | Tactical: {} | Ultimate: {} | Ring: {} '\
          '|'.format(stats.health, stats.shield, stats.tactical, stats.ultimate, stats.ring))
    print(ui['bar'])

    print(ui['health'], stats['health'],
          ui['shield'], stats['shield'],
          ui['tactical'], stats['tactical'],
          ui['ultimate'], stats['ultimate'],
          ui['ring'], stats['ring'],
          ui['weapons0'], weapon0['uiName'], 
          stats['ammo0'], ui['weapons1'],
          weapon0['uiName'], stats['ammo1'], 
          ui['weapons1'], ui['location'])
          
    # display location
def displayLocation():
    print('\tYou are in {}.'.format(current_location['name']))
    print(current_location['deftext'])







