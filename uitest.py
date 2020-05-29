from os import system, name
from script import*
       
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

class consumables:
    shieldCell    = ["Shield Cell",     25]
    shieldBattery = ["Shield Battery", 100]
    syringe       = ["Syringe",         25]
    medKit        = ["Med Kit",        100]
       
#---------------------------------------------------------
class mainMechanics(stats, rooms):
    def movement(self):
        if stats.command in directions:
            if stats.command in locations[rooms.currentRoom]:
                rooms.currentRoom = locations[rooms.currentRoom][stats.command]
        else:
            print("You can't go that way.")
       
#---------------------------------------------------------
class ui(stats, weapons, attatchments, rooms):
    quit = False
    
    def clear(self):
        if name == 'nt': 
            _ = system('cls')
       
    def quitGame(self):
        if stats.command == 'quit' or stats.command == 'q':
            self.quit = True

    def getInput(self):
        stats.command = input('\tNext Action: ').strip()
    
    def displayRoom(self):
        print('\tYou are in {}.'.format(locations[rooms.currentRoom]['name']))
        print(locations[rooms.currentRoom][rooms.currentText])
    
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
        self.getInput()
        self.quitGame()

"""
********************************
Main Driver
********************************
"""
uiManager = ui()
mainManager = mainMechanics()
while (1):
    uiManager.mainUI()
    if uiManager.quit == True: break
    mainManager.movement()

