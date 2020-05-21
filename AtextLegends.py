# RESOURCES
#--------------------------------------------------------------------
from os import system, name
system('mode con: cols=75 lines=50') # screen size

# DATA
#--------------------------------------------------------------------
  # location data
locations = {\
    'empty': {'name': 'an empty room', 'east': 'bedroom', 'north': 'temple',
        'deftext': 'The stone floors and walls are cold and damp.\n' 
                   'To the north is a temple, and to the east is a bedroom.',
        'contents': [],
        'win': ['candle','statue','bench']},
    'temple': {'name': 'a small temple', 'east': 'torture', 'south': 'empty', 
        'deftext': 'This seems to be a place of worship and deep contemplation. \n' 
                   'To the east is a gruesome looking room, and the south is an empty room.', 
        'contents': ['bench', 'candle', 'bench', 'statue']},
    'torture': {'name': 'a torture chamber', 'west': 'temple', 'south': 'bedroom',
        'deftext': 'There is a rack and an iron maiden against the wall \n'
                   'and some dark stains on the floor. To the south is \n'
                   'a bedroom, and the temple is to the west.',
        'contents': []},
    'bedroom': {'name': 'a bedroom', 'north': 'torture', 'west': 'empty',
        'deftext': 'This is clearly a bedroom, but no one has slept here \n'
                   'in a long time. To the west is the room where you awoke, \n'
                   'and to the north is the torture chamber.',
        'contents': ['sheets', 'bed']}}

  # user interface
ui = {\
    'stats': {'shield': 0, 'health': 100, 'tactical': 0, 
              'ultimate': 0, 'ammo1': 0, 'ammo2': 0, 'ring' : 10},
    'design': { 'bar': '----------------------------------------------------------------------',
                'health': 'Shield/Health: ', 
                'tactical': ' | Tactical: (', 
                'ultimate': ') | Ultimate: (', 
                'weapons' : ')\nWeapons:\n', 
                'location': 'Location:\n', 
                'ring1': '\tThe Ring is (', 
                'ring2': ') turns from closing.\n\n',}}
                
  # weapons
weapons = {\
    'melee'  :   {'closeRange':  8,'midRange': 0,'farRange':  0},
    'mastiff': {'closeRange': 20,'midRange': 15,'farRange':  9},
    'r-301':   {'closeRange': 16,'midRange': 18,'farRange': 16,}}
    
  # attatchments
  
  # consumables
consumables = {\
    'shield'  : {'Shield Cell':  25, 'Shield Battery': 100},
    'health'  : {'Syringe': 25, 'Med Kit': 100},
    'ultaccel': {'Ultimate Accelerant': 25}}


directions = ['north', 'south', 'east', 'west'] # movement

current_location = locations['empty'] # initialize starting room
weapon0 = weapons['melee']
weapon1 = weapons['melee']
stats = ui['stats'] 
ui = ui['design']
inventory = [] # player inventory
quitGame = False # set to false so quitGame = True exits the game loop
win = False # token used to determine if the game is won

# FUNCTIONS
#--------------------------------------------------------------------
    # clear screen
def clear():
    if name == 'nt': 
        _ = system('cls')
        
    # user interface
def displayUI():
    print(ui['bar'])
    print(ui['health'],stats['shield'],'/',
          stats['health'],ui['tactical'],
          stats['tactical'],ui['ultimate'],
          stats['ultimate'],ui['weapons'], # add the weapon ui after this
          ui['ring1'],stats['ring'],
          ui['ring2'], ui['location'])

# GAME LOGIC
#--------------------------------------------------------------------
clear() # clear screen to begin game

    # character and drop location selection
#while not quitGame:
#    if quitGame == True:
#        break
#

    # main game loop
while not quitGame:
    if quitGame == True:
        break

      # display inventory
    print()
    if (inventory):
        print('You are carrying: ', inventory)
    else:
        print("You aren't carrying anything.")
    displayUI()
      # display current location
    print('You are in {}.'.format(current_location['name']))
    print(current_location['deftext'])

      # display movable objects
    if current_location['contents']:
        print('In the room are: {}'.format(', '.join(current_location['contents'])))

      # get input
    command = input('\nWhat do you do? ').strip()

      # movement
    if command in directions:
        if command in current_location:
            current_location = locations[current_location[command]]
        else:
              # bad movement
            print("You can't go that way.")

      # quit game
    elif command.lower() in ('q', 'quit'):
        quitGame = True

      # inventory
    elif command == 'inventory':
        print('You are carrying: ')
        print(inventory)

      # gather objects
    elif command.lower().split()[0] == 'get':
        item = command.lower().split()[1]
        if item in current_location['contents']:
            current_location['contents'].remove(item)
            inventory.append(item)
        else:
            print("I don't see that here.")

      # get rid of objects
    elif command.lower().split()[0] == 'drop':
        item = command.lower().split()[1] # parses dropped item
        if item in inventory:
            current_location['contents'].append(item)
            inventory.remove(item)
        else:
            print("You aren't carrying that.")

      # win condition built into drop mechanic "Placing Trophies from Zork"
        if current_location['win']:
            winCheck = 0;
            for wc in current_location['win']:
                for items in current_location['contents']:
                    if wc == items:
                        winCheck = winCheck + 1
                        break 
            if winCheck == 3:
                quitGame = True
                win = True 

      # bad command
    else:
        print("I don't understand that command.")
        
    clear() # clear screen for next turn
    
# END SCREEN
#--------------------------------------------------------------------
if win == True:
    print("You have won the game!")
else:
    print("Thanks for playing!") # the user quits










