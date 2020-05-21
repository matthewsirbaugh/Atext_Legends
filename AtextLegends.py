from os import system, name

def clear():
    if name == 'nt': 
        _ = system('cls')
# data setup
rooms = {\
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

directions = ['north', 'south', 'east', 'west']
current_room = rooms['empty']
carrying = []
quitGame = False 
win = False
system('mode con: cols=75 lines=30')
clear()

# game loop
while not quitGame:
    if quitGame == True:
        break
    # display inventory
    print()
    if (carrying):
        print('You are carrying: ', carrying)
    else:
        print("You aren't carrying anything.")
    # display current location
    print('You are in {}.'.format(current_room['name']))
    print(current_room['deftext'])
    # display movable objects
    if current_room['contents']:
        print('In the room are: {}'.format(', '.join(current_room['contents'])))
    # get user input
    command = input('\nWhat do you do? ').strip()
    # movement
    if command in directions:
        if command in current_room:
            current_room = rooms[current_room[command]]
        else:
            # bad movement
            print("You can't go that way.")
    # quit game
    elif command.lower() in ('q', 'quit'):
        quitGame = True
    # inventory
    elif command == 'inventory':
        print('You are carrying: ')
        print(carrying)
    # gather objects
    elif command.lower().split()[0] == 'get':
        item = command.lower().split()[1]
        if item in current_room['contents']:
            current_room['contents'].remove(item)
            carrying.append(item)
        else:
            print("I don't see that here.")
    # get rid of objects
    elif command.lower().split()[0] == 'drop':
        item = command.lower().split()[1]
        if item in carrying:
            current_room['contents'].append(item)
            carrying.remove(item)
        else:
            print("You aren't carrying that.")
    #Win Condition - Place all benches in the original empty room.
        if current_room['name'] == 'an empty room':
            winCheck = 0;
            for wc in current_room['win']:
                for items in current_room['contents']:
                    if wc == items:
                        winCheck = winCheck + 1
                        break 
            if winCheck == 3:
                quitGame = True
                win = True 
    # bad command
    else:
        print("I don't understand that command.")
    clear()
if win == True:
    print("You have won the game!")
else:
    print("Thanks for playing!")