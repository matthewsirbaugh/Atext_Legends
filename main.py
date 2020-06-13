from os import system, name
from script import*
import time
        
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
    health   =      100
    shield   =        0
    tactical =        0
    ultimate =        0
    ammo0    =        0
    ammo1    =        0
    ring     =        10
    command  =        ''
    turn     =        1
    playerCharacter = ''
    currentLocation = ''
    playerSet =       False
    locationSet =     False

    # index for gun multidimensional list. 
    # (0,0) is the default melee
    # First index is the weapon name as a string
    # Second index can only be 0, 1, or 2.
    #     representing a near, midrange, or far power adjustment, respectively.
    weapon0  = [0,0]  
    weapon1  = [0,0]

class weapons:
    gun = [\
            ["Melee",    8,  0,  0],
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
            if stats.command in locations[stats.currentLocation]:
                stats.currentLocation = locations[stats.currentLocation][stats.command]
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
class UI(stats, weapons, attatchments, rooms):
    quit = False
    exit = False
    
    def uiReset(self):
        self.quit = False
        self.exit = False
    
    def clear(self):
        if name == 'nt': 
            _ = system('cls')
            
    def centerText(self, text):
        lines = text.split('\n')
        return '\n'.join(line.center(86) for line in lines)
       
    def quitGame(self):
        if stats.command == 'quit' or stats.command == 'q':
            self.quit = True
    
    def exitMenu(self):
        if stats.command == 'exit':
            self.exit = True

    def getInput(self):
        stats.command = input('\tNext Action: ').strip()
        args = stats.command.lower().split(' ',1)
        try:
            if args[1] in locationList: # script has the locations set to the
                args[0] = args[1]       # last word if the location has two words 
                return args
        except IndexError: # otherwise it will throw an error and pass arguments as typed
            pass
        return args
    
    def displayRoom(self):
        print(self.centerText('{}'.format(locations[stats.currentLocation]['name'])))
        print(self.centerText(locations[stats.currentLocation][rooms.currentText]))
#***********************************    
    def startUI(self):
        self.clear()
        print('-------------------------------------------'\
              '-------------------------------------------')
        print(self.centerText('Welcome to Atext Legends!\n'))
        print(self.centerText('To begin, select a character to learn about thier\n'\
              'abilities, and confirm your selection to board the\n'\
              'drop ship and enter the arena!\n'))      
        print(self.centerText('|-----------|------------|------------|'))
        print(self.centerText('|    Loba   | Pathfinder |   Octane   |'))
        print(self.centerText('|-----------|------------|------------|'))
        print(self.centerText('| Bangalore |  Lifeline  | Bloodhound |'))
        print(self.centerText('|-----------|------------|------------|\n'))
        print(self.centerText('Use <help> to learn how to play'))
        print(self.centerText('Use <commands> to see a list of usable commands'))
        print('-------------------------------------------'\
              '-------------------------------------------')
        args = self.getInput()
        self.quitGame()
        return args
#***********************************    
    def characterUI(self, args):
        try:
            self.clear()
            if args[0] in characterList:
                stats.playerCharacter = args[0]
            print('-------------------------------------------'\
                  '-------------------------------------------')
            print(self.centerText(characters[stats.playerCharacter]['name']))
            print(self.centerText('{}\n'.format(characters[stats.playerCharacter]['bio']))) 

            print('    Ultimate: {}\n'.format(characters[stats.playerCharacter]['ultText' ]))
            print('    Tactical: {}\n'.format(characters[stats.playerCharacter]['tactText']))
            print('    Passive:  {}\n\n\n'.format(characters[stats.playerCharacter]['passText']))
            print(self.centerText('Would you like to play as {}?\n'.format(stats.playerCharacter)))
            print(self.centerText('|-----------|------------|------------|'))
            print(self.centerText('|    Loba   | Pathfinder |   Octane   |'))
            print(self.centerText('|-----------|------------|------------|'))
            print(self.centerText('| Bangalore |  Lifeline  | Bloodhound |'))
            print(self.centerText('|-----------|------------|------------|\n'))
            print(self.centerText('Use <help> to learn how to play'))
            print(self.centerText('Use <commands> to see a list of usable commands'))
            print('-------------------------------------------'\
                  '-------------------------------------------')
            args = self.getInput()
            self.exitMenu()
            self.quitGame()
            return args
        except KeyError:
            self.clear()
            print("You fucked up")
#***********************************    
    def locationUI(self):
        self.clear()
        print('-------------------------------------------'\
              '-------------------------------------------')
        print(self.centerText('Location Selection\n'))
        print(self.centerText('The map is split into five parts, each with different '\
              'drop locations.\nEach location has a loot rarity score:\n'\
              'Common[COM] << Average[AVG] << Rare[RAR]\n'\
              'Be cautious, however, as locations with rarer items\n'\
              'also have a higher chance of encountering enemies!\n\n'))
        print(self.centerText('     REGION ONE                 REGION TWO'))
        print(self.centerText('SLUM LAKES  LOOT[{}]    RUNOFF     LOOT[{}]'\
              .format(locationList['lakes'],locationList['runoff'])))
        print(self.centerText('THE PIT     LOOT[{}]\t    BUNKER     LOOT[{}]'\
              .format(locationList['pit'],locationList['bunker'])))
        print(self.centerText('CONTAINMENT LOOT[{}]    AIRBASE    LOOT[{}]\n'\
              .format(locationList['containment'],locationList['airbase'])))
        print(self.centerText('     REGION THREE                REGION FOUR'))
        print(self.centerText('GAUNTLET    LOOT[{}]    SWAMPS     LOOT[{}]'\
              .format(locationList['gauntlet'],locationList['swamps'])))
        print(self.centerText('MARKET      LOOT[{}]    THE CAGE   LOOT[{}]'\
              .format(locationList['market'],locationList['cage'])))
        print(self.centerText('SKULL TOWN  LOOT[{}]    HYDRO DAM  LOOT[{}]'\
              .format(locationList['town'],locationList['dam'])))
        print(self.centerText('THUNDERDOME LOOT[{}]    REPULSOR   LOOT[{}]'\
              .format(locationList['thunderdome'],locationList['repulsor'])))
        print('\t\t     WATER TREATMENT LOOT[{}]\n'.format(locationList['treatment']))
        print(self.centerText('REGION FIVE'))
        print(self.centerText('ARTILLERY   LOOT[{}]'.format(locationList['artillery'])))
        print(self.centerText('RELAY       LOOT[{}]'.format(locationList['relay'])))
        print(self.centerText('WETLANDS    LOOT[{}]'.format(locationList['wetlands'])))
        print()
        print(self.centerText('Type the name of a location to drop there'))
        print()
        print(self.centerText('Use <help> to learn how to play'))
        print(self.centerText('Use <commands> to see a list of usable commands'))
        print('-------------------------------------------'\
              '-------------------------------------------')
        args = self.getInput()
        self.exitMenu()
        self.quitGame()
        return args
#**********************************    
    def mainUI(self):
        self.clear()
        print('-------------------------------------------'\
              '-------------------------------------------')
        print(self.centerText('| Health: {} | Shield {} | Tactical: {} | Ultimate: {} | Ring: {} | Turn {} '\
        '|\n'.format(stats.health, stats.shield, stats.tactical, stats.ultimate, stats.ring, stats.turn))) 
        print(self.centerText('   WEAPONS'))
        print(self.centerText('  {} - {} Rounds\t        {} - {} Rounds\t     '\
        .format(weapons.gun[stats.weapon0[0]][stats.weapon0[1]], stats.ammo0,
                weapons.gun[stats.weapon1[0]][stats.weapon1[1]], stats.ammo1)))
        print(self.centerText(' {}: +{}\t{}: +{}    '.format(*attatchments.stabalizer, 
                                                         *attatchments.stabalizer)))
        print(self.centerText(' {}: +{}\t{}: +{}    '.format(*attatchments.extendedMag,
                                                        *attatchments.extendedMag)))
        print(self.centerText(' {}: +{}\t{}: +{}    '.format(*attatchments.bolt,       
                                                             *attatchments.bolt)))
        print(self.centerText(' {}: +{}\t{}: +{}    '.format(*attatchments.optics,     
                                                         *attatchments.optics)))
        print(self.centerText(' {}: +{}\t{}: +{}    '.format(*attatchments.stock,      
                                                         *attatchments.stock)))
        print()
        self.displayRoom()
        print()
        print(self.centerText('Use <help> to learn how to play'))
        print(self.centerText('Use <commands> to see a list of usable commands'))
        print('-------------------------------------------'\
              '-------------------------------------------')
        args = self.getInput()
        self.quitGame()
        return args
#***********************************    
    def inventoryUI(self):
        self.clear()
        print('-------------------------------------------'\
              '-------------------------------------------')
        print(self.centerText('| Health: {} | Shield {} | Tactical: {} | Ultimate: {} | Ring: {} | Turn {} '\
        '|\n'.format(stats.health, stats.shield, stats.tactical, stats.ultimate, stats.ring, stats.turn)))
        for x in reversed(range(0,5)):
            print('\t',consumables[x],inventory[1][x],'\n')
        print()
        self.displayRoom()
        print('\n')
        print(self.centerText('Use <help> to learn how to play'))
        print(self.centerText('Use <commands> to see a list of usable commands'))
        print('-------------------------------------------'\
              '-------------------------------------------')
        args = self.getInput()
        self.exitMenu()
        self.quitGame()
        return args

"""*****************************
Main Driver
*****************************"""
ui = UI()
mechanic = Mechanics() 
# Need to use stats for data members which means 
# I need to change stats to Statistics and create 
# an object. 

while (1):
    while (not mechanic.playerSet and not ui.quit):
        ui.uiReset()
        command = ui.startUI()
        while (not mechanic.playerSet and not ui.quit):
            command = ui.characterUI(command)
            if command[0] == 'yes': 
                mechanic.playerSet = True
            if ui.exit == True: break
        if ui.quit == True: break    
    if ui.quit == True: break
    
    while (not mechanic.locationSet):
        command = ui.locationUI()
        if command[0] in locationList: 
            stats.currentLocation = command[0]
            mechanic.locationSet = True
        if ui.quit == True: break
    if ui.quit == True: break

    while (not ui.quit):
        ui.uiReset()
        command = ui.mainUI()
        if command[0] in directions:
            mechanic.movement()
        if ui.quit == True: break
    
    if ui.quit == True: break #breaks out of wrapping loop. 

#if mechanic.playerSet == True: break #exit condition for main loop
"""
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
"""
# quit screen
ui.clear()
print("\tThanks for playing!")
















