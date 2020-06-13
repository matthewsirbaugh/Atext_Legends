locationList = {\
        'lakes'      :'AVG', 'containment':'AVG', 'pit'      :'RAR',    
        'runoff'     :'RAR', 'bunker'     :'RAR', 'airbase'  :'RAR', 
        'gauntlet'   :'RAR', 'town'       :'AVG', 'market'   :'COM',  
        'thunderdome':'RAR', 'treatment'  :'RAR', 'cage'     :'AVG',    
        'dam'        :'COM', 'repulsor'   :'RAR', 'swamps'   :'RAR',  
        'wetlands'   :'AVG', 'relay'      :'RAR', 'artillery':'RAR'}

locations   = {\
'lakes'       :   {'name': 'Slum Lakes', 'region' : 1, 
                   'northeast':'artillery', 'southeast':'containment', 'south':'pit',
        'deftext' :'____________________________________________________________\n\n' #60
                   'You\'re in Slum Lakes, a large town of shacks chock full of\n'
                   'tasty Loot. Fights here are close quarters, with a 10% Buff\n'
                   'to Shotguns and a 10% Nerf to Snipers.\n\n\n\n'
                   '____________________________________________________________\n',
        'contents':['med kit']},
'containment' :   {'name': 'Containment', 'region' : 1, 
                   'west':'lakes', 'east':'artillery',
        'deftext' :'____________________________________________________________\n\n'
                   'Containment is comprised of a series of abandoned labs, with\n'
                   'a spire in the center. Midrange weapons get a 15% Buff, and\n'
                   'caged Flyers will cry out when approached, making it harder\n'
                   'for Enemies to sneak up on you.\n\n\n'
                   '____________________________________________________________\n',
        'contents':['med kit']},
'pit'         :   {'name': 'The Pit', 'region' : 1, 
                   'north':'lakes', 'south':'runoff',
        'deftext' :'____________________________________________________________\n\n'
                   'Welcome to The Pit, where Black Friday is everyday. There\'s\n'
                   'plenty of Supply Bins and Loot on the ground, but you\'ll\n'
                   'have to hurt some feelings if you\'re going to take it. Be\n'
                   'cautious, though. There\'s no cover, and Lifeline can\'t call\n'
                   'down any Care Packages while inside.\n\n'
                   '____________________________________________________________\n',
        'contents': ['med kit']},
'runoff'      : {  'name': 'Runoff', 'region' : 2, 
                   'north':'pit', 'east':'bunker', 'south':'airbase',
        'deftext' :'____________________________________________________________\n\n'
                   'Runoff is a hot drop Location with large buildings. The\n'
                   'buildings offer ample cover, and the long hallways are great\n'
                   'for close quarters gun fights, giving Midrange weapons a\n'
                   '10% Buff in Power.\n\n\n'
                   '____________________________________________________________\n',
        'contents': ['med kit']},
'bunker'      :   {'name': 'Bunker', 'region' : 2, 
                   'northwest':'runoff', 'southwest':'airbase',
        'deftext' :'____________________________________________________________\n\n'
                   'Bunker is, quite literally, a bunker built into a mountain.\n'
                   'Outside of Bunker you can find Supply Bins, and inside you\n'
                   'can find high yier Loot. Inside bunker is a tight corridor\n'
                   'with several small rooms that break off from it. Shotguns\n'
                   'get a 10% Buff.\n\n'
                   '____________________________________________________________\n',
        'contents': ['med kit']},
'airbase'     :   {'name': 'Airbase', 'region' : 2, 
                   'north':'runoff', 'east':'bunker', 'south':'gauntlet',
        'deftext' :'____________________________________________________________\n\n'
                   'Here, you\'ll find decent loot, but the danger is wall to\n'
                   'wall. There are a few buildings here, and a vantage point\n'
                   'that\'s great for Snipers, giving them a 15% buff. There\'s\n'
                   'enough cover for team fights, but the loot is a bit sparse.\n\n\n'
                   '____________________________________________________________\n',
        'contents': ['med kit']},
'gauntlet'    :   {'name': 'Gauntlet', 'region' : 3, 
                   'north':'airbase', 'east':'market', 'south':'town',
        'deftext' :'____________________________________________________________\n\n'
                   'Gauntlet is an adrenaline fueled arena inspired by the champ\n'
                   'himself, Octane. In the center of the arena is a large ring\n'
                   'of fire, with ramps on either side. Jump Pads are located at\n'
                   'various Locations, adding acrobatics to the chaos of battle.\n\n\n'
                   '____________________________________________________________\n',
        'contents': ['med kit']},
'market'      :   {'name': 'Market', 'region' : 3, 
                   'northwest':'gauntlet', 'southwest':'town', 'south':'treatment',
        'deftext' :'____________________________________________________________\n\n'
                   'This Market is where retail employees go to vent, with all\n'
                   'the bloodshed that entails. The inside of Market has several\n'
                   'rooms along the internal perimeter, and large rooftop that\'s\n'
                   'great for sniping or just staying above the action, giving\n'
                   'Snipers and Shotguns a 10% Buff\n\n'
                   '____________________________________________________________\n',
        'contents': ['med kit']},
'town'        :   {'name': 'Skull Town', 'region' : 3, 
                   'north':'gauntlet', 'east':'market', 'south':'thunderdome',
        'deftext' :'____________________________________________________________\n\n'
                   'You\'re in the infamous Skull Town, a plus-shaped 4 lane area\n'
                   'with multiple buildings and all the highground. The skeleton\n'
                   'of a gargantuan beast covers the town. This area has the\n'
                   'highest chance of Enemy encounters, but if you can survive\n'
                   'here, you can survive anywhere (your experience may vary)\n\n'
                   '____________________________________________________________\n',
        'contents': ['med kit']},
'thunderdome' :   {'name': 'Thunderdome', 'region' : 3, 
                   'north':'town', 'east':'treatment',
        'deftext' :'____________________________________________________________\n\n'
                   'If you go to Skulltown to prove you can survive, you go to\n'
                   'Thunderdome to prove you can kill. There\'s tons of Loot, and\n'
                   'plenty of victims. Get ready for the fight of your life, or\n'
                   'at least the last few minutes of it. You\'re guaranteed to\n'
                   'encounter an Enemy the first time you come here, so come\n'
                   'prepared and blood thirsty.\n'
                   '____________________________________________________________\n',
        'contents': ['med kit']},
'treatment'   :   {'name': 'Water Treatment', 'region' : 3, 
                   'west':'thunderdome', 'northwest':'market', 'north':'cage',
        'deftext' :'____________________________________________________________\n\n'
                   'Water Treatment is the southern most location on the map.\n'
                   'There\'s quite a few buildings, with large hallways and ropes\n'
                   'for increased manuverability. Your back is to the ocean,\n'
                   'and Enemies can be seen approaching from far, so Snipers get\n'
                   'a 20% Buff, and Midrange weapons get a 10% Buff as well.\n'
                   'Be careful when approaching, as Buffs apply to Enemies too!\n'
                   '____________________________________________________________\n',
        'contents': ['med kit']},
'cage'        :   {'name': 'The Cage','region' : 4, 
                   'northeast':'swamps', 'east':'dam', 'southeast':'repulsor', 'south':'treatment', 
        'deftext' :'____________________________________________________________\n\n'
                   'The cage is a very active drop location thanks to being the\n'
                   'highest highground in the game. The tower in the center of\n'
                   'the location must be scaled from the inside without the help\n'
                   'of an ability, so Legends with movement abilities have an\n'
                   'advantage here. Snipers recieve a 20% Buff.\n\n'
                   '____________________________________________________________\n', 
        'contents': ['shield cell']},
'dam'         :   {'name': 'Hydro Dam','region' : 4, 
                   'west':'cage', 'east':'swamps', 
        'deftext' :'____________________________________________________________\n\n'
                   'Hydro Dam is located in the heart of Region Four, and houses\n'
                   'rare loot, and as a consequence, is a frequently visited\n'
                   'Location. The large open spaces make traversing the location\n'
                   'safely difficult, and Midrange weapons particularly deadly,\n'
                   'giving them a 20% Buff in Power\n\n'
                   '____________________________________________________________\n',  
        'contents': ['shield cell']},
'repulsor'    : {'name': 'Repulsor', 'region' : 4, 
                 'northwest':'cage', 'northeast':'swamps', 
        'deftext' :'___________________________________________________________\n\n' 
                   'Repulsor is an abandoned military facility, characterized\n'
                   'by the destroyed Repulsor Tower located there, which used\n'
                   'keep the Leviathans from trampling King\'s Canyon. There\n'
                   'are several building here, with a unique tunnel system\n'
                   'that makes escaping much easier, giving a 10% Buff when\n'
                   'attempting to Escape\n'
                   '____________________________________________________________\n', 
        'contents': ['shield cell']},
'swamps'      : {'name': 'Swamps', 'region' : 4, 
                 'north':'wetlands', 'west':'cage', 'southwest':'dam', 'south':'repulsor', 
        'deftext' :'___________________________________________________________\n\n' 
                   'The buildings in this location are built on stilts, high\n'
                   'in the air. The buildings are connected by bridges and\n'
                   'ziplines, making it the perfect spot for quick getaways\n'
                   'and strategic repositioning, giving a 10% buff when\n'
                   'attempting to Escape\n\n'
                   '____________________________________________________________\n', 
        'contents': ['shield cell']},
'wetlands'    :  {'name': 'Wetlands','region' : 5, 
                  'northwest':'artillery', 'northeast':'relay', 'south':'swamps',
        'deftext' :'____________________________________________________________\n\n'
                   'Wetlands is a Location surrounded by swampland. There are\n'
                   'a few buildings here, but largely there is very little in\n'
                   'the way of cover. The same can be said for the Loot, which\n'
                   'is to say, "What Loot?"\n\n\n'
                   '____________________________________________________________\n',
        'contents': ['shield battery']},
'relay'       :  {'name': 'Relay','region' : 5, 
                  'west':'artillery', 'south':'wetlands',
        'deftext' :'____________________________________________________________\n\n'
                   'Relay is located in the northeastern corner of the map. The\n'
                   'Loot here is middle of the row, but it has the least likely\n'
                   'chance for Enemy encounters of any location. Zip lines\n'
                   'connect several buldings, making looting a quick process,\n'
                   'but you\'re vulnerable while zipping to the next buiding.\n\n'
                   '____________________________________________________________\n',
        'contents': ['shield battery']},
'artillery'   :  {'name': 'Artillery', 'region' : 5, 
                  'northwest':'lakes', 'southwest':'containment', 'northeast':'relay', 'southeast':'wetlands',
        'deftext' :'____________________________________________________________\n\n'
                   'Artillery is an abandoned military compound, located in the\n'
                   'northern most part of the map. Here you\'ll find bunkers and\n'
                   'buildings containing high tier loot, along with plenty of\n'
                   'other players to keep you company\n\n\n'
                   '____________________________________________________________\n',
        'contents':['syringe']}}
#----------------------------------------------------------------------------------------
characterList= ['loba','bangalore']
characters   = {\
'loba'     :{'name'    :'Loba - High Society Thief', 
             'passive' :'Eye For Quality', 
             'tactical':"Burglar's Best Friend",
             'ultimate':'Black Market Boutique',
    'bio'     :'____________________________________________________________\n\n'
               'When Loba was nine, she looked on as simulacrum hitman\n'
               'Revenant killed her family. Left with nothing, Loba survived\n'
               'by picking pockets. As her skills improved, Loba used every\n'
               'tool at her disposal to lift herself from the gutter.\n'
               'Everything changed when she broke into a supposedly\n'
               'impenetrable facility and got her hands on the Jump Drive\n'
               'tech stored inside. With her new teleportation bracelet,\n'
               'the most secure and unattainable items were within her\n'
               'reach. So was her dream of living the high life.\n'
               '____________________________________________________________\n',
    'passText':'\tLpassive text\n' 
               '\t\tpassive text',
    'tactText':'\ttactical text\n' 
               '\t\ttactical text',
    'ultText' :'\tultimate text\n' 
               '\t\tultimate text'},
'bangalore':{'name'    :'Bangalore - Professional Soldier', 
             'passive' :'Double Time', 
             'tactical':'Smoke Launcher',
             'ultimate':'Rolling Thunder',
    'bio'     :'____________________________________________________________\n\n'
               'Born into a military family where she, her parents, and her\n'
               'four older brothers all served in the IMC Armed Forces,\n'
               'Bangalore has been an exceptional soldier since she was\n'
               'young. She was top of her class at the IMC Military Academy\n'
               'and the only cadet who could take apart a Peacekeeper, equip\n'
               'it with a Precision Choke hop-up, and put it back together\n'
               'in under twenty seconds - blindfolded. Bangalore fights to\n'
               'raise money for passage back to the IMC home base, where she\n'
               'hopes to reunite with what remains of her family.\n'
               '____________________________________________________________\n',
    'passText':'\tBpassive text\n' 
               '\tpassive text',
    'tactText':'\ttactical text\n' 
               '\ttactical text',
    'ultText' :'\tultimate text\n' 
               '\tultimate text'}}
#----------------------------------------------------------------------------------------
directions  = ['north', 'south', 'east', 'west', 'northeast','southeast','northwest','southwest']

consumables = ['Syringe:             X',
               'Med Kit:             X',
               'Shield Cell:         X',
               'Shield Battery:      X',
               'Ultimate Accelerant: X']

"""
UI  = inventory[0][X]
num = inventory[X][0]
Syringe       Med Kit    
[0][0]        [0][1]
[1][0]        [1][1]
Shield Cell   Shield Battery
[0][2]        [0][3]
[1][2]        [1][3]
"""
inventory = [['syringe','med kit','shield cell','shield battery','ultimate accelerant'],
             [        0,        0,            0,               0,                    0],
             [       25,      100,           25,             100,                   20]]
