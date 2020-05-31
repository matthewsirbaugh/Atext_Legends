from os import system, name
from script import*

class char:
    currentCharacter = 'loba'
    def getCharacter(self,args):
        if args[0] in characterList:
            self.currentCharacter = args[0]
        
class rooms:
    # room name
    currentRoom = 'empty'
    #location description
    currentText = 'deftext'
    #currently selected item
    currentItem = ''
    #description text for currently selected item
    currentItemText = 'itemtext'

class stats:
    health   =   100
    shield   =     0
    tactical =     0
    ultimate =     0
    ammo0    =     0
    ammo1    =     0
    ring     =    10
    command  =    ''
    turn     =     1

    # index for gun multidimensional list. 
    # (0,0) is the default melee
    # First index is the weapon name as a string
    # Second index can only be 0, 1, or 2.
    #     representing a near, midrange, or far power adjustment, respectively.
    weapon0  = [0,0]  
    weapon1  = [0,0]

class weapons:
    gun = [["Melee",    8,  0,  0],
           ["R-301",   15, 15, 15],
           ["Mastiff", 18, 12,  8]]  

class attatchments:
    stabalizer  = ["Barrel Stabalizer", 0]
    extendedMag = ["Extended Magazine", 0]
    bolt        = ["Shotgun Bolt",      0]
    optics      = ["Optics",            0]
    stock       = ["Stock",             0]

#---------------------------------------------------------
class Mechanics(stats, rooms):
    def movement(self):
        if stats.command in directions:
            if stats.command in locations[rooms.currentRoom]:
                rooms.currentRoom = locations[rooms.currentRoom][stats.command]
        else:
            print("You can't go that way, friend.")
    
    def pickUp(self, args):
        if args[0] == 'get':
            rooms.currentItem = args[1]
        if rooms.currentItem in locations[rooms.currentRoom]['contents']:
            locations[rooms.currentRoom]['contents'].remove(rooms.currentItem)
            # get index of current item
            x = [x for x in inventory if rooms.currentItem in x][0]
            # add one to count
            inventory[1][x.index(rooms.currentItem)] += 1
        else:
            print("No item like that here that I can see.")
    
            
#---------------------------------------------------------
class UI(stats, weapons, attatchments, rooms, char):
    quit = False
    exit = False
    
    def uiReset(self):
        self.quit = False
        self.exit = False
    
    def clear(self):
        if name == 'nt': 
            _ = system('cls')
       
    def quitGame(self):
        if stats.command == 'quit' or stats.command == 'q':
            self.quit = True
    
    def exitMenu(self):
        if stats.command == 'exit':
            self.exit = True

    def getInput(self):
        stats.command = input('\tNext Action: ').strip()
        command = stats.command.lower().split(' ',1)
        return command
    
    def displayRoom(self):
        print('\tYou are in {}.'.format(locations[rooms.currentRoom]['name']))
        print(locations[rooms.currentRoom][rooms.currentText])
#***********************************    
    def characterUI(self, string1):
        self.clear()
        print('----------------------------------------'\
              '----------------------------------------')
        
        
        print('\t\t\t{}\n'.format(characters[string1]['name']))
        print('\t    Ultimate: {}\n'.format(characters[string1]['ultText' ]))
        print('\t    Tactical: {}\n'.format(characters[string1]['tactText']))
        print('\t    Passive:  {}\n'.format(characters[string1]['passText']))
        print('\t\t\tUse <help> to learn how to play.')
        print('\t\tUse <commands> to see a list of usable commands.')
        
        print('----------------------------------------'\
              '----------------------------------------')
        args = self.getInput()
        self.exitMenu()
        return args
#***********************************    
    def startUI(self):
        self.clear()
        print('----------------------------------------'\
              '----------------------------------------')
        print('\t\t\tWelcome to Atext Legends!\n')
        print('\t    Atext Legends is the ultimate test of strength, skill,\n',
              '\tand cunning. You must work with your team to outrun\n',
              '\tthe Ring, claim glory on the battlefield, and earn your\n',
              '\tplace in the Hall of Legends.')
        print('\t    To begin, select a character to learn about thier\n',
              '\tabilities, and confirm your selection to board the\n',
              '\tdrop ship and enter the arena!\n')      
        print('    Loba:')
        print('{}\n'.format(characters['loba']['bio']))
        print('    Bangalore:')
        print('{}\n'.format(characters['bangalore']['bio']))
        print('\t\t\tUse <help> to learn how to play.')
        print('\t\tUse <commands> to see a list of usable commands.')
        print('----------------------------------------'\
              '----------------------------------------')
        args = self.getInput()
        self.exitMenu()
        return args
#***********************************    
    def inventoryUI(self):
        self.clear()
        print('----------------------------------------'\
              '----------------------------------------')
        print('| Health: {} | Shield {} | Tactical: {} | Ultimate: {} | Ring: {} | Turn {} '\
        '|\n\n'.format(stats.health, stats.shield, stats.tactical, stats.ultimate, stats.ring, stats.turn))
        for x in reversed(range(0,5)):
            print('\t',consumables[x],inventory[1][x],'\n')
        print('    Location:')
        self.displayRoom()
        print('\n')
        print('\t\t\tUse <help> to learn how to play.')
        print('\t\tUse <commands> to see a list of usable commands.')
        print('----------------------------------------'\
              '----------------------------------------')
        args = self.getInput()
        self.exitMenu()
        return args
#**********************************    
    def mainUI(self):
        self.clear()
        print('----------------------------------------'\
              '----------------------------------------')
        print('| Health: {} | Shield {} | Tactical: {} | Ultimate: {} | Ring: {} | Turn {} '\
        '|\n'.format(stats.health, stats.shield, stats.tactical, stats.ultimate, stats.ring, stats.turn)) 
        print('    Weapons:')
        print('\t{} - {} Rounds'.format(weapons.gun[stats.weapon0[0]][stats.weapon0[1]], stats.ammo0))
        print('\t\t{}: +{}'.format(*attatchments.stabalizer))
        print('\t\t{}: +{}'.format(*attatchments.extendedMag))
        print('\t\t{}     : +{}'.format(*attatchments.bolt))
        print('\t\t{}           : +{}'.format(*attatchments.optics))
        print('\t\t{}            : +{}'.format(*attatchments.stock))
        print()
        print('\t{} - {} Rounds'.format(weapons.gun[stats.weapon1[0]][stats.weapon1[1]], stats.ammo0))
        print('\t\t{}: +{}'.format(*attatchments.stabalizer))
        print('\t\t{}: +{}'.format(*attatchments.extendedMag))
        print('\t\t{}     : +{}'.format(*attatchments.bolt))
        print('\t\t{}           : +{}'.format(*attatchments.optics))
        print('\t\t{}            : +{}'.format(*attatchments.stock))
        print('    Location:')
        self.displayRoom()
        print('----------------------------------------'\
              '----------------------------------------')
        args = self.getInput()
        self.quitGame()
        return args
"""
********************************
Main Driver
********************************
"""
ui = UI()
mechanic = Mechanics()
character = char()

#command = ui.startUI()
#character.getCharacter(command)
#command = ui.characterUI(character.currentCharacter)

while (1):
    command = ui.mainUI()
    if ui.quit == True: break

    if command[0] in directions:
        mechanic.movement()
        
    while (command[0] == 'inventory'):
        command = ui.inventoryUI()
        #if command[0] == 'use':
        if ui.exit == True: break

    #while (command[0] in commandList):
    
    if command[0] == 'get':
        mechanic.pickUp(command)
    
    ui.uiReset()

# quit screen
print("\tThanks for playing!")
