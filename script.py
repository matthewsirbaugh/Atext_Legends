locations   = {\
'empty' : {'name': 'an empty room', 'east': 'bedroom', 'north': 'temple',
    'deftext' : '\tThe stone floors and walls are cold and damp.\n' 
                '\tTo the north is a temple, and to the east is a bedroom.',
    'contents': ['med kit']},
'temple' : {'name': 'a small temple', 'east': 'torture', 'south': 'empty', 
    'deftext': '\tThis seems to be a place of worship and deep\n' 
               '\tcontemplation. To the east is a gruesome looking\n' 
               '\troom, and to the south is an empty room.', 
    'contents': ['shield cell']},
'torture': {'name': 'a torture chamber', 'west': 'temple', 'south': 'bedroom',
    'deftext' : '\tThere is a rack and an iron maiden against the wall \n'
                '\tand some dark stains on the floor. To the south is \n'
                '\ta bedroom, and the temple is to the west.',
    'contents': ['shield battery']},
'bedroom' : {'name': 'a bedroom', 'north': 'torture', 'west': 'empty',
    'deftext' : '\tThis is clearly a bedroom, but no one has slept here \n'
                '\tin a long time. To the west is the room where you awoke, \n'
                '\tand to the north is the torture chamber.',
    'contents': ['syringe']}}
characterList= ['loba']
characters   = {\
'loba'      : {'name'    :'Loba', 
               'passive' :'Eye For Quality', 
               'tactical':"Burglar's Best Friend",
               'ultimate':'Black Market Boutique',
    'biography'   :'\tbiography text\n' 
                   '\tbiography text',
    'passiveText' :'\tpassive text\n' 
                   '\tpassive text',
    'tacticalText':'\ttactical text\n' 
                   '\ttactical text',
    'ultimateText':'\tultimate text\n' 
                   '\tultimate text'},
'bangalore' : {'name'    :'Bangalore', 
               'passive' :'Double Time', 
               'tactical':'Smoke Launcher',
               'ultimate':'Rolling Thunder',
    'biography'   :'\tbiography text\n' 
                   '\tbiography text',
    'passiveText' :'\t\n' 
                   '\t',
    'tacticalText':'\t\n' 
                   '\t',
    'ultimateText':'\t\n' 
                   '\t'}}

directions  = ['north', 'south', 'east', 'west']

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

 
