#--------------------------------------------------------------------
# RESOURCES
#--------------------------------------------------------------------
from os import system, name
from util import*
system('mode con: cols=90 lines=50') # screen size
#--------------------------------------------------------------------
# DATA
#--------------------------------------------------------------------
    # initialize location
    # game variables
inventory = [] 
quitGame = False 
win = False

#--------------------------------------------------------------------           
# GAME LOGIC
#--------------------------------------------------------------------
    # main game loop
clear()
while not quitGame:
    if quitGame == True:
        break

    displayUI()
    displayLocation()

      # display objects
    if current_location['contents']:
        print('\tIn the room are: {}'.format(', '.join(current_location['contents'])))

      # get input
    print(ui['bar'])
    command = input('\tNext Action: ').strip()

      # movement
    if command in directions:
        if command in current_location:
            current_location = locations[current_location[command]]
        else:
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

      # drop objects
    elif command.lower().split()[0] == 'drop':
        item = command.lower().split()[1] 
        if item in inventory:
            current_location['contents'].append(item)
            inventory.remove(item)
        else:
            print("You aren't carrying that.")

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
    print("Thanks for playing!")




