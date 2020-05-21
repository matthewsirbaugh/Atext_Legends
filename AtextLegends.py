#--------------------------------------------------------------------
# RESOURCES
#--------------------------------------------------------------------
from os import system, name
system('mode con: cols=90 lines=50') # screen size

#--------------------------------------------------------------------
# DATA
#--------------------------------------------------------------------
#******************************#
    # location data
locations = {\
    'empty' : {'name': 'an empty room', 'east': 'bedroom', 'north': 'temple',
        'deftext' : '\tThe stone floors and walls are cold and damp.\n' 
                   '\tTo the north is a temple, and to the east is a bedroom.',
        'contents': [],
        'win': ['candle','statue','bench']},
    'temple' : {'name': 'a small temple', 'east': 'torture', 'south': 'empty', 
        'deftext': '\tThis seems to be a place of worship and deep contemplation. \n' 
                   '\tTo the east is a gruesome looking room, and the south is an empty room.', 
        'contents': ['bench', 'candle', 'bench', 'statue']},
    'torture': {'name': 'a torture chamber', 'west': 'temple', 'south': 'bedroom',
        'deftext': '\tThere is a rack and an iron maiden against the wall \n'
                   '\tand some dark stains on the floor. To the south is \n'
                   '\ta bedroom, and the temple is to the west.',
        'contents': []},
    'bedroom': {'name': 'a bedroom', 'north': 'torture', 'west': 'empty',
        'deftext': '\tThis is clearly a bedroom, but no one has slept here \n'
                   '\tin a long time. To the west is the room where you awoke, \n'
                   '\tand to the north is the torture chamber.',
        'contents': ['sheets', 'bed']}}
        
#******************************#
    # stats
gameStats =  {\
    'stats': {'shield': 0, 'health': 100, 'tactical': 0, 
              'ultimate': 0, 'ammo0': 0, 'ammo1': 0, 'ring' : 10}}

#******************************#
    # user interface
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

#******************************#                
    # weapons
weapons = {\
    'melee'  : {'uiName': '\n\tMelee:      Ammo(','name': 'Melee', 'closeRange':  8, 'midRange': 0,  'farRange':  0},
    'mastiff': {'uiName': '\n\tMastiff:    Ammo(','name': 'Mastiff', 'closeRange': 20, 'midRange': 15, 'farRange':  9},
    'r-301':   {'uiName': '\n\tR-301:      Ammo(','name': 'R-301', 'closeRange': 16, 'midRange': 18, 'farRange': 16}}

#******************************#    
    # attatchments
attatchments = {\
    'heavyMag':    {'uiName': '\n\tExt. Heavy Mag    :  +', 'bonus': 3, 'name': 'Extended Heavy Mag'},
    'lightMag':    {'uiName': '\n\tExt. Light Mag    :  +', 'bonus': 3, 'name': 'Extended Light Mag'},
    'stabalizer':  {'uiName': '\n\tBarrel Stabalizer :  +', 'bonus': 2, 'name': 'Barrel Stabalizer'},
    'stock':       {'uiName': '\n\tStandard Stock    :  +', 'bonus': 2, 'name': 'Standard Stock'},
    'shotgunBolt': {'uiName': '\n\tShotgun Bolt      :  +', 'bonus': 2, 'name': 'Shotgun Bolt'},
    'optics':      {'uiName': '\n\tHCOG Scope        :  +', 'bonus': 1, 'name': '1X HCOG Sights'}}

#******************************#
    # consumables
consumables = {\
    'shield'  : {'Shield Cell':  25, 'Shield Battery': 100},
    'health'  : {'Syringe': 25, 'Med Kit': 100},
    'ultaccel': {'Ultimate Accelerant': 25}}

    # directions
#******************************#
directions = ['north', 'south', 'east', 'west'] 

    # initialize location
#******************************#
current_location = locations['empty'] 

    # initialize weapons
#******************************#
weapon0 = weapons['melee'] 
weapon1 = weapons['melee']

    # ui and game stats
#******************************#
stats = gameStats['stats']
ui = userInterface['design']

    # game variables
#******************************#
inventory = [] 
quitGame = False 
win = False 

#--------------------------------------------------------------------
# FUNCTIONS
#--------------------------------------------------------------------

#******************************#
    # clear screen
def clear():
    if name == 'nt': 
        _ = system('cls')
        
#******************************#        
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
          
#******************************#
    # display location
def displayLocation():
    print('\tYou are in {}.'.format(current_location['name']))
    print(current_location['deftext'])

#--------------------------------------------------------------------           
# GAME LOGIC
#--------------------------------------------------------------------
clear()
#******************************#
    # character select
#while not quitGame:
#    if quitGame == True:
#        break
#

#******************************#
    # main game loop
while not quitGame:
    if quitGame == True:
        break

#******************************#
      # display UI
    displayUI()

#******************************#
      # display current location
    displayLocation()

#******************************#
      # display movable objects
    if current_location['contents']:
        print('\tIn the room are: {}'.format(', '.join(current_location['contents'])))

#******************************#
      # get input
    print(ui['bar'])
    command = input('\tNext Action: ').strip()

#******************************#
      # movement
    if command in directions:
        if command in current_location:
            current_location = locations[current_location[command]]
        else:
              # bad movement
            print("You can't go that way.")

#******************************#
      # quit game
    elif command.lower() in ('q', 'quit'):
        quitGame = True

#******************************#
      # inventory
    elif command == 'inventory':
        print('You are carrying: ')
        print(inventory)

#******************************#
      # gather objects
    elif command.lower().split()[0] == 'get':
        item = command.lower().split()[1]
        if item in current_location['contents']:
            current_location['contents'].remove(item)
            inventory.append(item)
        else:
            print("I don't see that here.")

#******************************#
      # drop objects
    elif command.lower().split()[0] == 'drop':
        item = command.lower().split()[1] 
        if item in inventory:
            current_location['contents'].append(item)
            inventory.remove(item)
        else:
            print("You aren't carrying that.")

#******************************#
      # win condition
        if current_location['name'] == 'an empty room':
            winCheck = 0;
            for wc in current_location['win']:
                for items in current_location['contents']:
                    if wc == items:
                        winCheck = winCheck + 1
                        break 
            if winCheck == 3:
                quitGame = True
                win = True 
#******************************#
      # bad command
    else:
        print("I don't understand that command.")
        
    clear()

#--------------------------------------------------------------------
# END SCREEN
#--------------------------------------------------------------------
if win == True:
    print("You have won the game!")
else:
    print("Thanks for playing!") # the user quits




