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
        
gameStats =  {\
    'stats': {'shield': 0, 'health': 100, 'tactical': 0, 
              'ultimate': 0, 'ammo0': 0, 'ammo1': 0, 'ring' : 10}}

userInterface = {\
    'design': {'bar'      : '--------------------'\
                            '--------------------'\
                            '--------------------'\
                            '--------------------',
               'shield'   : '| Shield:',
               'health'   : '| Health:',
               'tactical' : '| Tactical:', 
               'ultimate' : '| Ultimate:',
               'ring'     : '| Ring:',              
               'weapons0' : '|\n\nWeapons:',
               'weapons1' : ')',
               'location' : '\n\nLocation:'}}
               
weapons = {\
    'melee'  : {'uiName': '\n\tMelee:      Ammo(','name': 'Melee', 'closeRange':  8, 'midRange': 0,  'farRange':  0},
    'mastiff': {'uiName': '\n\tMastiff:    Ammo(','name': 'Mastiff', 'closeRange': 20, 'midRange': 15, 'farRange':  9},
    'r-301':   {'uiName': '\n\tR-301:      Ammo(','name': 'R-301', 'closeRange': 16, 'midRange': 18, 'farRange': 16}}
    
attatchments = {\
    'heavyMag':    {'uiName': '\n\tExt. Heavy Mag    :  +', 'bonus': 3, 'name': 'Extended Heavy Mag'},
    'lightMag':    {'uiName': '\n\tExt. Light Mag    :  +', 'bonus': 3, 'name': 'Extended Light Mag'},
    'stabalizer':  {'uiName': '\n\tBarrel Stabalizer :  +', 'bonus': 2, 'name': 'Barrel Stabalizer'},
    'stock':       {'uiName': '\n\tStandard Stock    :  +', 'bonus': 2, 'name': 'Standard Stock'},
    'shotgunBolt': {'uiName': '\n\tShotgun Bolt      :  +', 'bonus': 2, 'name': 'Shotgun Bolt'},
    'optics':      {'uiName': '\n\tHCOG Scope        :  +', 'bonus': 1, 'name': '1X HCOG Sights'}}
    
consumables = {\
    'shield'  : {'Shield Cell':  25, 'Shield Battery': 100},
    'health'  : {'Syringe': 25, 'Med Kit': 100},
    'ultaccel': {'Ultimate Accelerant': 25}}

directions = ['north', 'south', 'east', 'west']

#initialization
current_location = locations['empty']
weapon0 = weapons['melee'] 
weapon1 = weapons['melee']
stats = gameStats['stats']
ui = userInterface['design']

#--------------------------------------------------------------------
# FUNCTIONS
#--------------------------------------------------------------------
    # clear screen
def clear():
    if name == 'nt': 
        _ = system('cls')
        
        
    # user interface    
def displayUI():
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







