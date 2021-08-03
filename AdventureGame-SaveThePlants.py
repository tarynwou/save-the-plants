#created by Taryn Wou
#Adventure Game - Save The Plants

import random

chance = (0, 1, 2, 3, 4)

def showInstructions():
  #print a main menu and the commands
  print('''
ADVENTURE GAME - SAVE THE PLANTS


You live in the village Crestwood in the heart of Veil. The kingdom of Veil is of a prosperous yet sustainable type, the entire kingdom’s source of food is provided by the 7 sacred “Fergle Plants”. Crestwood is a place of serenity and politeness. This morning, however, you were awakened to the sound of frantic knocking at your door. The person was gone by the time you opened your door.

Whoever it was had left this newsletter at your front step.

Newsletter:
“THE CREST OF VEIL
Sometime during the night, the town’s most valuable possessions, the ‘Fergle Plants’ were stolen from the royal garden by a malevolent wizard. He has since taken over the tower and is taking pleasure in starving the town. The king has sent out all of his most skilled kingsmen soon after the incident to retrieve the ‘Fergle Plants’ and defeat the beast, but none of them have returned since. The King has announced a huge reward to whoever can get to the castle tower, defeat the wizard, and save the vital plants to save the town.”

You, a humble and ethical individual passionate about the welfare of your family, friends, and neighbours, have decided to embark on your quest to save the “Fergle Plants” and save the town. You will have to travel through the purple forest to get to the castle, so prepare yourself by loading up on goodies and seeking advice from the townspeople.

Don’t get too distracted by chatting up the village, you have a quest to endeavour on! Get to the castle to defeat the wizard! The time is ticking my friend!

================
Commands:
  go [direction: north, south, east, west, up, down]
  run [direction: north, south, east, west] (allows you a 40% chance of escaping a sticky situation)
  buy [item]
  use [item]
  attack
  yes
  no
  help (will repeat these commands at any point and time in the game)
================
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are at ' + currentRoom)
  #the directions that the user can go to are only displayed if there are rooms that they can go to
  if 'north' in gamemap[currentRoom]:
    print('North: ' + gamemap[currentRoom]['north'])
  if 'east' in gamemap[currentRoom]:
    print('East: ' + gamemap[currentRoom]['east'])
  if 'south' in gamemap[currentRoom]:
    print('South: ' + gamemap[currentRoom]['south'])
  if 'west' in gamemap[currentRoom]:
    print('West: ' + gamemap[currentRoom]['west'])
  if 'up' in gamemap[currentRoom]:
    print('Up: ' + gamemap[currentRoom]['up'])
  if 'down' in gamemap[currentRoom]:
    print('Down: ' + gamemap[currentRoom]['down'])
  #this shows their coins and health
  print('Coins:' , coins)
  print('Health:' , health)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in gamemap[currentRoom]:
    print('You see ', gamemap[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
gamemap = {
          #village
            'Your Home' : { 
                  'west' : 'Sally\'s Home',
                  'east' : 'Christopher\'s Home',
                  'north' : 'The Well',
                  'text' : 'yourhome'
                },
            'Sally\'s Home' : {
                  'east' : 'Your Home',
                  'west' : 'Leif\'s Home',
                  'north' : 'The Bank',
                  'text' : 'sallyshome'
                },
            'Christopher\'s Home' : {
                  'west' : 'Your Home',
                  'east' : 'Esther\'s Home',
                  'north' : 'The Bakery',
                  'text' : 'christophershome'
                },
            'Leif\'s Home' : {
                  'east' : 'Sally\'s Home',
                  'north' : 'The Cobbler\'s Den',
                  'text' : 'leifshome'
                },
            'Esther\'s Home' : {
                  'west' : 'Christopher\'s Home',
                  'north' : 'The Apothecary Shop',
                  'text' : 'esthershome'
                },
            'The Apothecary Shop' : {
                  'south' : 'Esther\'s Home',
                  'north' : 'The Trading Post',
                  'east' : 'The Postal Office',
                  'west' : 'The Bakery',
                  'sage' : 'sage' ,
                  'crystal' : 'crystal',
                  'lantern' : 'lantern',
                  'text' : 'apothecary'
                },
            'The Postal Office' : {
                  'west' : 'The Apothecary Shop',
                  'north' : 'The Tavern',
                  'text' : 'postaloffice'
                },
            'The Trading Post' : {
                  'east' : 'The Tavern',
                  'south' : 'The Apothecary Shop',
                  'west' : 'The Inn',
                  'axe' : 'axe',
                  'potion' : 'potion',
                  'shield' : 'shield',
                  'text' : 'tradingpost'
                  },
            'The Tavern' : {
                  'west' : 'The Trading Post',
                  'south' : 'The Postal Office',
                  'text' : 'tavern'   
                  },
            'The Bakery' : {
                  'east' : 'The Apothecary Shop',
                  'west' : 'The Well',
                  'south' : 'Christopher\'s Home',
                  'north' : 'The Inn',
                  'bread' : 'bread',
                  'meat' : 'meat',
                  'text' : 'bakery'
                  },
            'The Inn' : {
                  'east' : 'The Trading Post',
                  'west' : 'The Masonry',
                  'south' : 'The Bakery',
                  'text' : 'inn'
                  },
            'The Well' : {
                  'east' : 'The Bakery',
                  'west' : 'The Bank',
                  'south' : 'Your Home',
                  'north' : 'The Masonry',
                  'text' : 'well',
                  'moneyman' : 'man'
                  },
            'The Masonry' : {
                  'east' : 'The Inn',
                  'west' : 'Town Hall',
                  'south' : 'The Well',
                  'north' : 'The Forest Entry',
                  'text' : 'masonry'
                  },
            'The Bank' : {
                  'east' : 'The Well',
                  'west' : 'The Cobbler\'s Den',
                  'south' : 'Sally\'s Home',
                  'north' : 'Town Hall',
                  'text' : 'bank'
                  },
            'Town Hall' : {
                  'east' : 'The Masonry',
                  'west' : 'The Church',
                  'south' : 'The Bank',
                  'text' : 'townhall'
                  },
            'The Cobbler\'s Den' : {
                  'east' : 'The Bank',
                  'west' : 'The Library',
                  'north' : 'The Church',
                  'south' : 'Leif\'s Home',
                  'text' : 'cobblersden'
                  },
            'The Church' : {
                  'west' : 'The Fortune Teller\'s Tent',
                  'east' : 'Town Hall',
                  'south' : 'The Cobbler\'s Den',
                  'text' : 'church'
                  },
            'The Fortune Teller\'s Tent' : {
                  'east' : 'The Church',
                  'south' : 'The Library',
                  'text' : 'fortunetllerstent'
                  },
            'The Library' : {
                  'east' : 'The Cobbler\'s Den',
                  'north' : 'The Fortune Teller\'s Tent',
                  'text' : 'library'
                  },
            'The Forest Entry' : {
              'south' : 'The Masonry',
              'north' : 'Shabby Leaves',
              'text' : 'forestentry'
              },
         #forest
            'Shabby Leaves' : {
              'south' : 'The Forest Entry',
              'east' : 'Dobson\'s Fork',
              'west' : 'The Knight\'s Pathway',
              'north' : 'The Mystic Pond',
              'text' : 'shabbyleaves'
              },
            'The Mystic Pond' : {
              'south' : 'Shabby Leaves',
              'enemy' : 'thief',
              'text' : 'mysticpond'
              },
            'Dobson\'s Fork' : {
              'west' : 'Shabby Leaves',
              'north' : 'The Castle Landing',
              'east' : 'The Cave Entrance',
              'enemy' : 'thief',
              'text' : 'dobsonsfork'
              },
            'The Knight\'s Pathway' : {
              'east' : 'Shabby Leaves',
              'west' : 'The Castle Landing',
              'text' : 'knightspathway'
              },
            'The Castle Landing' : {
              'south' : 'Dobson\'s Fork',
              'west' : 'The Gatehouse',
              'east' : 'The Knight\'s Pathway',
              'enemy' : 'possessed guard',
              'text' : 'castlelanding'
              },

        #cave
            'The Cave Entrance' : {
              'west' : 'Dobson\'s Fork',
              'text' : 'caveentrance',
              },
            
              
              
        #castle
            #dungeon
            'The Dungeon Hallway 1' : {
              'north' : 'The Dungeon Hallway 2',
              'south' : 'The Bottom of Stairwell 1',
              'enemy' : 'possessed guard',
              'text' : 'dungeonhallway1'
                  },
            'The Dungeon Hallway 2' : {
              'south' : 'The Dungeon Hallway 1',
              'sword' : 'sword',
              'text' : 'dungeonhallway2'
                  },
            'The Bottom of Stairwell 1' : {
              'north' : 'The Dungeon Hallway 1',
              'up' : 'The Top of Stairwell 1',
              'text' : 'bottomofstair1',

                  },
            'The Top of Stairwell 1' : {
              'north' : 'The Place of Arms',
              'down' : 'The Bottom of Stairwell 1',
              'text' : 'topofstair1',
                  },
            #middlefloor
            'The Place of Arms' : {
              'west' : 'The Lavatories',
              'north' : 'The Gatehouse',
              'south' : 'The Top of Stairwell 1',
              'text' : 'placeofarms'
              },
            'The Lavatories' : {
              'north' : 'The Servant\'s Quarters',
              'east' : 'The Place of Arms',
              'text' : 'Lavatories',
              
              },
            'The Servant\'s Quarters' : {
              'east' : 'The Gatehouse',
              'south' : 'The Lavatories',
              'north' : 'The Great Hall',
              'enemy' : 'possessed guard',
              'text' : 'servantsquarter'
              },
            'The Gatehouse' : {
              'north' : 'The Kitchen',
              'south' : 'The Place of Arms',
              'west' : 'The Servant\'s Quarters',
              'east' : 'The Castle Landing',
              'enemy' : 'possessed guard',
              'text' : 'gatehouse'
              },
            'The Kitchen' : {
              'north' : 'The Pantries',
              'south' : 'The Gatehouse',
              'west' : 'The Great Hall',
              'enemy' : 'possessed guard',
              'text' : 'kitchen'
              },
            'The Great Hall' : {
              'north' : 'The Buttery',
              'south' : 'The Servant\'s Quarters',
              'east' : 'The Kitchen',
              'text' : 'greathall'
              },
            'The Buttery' : {
              'south' : 'The Great Hall',
              'east' : 'The Pantries',
              'north' : 'The Bottom of Stairwell 2',
              'text' : 'buttery'
              },
            'The Pantries' : {
              'south' : 'The Kitchen',
              'west' : 'The Buttery',
              'enemy' : 'possessed guard',
              'text' : 'pantries'
              },
            'The Bottom of Stairwell 2' : {
              'south' : 'The Buttery',
              'up' : 'The Top of Stairwell 2',
              'text' : 'bottomofstair2',
              },
            #royalfloor(topfloor)
            'The Top of Stairwell 2' : {
              'down' : 'The Bottom of Stairwell 2',
              'south' : 'The Storage Room',
              'text' : 'topofstair2',
              },
            'The Storage Room' : {
              'north' : 'The Top of Stairwell 2',
              'south' : 'The Solar',
              'east' : 'The Study',
              'enemy' : 'possessed guard',
              'text' : 'storageroom'
              },
            'The Solar' : {
              'north' : 'The Storage Room',
              'south' : 'The King\'s Chamber',
              'east' : 'The Throne Room',
              'text' : 'solar'
              },
            'The Study' : {
              'south' : 'The Throne Room',
              'west' : 'The Storage Room',
              'text' : 'study'
              },
            'The Throne Room' : {
              'south' : 'The Wardrobe',
              'west' : 'The Solar',
              'north' : 'The Study',
              'enemy' : 'possessed guard',
              'text' : 'throneroom'
              },
            'The King\'s Chamber' : {
              'north' : 'The Solar',
              'east' : 'The Wardrobe',
              'south' : 'The Boudoir',
              'text' : 'kingschamber'
              },
            'The Wardrobe' : {
              'north' : 'The Throne Room',
              'south' : 'The Vault',
              'west' : 'The King\'s Chamber',
              'text' : 'wardrobe'
              },
            'The Boudoir' : {
              'north' : 'The King\'s Chamber',
              'east' : 'The Vault',
              'text' : 'boudoir'
              },
            'The Vault' : {
              'north' : 'The Wardrobe',
              'west' : 'The Boudoir',
              'east' : 'The Bottom of Stairwell 3',
              'enemy' : 'Possessed guard',
              'text' : 'vault'
              },
            'The Bottom of Stairwell 3' : {
              'up' : 'The Top of Stairwell 3',
              'west': 'The Vault',
              'text' : 'bottomofstair3',
              },
            'The Top of Stairwell 3' : {
              'north' : 'The Lookout',
              'down' : 'The Bottom of Stairwell 3',
              'text' : 'topofstair3',
              },
            'The Lookout' : {
              'south' : 'The Top of Stairwell 3',
              'text' : 'lookout',
              'enemy' : 'wizard',
              }
              
                  

         
}
#restart = 'yes'
#while restart == 'yes':
 # inventory = []
  #currentRoom = 'Your Home'
  #gamemap = {

  #}

#start the player in the Hall
currentRoom = 'Your Home'

#displays game intructions and the storyline at the beggining of the game
showInstructions()
#ask user for their name which will be implemented throughout the game
username = input('Hello there! What is your name? ')
print ('Perfect, ' + username + ', your journey starts now!')

#sets coins and health
coins = 0
health = 100

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':  
    move = input('>')
    
  move = move.lower().split()
  #if the user types help, the commands will be displayed
  if move[0] == 'help':
    print('''
================
Commands:
  go [direction: north, south, east, west, up, down]
  run [direction: north, south, east, west] (allows you a 40% chance of escaping a sticky situation)
  buy [item]
  use [item]
  attack
  yes
  no
  help (will repeat these commands at any point and time in the game)
================

''')

  #health
  if health > 100:
    health = 100
  #if the user's health reaches 0
  if health <= 0:
    #if the user has a potion, they can revive themselves
    if 'potion' in inventory :
      usepotion = input('Your health has been depleted to 0 health points, would you like to use your health potion to revive yourself? ')
      if usepotion == 'yes':
        inventory.remove('potion')
        health = 100
    #if the user does not have the healing potion that they can pick up at the trading post, they will die
    if 'potion' not in inventory:
      print('Oh no! Unfortunately, the enemy got the best of you.')
      print('GAME OVER...')
    break
  #if the user's health is depleted to less than 20 health points, they will be asked if they want to use bread if they have it
  if health < 20 and 'bread' in inventory :
    usebread = input('Your health has been depleted to less than 20 health poins, would you like to eat some bread to replenish your health by 50 health points? ')
    if usebread == 'yes':
      inventory.remove('bread')
      #bread will give users 50 health points
      health = health + 50
      print('You gained 50 health points!')
  #if the user's health is depleted to less than 20 health points, they will be asked if they would like to use meat to extend their health to 200 health points
  if health < 20 and 'meat' in inventory :
    usemeat = input('Your health has been depleted to less than 20 health poins, would you like to eat some meat to expand and restore your health to 200 health points? ')
    if usemeat == 'yes':
      inventory.remove('meat')
      health = 200
      print('You ate some meat to restore your health to 200 health points!')
  
  #coins
  if coins < 0:
    coins = 0
    


  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in gamemap[currentRoom]:
      #set the current room to the new room
      currentRoom = gamemap[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')
        print('')


  #user fights monsters in different areas of game
        
  #forest thieves
  if 'enemy' in gamemap[currentRoom] and 'thief' in gamemap[currentRoom]['enemy']:
    if move[0] == 'go':
      #the theif's health is set to 15 health points and the user is warned of the theif
      thealth = 15
      print('Oh no! There is a thief blocking your path! Attack the thief to defeat him! An axe would work great if you have one!')
      print('If you "run [direction]" now, you may be able to lose the thief!')
      print('')
      print('Enemy Health:', thealth)
    #while the enemy is alive this process will take place
    while thealth > 0:
      #takes in user input
      move = ''
      while move == '':  
        move = input('>')
      move = move.lower().split()
      
      #user chooses to run past thief instead of fighting them
      if move[0] == 'run' and 'enemy' in gamemap[currentRoom] and 'thief' in gamemap[currentRoom]['enemy']:
        #if the user chooses to run, they will have a 40% of making it past the enemy successfully
        skip = random.choice(chance)
        if skip <= 1:
          if move[1] in gamemap[currentRoom]:
            currentRoom = gamemap[currentRoom][move[1]]
          thealth = -1
        if skip > 1:
          health = health - 10
          coins = coins - 3
          if coins < 0:
            coins = 0
          if move[1] in gamemap[currentRoom]:
              currentRoom = gamemap[currentRoom][move[1]]  
          thealth = -2

      #user chooses to leave the room using 'go' command
      #if they type 'go' first
      if move[0] == 'go' and 'enemy' in gamemap[currentRoom] and 'thief' in gamemap[currentRoom]['enemy']:
        #check that they are allowed wherever they want to go
        if move[1] in gamemap[currentRoom]:
          #set the current room to the new room
          currentRoom = gamemap[currentRoom][move[1]]
          health = health - 15
          coins = 0
          thealth = -3
        #there is no door (link) to the new room
        else:
            print('You can\'t go that way!')
      
            
      #if user fights without items
      if move[0] == 'attack' and 'axe' not in inventory:
        print('You have attacked the thief!')
        #user's normal attack does 3 damage
        thealth = thealth - 3
        print('Enemy Health:', thealth)
        print('')
        if thealth > 0:
          print('The thief has attacked you!')
          #if the user has a shield, they will take 
          if 'shield' in inventory:
            health = health - 1
          else:
            health = health - 3
          print('Your Health:', health)
          
      #if the user has an axe in their inventory the damage they give will be increased
      if move[0] == 'attack' and 'axe' in inventory :
        print('You have attacked the thief!')
        #if the user has an axe they will do 5 damage
        thealth = thealth - 5
        print('Enemy Health:', thealth)
        print('')
        if thealth > 0:        
          print('The thief has attacked you!')
        #if the user has a shield in their inventory the damage taken will be reduced
          if 'shield' in inventory:
            health = health - 1
          else:
            health = health - 3
          print('Your Health:', health)

      #if user uses a stem of sage on the enemy
      if move[0] == 'attack' and 'sage' in inventory:
        print('')
        usesage = input('You have some sage in your inventory, would you like to use it to put them to sleep? ')
        #if the user has sage, they can put the enemy to sleep
        if usesage == 'yes':
          inventory.remove('sage')
          print('You put the enemy to sleep.')
          thealth = 0
        if usesage == 'no':
          thealth = 15
      #if the user's health reaches 0
      if health <= 0:
        #if the user has a potion, they can revive themselves
        if 'potion' in inventory :
          usepotion = input('Your health has been depleted to 0 health points, would you like to use your health potion to revive yourself? ')
          if usepotion == 'yes':
            inventory.remove('potion')
            health = 100
        #if the user does not have the healing potion that they can pick up at the trading post, they will die
        if 'potion' not in inventory:
          print('Oh no! Unfortunately, the enemy got the best of you.')
          print('GAME OVER...')
        break
        
    #this is the outcome if the user defeats the enemy, the enemy is deleted from the room
    if thealth == 0 or thealth < -3:
      del gamemap[currentRoom]['enemy']
      print('You have defeated the thief, good riddance!')
    #this is the outcome if the user is successful at running past the enemy
    if thealth == -1:
      print('You are very lucky! You sneaked past the thief without them seeing!')
    #this is the outcome if the user is not successful at running past the enemy
    if thealth == -2:
      print('The theif chased you down and you got mugged!')
      print('You lost 10 health points and 3 coins!')

    #if the user leaves the room by using "go" command
    if thealth == -3:
      print('The thief caught up to you and stole all your money! You can\'t expect the thief to let you go, ya dingus!')
      print('You lost 15 health points and all your coins.')
    


  #possessed castle guards
  if 'enemy' in gamemap[currentRoom] and 'possessed guard' in gamemap[currentRoom]['enemy']:
    if move[0] == 'go':
      #the guard's health is set to 20
      thealth = 20
      print('You have encountered one of the king\'s guards, maybe he can help you! Uh oh, looks like he was possessed! "attack" to defeat the guard. If you have one, use your handy axe. If you found it, use the enchanted sword, works like a charm. ')
      print('If you "run [direction]" now, you may be able to outrun the guard, his armour will weigh him down.')
      print('')
      print('Enemy Health:', thealth)
    #while the enemy is alive this process will take place  
    while thealth > 0:
      #takes in user input
      move = ''
      while move == '':  
        move = input('>')
      move = move.lower().split()
      
      #user chooses to run past thief instead of fighting them
      if move[0] == 'run' and 'enemy' in gamemap[currentRoom] and 'possessed guard' in gamemap[currentRoom]['enemy']:
        skip = random.choice(chance)
        if skip <= 1:
          if move[1] in gamemap[currentRoom]:
            currentRoom = gamemap[currentRoom][move[1]]
          thealth = -4
        if skip > 1:
          health = health - 15
          if move[1] in gamemap[currentRoom]:
              currentRoom = gamemap[currentRoom][move[1]]  
          thealth = -2

      #user chooses to leave the room using 'go' command
      #if they type 'go' first
      if move[0] == 'go' and 'enemy' in gamemap[currentRoom] and 'possessed guard' in gamemap[currentRoom]['enemy']:
        #check that they are allowed wherever they want to go
        if move[1] in gamemap[currentRoom]:
          #set the current room to the new room
          currentRoom = gamemap[currentRoom][move[1]]
          health = health - 20
          thealth = -3
        #there is no door (link) to the new room
        else:
            print('You can\'t go that way!')
      
            
      #if user fights without items
      if move[0] == 'attack' and 'axe' not in inventory:
        print('You have attacked the guard!')
        thealth = thealth - 3
        print('Enemy Health:', thealth)
        print('')
        if thealth > 0:
          print('The guard has attacked you!')
          if 'shield' in inventory:
            health = health - 3
          else:
            health = health - 5
          print('Your Health:', health)
          
      #if the user has an axe in their inventory the damage they give will be increased
      if move[0] == 'attack' and 'axe' in inventory :
        print('You have attacked the guard!')
        thealth = thealth - 5
        print('Enemy Health:', thealth)
        print('')
        if thealth > 0:        
          print('The guard has attacked you!')
        #if the user has a shield in their inventory the damage taken will be reduced
          if 'shield' in inventory:
            health = health - 3
          else:
            health = health - 5
          print('Your Health:', health)
          
      #if the user's health reaches 0
      if health <= 0:
        #if the user has a potion, they can revive themselves
        if 'potion' in inventory :
          usepotion = input('Your health has been depleted to 0 health points, would you like to use your health potion to revive yourself? ')
          if usepotion == 'yes':
            inventory.remove('potion')
            health = 100
        #if the user does not have the healing potion that they can pick up at the trading post, they will die
        if 'potion' not in inventory:
          print('Oh no! Unfortunately, the enemy got the best of you.')
          print('GAME OVER...')
        break
      
      #if user uses a stem of sage on the enemy
      if move[0] == 'attack' and 'sage' in inventory:
        print('')
        usesage = input('You have some sage in your inventory, would you like to use it to put them to sleep? ')
        if usesage == 'yes':
          inventory.remove('sage')
          print('You put the enemy to sleep.')
          thealth = 0
        if usesage == 'no':
          thealth = 15
        

    if thealth == 0 or thealth == -1 or thealth < -4:
      del gamemap[currentRoom]['enemy']
      print('You have defeated the guard, good riddance!')

    if thealth == -4:
      print('You are very lucky! You sneaked past the guard without them seeing!')

    if thealth == -2:
      print('The guard chased you down and hit you with the hilt of his sword!')
      print('You lost 15 health points!')

    if thealth == -3:
      print('The guard stopped you in your path and you suffered some serious damage. Don\'t walk away from a battle ya dingus!')
      print('You lost 20 health points.')


  #your home
  if 'text' in gamemap[currentRoom] and 'yourhome' in gamemap[currentRoom]['text']:
    if move[0] == 'go':
      print('You are back at your home.')
      hnewsletter = input('Would you like to read the newsletter again? ')
      if hnewsletter == 'yes':
        print('''
  “THE CREST OF VEIL
  Sometime during the night, the town’s most valuable possessions, the ‘Fergle Plants’ were stolen from the royal garden by a malevolent wizard. He has since taken over the tower and is taking pleasure in starving the town. The king has sent out all of his most skilled kingsmen soon after the incident to retrieve the ‘Fergle Plants’ and defeat the beast, but none of them have returned since. The King has announced a huge reward to whoever can get to the castle tower, defeat the wizard, and save the vital plants to save the town.”
''')
      
  #Leif's home
  if 'text' in gamemap[currentRoom] and 'leifshome' in gamemap[currentRoom]['text']:
    if move[0] == 'go':
      leif = input('You arrive at Leif\'s house, knock on his door? ')
      if leif == 'yes':
        print('Hey, ' + username + '! A quest you say? You’re going to need some supplies on your journey. Have you stopped by The Trading Post today? I heard they had some awesome trades today.')

  #Sally's Home
  if 'text' in gamemap[currentRoom] and 'sallyshome' in gamemap[currentRoom]['text']:
    if move[0] == 'go':
      print('DOOR SIGN: "Out to lunch, stop by later."')
      package = input('There is a package on her doorstep, open it? ')
      if package == 'yes':
        print('You get attacked by feral rats that took shelter in the package, serves you well!')
        print('You lost 5 health points')
        health = health - 5
      elif package == 'no':
        print('')
      else: 
        print('That\'s not a command, ya dingus.')


        
  #Christopher
  if 'text' in gamemap[currentRoom] and 'christophershome' in gamemap[currentRoom]['text']:
    if move[0] == 'go':
      chris = input('You arrive at Christopher\'s house, knock on his door? ')
      if chris == 'yes':
        print('Hello there ' + username + '! Have you gone to the bank to collect your daily interest? Many are making withdrawals before the economy collapses without our precious ‘Fergle Plants’ Oi! Go get yours before the stock runs out!!')

  #Esther's Home
  if 'text' in gamemap[currentRoom] and 'esthershome' in gamemap[currentRoom]['text']:
    if move[0] == 'go':
      esther = input('You arrive at Esther\'s house, knock on his door? ')
      if esther == 'yes':
        print(username + '! It’s so wonderful to see you in a time of distress.')

  #the library
  if 'text' in gamemap[currentRoom] and 'library' in gamemap[currentRoom]['text']:
    if move[0] == 'go':
      print('You enter the library and see three people: the Librarian, a strange poet, and another townsperson.')
      #asks user if they want to speak with The Odd Poet
      oddpoet = input ('Would you like to speak to the odd poet in the corner? ')
      if oddpoet == 'yes':
        print('oooooooh oooooooh oooooooooooh. -There once was a witch-.. wowza -who lived in a ditch-.. awwwww -Had a velvet blue cat,- BLUE? -but not long after that. It died from an itch.- Such a shame. Poor cat never had a chance. The… The.. The Unrich Witch! That’s the name. What a lovely poem….')
        print('')
      #asks user if they want to speak with one of the townspeople
      townsperson3 = input('Would you like to speak to the townsman sitting at the table? ')
      if townsperson3 == 'yes':
        print('Can I help you? That\'s what I thought, now git!')
        print('')
      ##asks user if they want to speak with The Librarian
      librarian = input('Would you like to speak to the Librarian? ')
      if librarian == 'yes':
        print('Don’t waste too much of your time socializing my dearest, some of the villagers are more informative than not. Books yield more information anyway.')
        print('')
        
  #The cobbler's den
  if 'text' in gamemap[currentRoom] and 'cobblersden' in gamemap[currentRoom]['text']:
    if move[0] == 'go':
      shoes = ('Why hello there! Those shoes of yours are looking a little rough, what do you say you invest in a new pair eh? These shoes are all new and improved, with the most durable sole on the market! Would you like me to go in the back and get some pairs for you to try on? ')
      if shoes == 'yes':
        coins = coins + 1
        print('Yay! You earned a coin for trying on some shoes.')
        
  #the bank
  if 'text' in gamemap[currentRoom] and 'bank' in gamemap[currentRoom]['text']:
    if move[0] == 'go':
      banker = input('You enter the bank and approach Marcus the banker at the desk. Speak with him? ')
      if banker =='yes':
        income = input('Hello, let me guess, you’re here for your daily income of 10 coins, correct? ')
        if income == 'yes' :
          coins = coins + 10
          print('Take your coins and be on your way, I got filing to do! Now scatter!')
          print('You collected 10 coins!')
          del gamemap[currentRoom]['text']

        
  #the well
  if 'text' in gamemap[currentRoom] and 'well' in gamemap[currentRoom]['text']:
    if move[0] == 'go':
      print('At the town\'s Well you see that there are many people in deep discussions.')
      print('')
      historian = input('Would you like to speak to The Town\'s Historian? ')
      if historian == 'yes':
        print('Oh hello ' + username +'. Sorry, I’m in a bit of a slump. In all the years that Veil has been in the running, we have never ever let such a traumatic incident happen. Oh wow, I am stressed…')
        print('')
      townsperson1 = input('Would you like to speak to one of the townspeople? ')
      if townsperson1 == 'yes':
        print(username + '! Oh ' + username + '!! Have you checked out The Tavern lately?? I just came from…. The Tavern! Have you been? I had a wonderf…. wonder.. hey I wonder how many townsmen can fit in The Tavern.')
        print('')
        
  if 'moneyman' in gamemap[currentRoom] and 'man' in gamemap[currentRoom]['moneyman']:
    if move[0] == 'go':
      print('')
      mysteriousman1 = input('A mysterious man is gesturing for you to come over to him, do you trust him? ')
      if mysteriousman1 == 'yes':
        print('Psst. Hey you. Are you in the market for a game changer? Find a dark place with holes. Good luck my friend.')
        print('The man places 4 coins in your hands.')
        print('')
        coins = coins + 4
        del gamemap[currentRoom]['moneyman']
        
  #The bakery
  if 'text' in gamemap[currentRoom] and 'bakery' in gamemap[currentRoom]['text']:
    if move[0] == 'go':
      foodprompt = input('Hello! How may I help you today? We have baked a fresh variety of many goods, from bread to pastries. Would you like to purchase some goods for your journey? ')
      print('')
  
      if foodprompt == 'yes': 
        print('''
In store today we have:

a loaf of bread: 4 coins - this will add 50 health points

a slab of meat: 7 coins - this will extend and fill your health to 200 health points

''')
        #asks if user wants to make a purchase
        buyfood = input('Would you like to make a purchase? Use buy command and name of item to purchase. (ex. buy a slab of meat) ')
        #if user wants to buy a loaf of bread, they can purchase it as many times as they want if they have enough coins
        if buyfood == 'buy a loaf of bread':
          if coins >= 4:   
            inventory += ['bread']
            coins = coins - 4
            print('You purchased a loaf of bread!')
          else:
            print('You do not have enough coins to make this purchase')
        #if user wants to buy a slab of meat, they can purchase it as many times as they want if they have enough coins
        elif buyfood == 'buy a slab of meat':
          if coins >= 7:   
            inventory += ['meat']
            coins = coins - 7
            print('You purchased a slab of meat!')
          else:
            print('You do not have enough coins to make this purchase')
        
      
  #The apothecary
  if 'text' in gamemap[currentRoom] and 'apothecary' in gamemap[currentRoom]['text']:
    if move[0] == 'go':
      print('Good Morrow young fiddlestick, how do you do? Are you in the market for twigfire? Glabberstem? lynneberries?')
      print('')
      apothecary = input('Would you like to shop the market today? ')
      if apothecary == 'yes': 
        print('''
In store today we have:

a stem of sage: 2 coins - this will put any enemy (besides the wizard) you encounter to sleep

a crystal: 3 coins - this holds the magic of a thousand universes

a lantern: 12 coins - this will help you in the dark times

''')
        #if user wants to buy a stem of sage, they can purchase it as many times as they want if they have enough coins
        apothbuy = input('Would you like to make a purchase? Use buy command and name of item to purchase. (ex. buy a stem of sage) ')
        if apothbuy == 'buy a stem of sage':
          if coins >= 2:   
            inventory += ['sage']
            coins = coins - 2
            print('You purchased a stem of sage!')
          else:
            print('You do not have enough coins to make this purchase')
        #if user wants to buy a crystal, they can purchase it as many times as they want if they have enough coins
        elif apothbuy == 'buy a crystal':
          if coins >= 3:   
            inventory += ['crystal']
            coins = coins - 3
            print('You purchased a crystal!')
          else:
            print('You do not have enough coins to make this purchase')
        #if user wants to buy a crystal, they can purchase it as many times as they want if they have enough coins 
        elif apothbuy == 'buy a lantern':
          if coins >= 12:   
            inventory += ['lantern']
            coins = coins - 12
            print('You purchased a lantern!')
          else:
            print('You do not have enough coins to make this purchase')
         
          
  #The postal office
  if 'text' in gamemap[currentRoom] and 'postaloffice' in gamemap[currentRoom]['text']:
    if move[0] == 'go':
      print('The Postal Office is closed.')
      #the user can read the newspaper from the very beginning again
      wallpost = input('There is a newsletter attached to the wall, would you like to read it?')
      if wallpost == 'yes':
        print('''
  “THE CREST OF VEIL
  Sometime during the night, the town’s most valuable possessions, the ‘Fergle Plants’ were stolen from the royal garden by a malevolent wizard. He has since taken over the tower and is taking pleasure in starving the town. The king has sent out all of his most skilled kingsmen soon after the incident to retrieve the ‘Fergle Plants’ and defeat the beast, but none of them have returned since. The King has announced a huge reward to whoever can get to the castle tower, defeat the wizard, and save the vital plants to save the town.”

You feel something wrapped in the newsletter, you take the newsletter off the wall and a coin falls out. It's your lucky day!
''')
        #this coin farm is unlimited so you can keep coming back to this room for unlimited coins
        coins = coins + 1
        
  #The fortune teller tent
  if 'text' in gamemap[currentRoom] and 'fortunetllerstent' in gamemap[currentRoom]['text']:
    if move[0] == 'go':
      reading = input('Welcome to my tent deary. Would you like to get a reading? ')
      if reading == 'yes':
        print('I see that you are headed off towards the castle to fight the wizard. You see no risk in that. Well my deary, beware of the guards in the castle, the wizard possessed all the remaining castle residents after the King managed to escape with his guards. Another thing! Be careful when deciding what items you choose to bring on your adventure! That’s all I’m going to say. Hmmmm, the universe is still very indecisive of your future young one!')
        
  #the church
  if 'text' in gamemap[currentRoom] and 'church' in gamemap[currentRoom]['text']:
    if move[0] == 'go':
      print('You step into the Church and no one is present')
      pray = input('Would you like to pray? ')
      #if the user chooses to pray, they'll get 2 coins. we aren't endorsing religion pls don't sue.
      if pray == 'yes':
        print('2 coins appear on the stairs.')
        coins = coins + 2
        #the user isn't allowed to 
        del gamemap[currentRoom]['text']
        
  #townhall
  if 'text' in gamemap[currentRoom] and 'townhall' in gamemap[currentRoom]['text']:
    if move[0] == 'go':
      print('You walk into town hall and see The Lord and Lady talking to the secretary.')
    secretary = input('Would you like to speak to the Secretary? ')
    if secretary == 'yes':
      print('Why look who it is. You know the town has been ranting and raving about you? Everyone is shocked that YOU have taken the initiative to save our town!')
      print('')
    lord = input('Would you like to speak to The Lord? ')
    if lord == 'yes':
      print('It seems you are ready to endeavour on this journey. All I can say is that you are a very brave young soul, that is for certain! I can assure you that if you return, I will make sure you are set for life, for having saved my town.')
      print('')
    lordswife = input('Would you like to speak to The Lady? ')
    if lordswife == 'yes' :
      print('What’s that you say? You’re headed to the castle? Oh dear god that is madness! Please, do not leave.. I can’t afford to see another young one like you disappear!')
      print('')
      
  #The masonry
  if 'text' in gamemap[currentRoom] and 'masonry' in gamemap[currentRoom]['text']:
    if move[0] == 'go':
      mason = input('You enter the Masonry and see the mason hard at work. Would you like to speak to the mason? ')
      if mason == 'yes':

        print('Hey kid. One piece of advice. Find the enchanted sword. The power it holds is essential to stand a chance against the oppressive wizard.')

  #the inn
  if 'text' in gamemap[currentRoom] and 'inn' in gamemap[currentRoom]['text']:
    if move[0] == 'go':
      clerk = input('You see a frustrated clerk at the front desk. Would you like to speak to her? ')
      if clerk == 'yes':
        fat = input('Hello there. Ugh I feel fat today. Do I look okay today? ')
        if fat == 'yes' :
          coins = coins + 1
          print('Awh you\'re such a sweetheart! Here\'s a coin.')
          del gamemap[currentRoom]['text']
        if fat == 'no':
          health = health - 5
          print('How rude! she says as you slaps you. You lost 5 health points.')
        
  #the trading post
  if 'text' in gamemap[currentRoom] and 'tradingpost' in gamemap[currentRoom]['text']:
    if move[0] == 'go':
      #when the user enters the room for the very first time, they will be allowed to pick an item from the shop for free
      if 'axe' in gamemap[currentRoom] and 'potion' in gamemap[currentRoom] and 'shield' in gamemap[currentRoom]:
        print('Ahh, good morning young feller! Nice to see a bright face on this tragic day, oh I hope none of this kidnapping business affects my traffic flow, I simply cannot afford to let that happen! On the journey to save the kingdom you say? That is one big quest for a small feller like you.. You know, this might actually be a wondrous idea! Maybe once this whole thing is over, my adoring customers will return to their favourite stop. Say, I think you need a helping hand if you want to slay this wizard.')
        print('')
        print(''' Please choose any item of mine, on the house!
Options:

an axe: 10 coins - this will increase the damage you give to enemies
a shield: 10 coins - this will reduce the damage you take
a healing potion: 10 coins - this will restore your health to 100 health points if your health ever falls below 20 health points

To select your item type 'grab [item]'
Ex. grab an axe ''')
      
        free = input('Please feel free to grab an item. ')
        #if they choose to grab the axe, the axe will be added to the user's inventory
        if free == 'grab an axe':
          if 'axe' in gamemap[currentRoom]:
            inventory += ['axe']
            del gamemap[currentRoom]['axe']
            print('')
            print('You picked the axe!')
            print('')
            print('')
        #if they choose to grab the shield, the shield will be added to the user's inventory  
        if free == 'grab a shield':
          if 'shield' in gamemap[currentRoom]:
            inventory += ['shield']
            del gamemap[currentRoom]['shield']
            print('')
            print('You picked the shield!')
            print('')
            print('')
           #if they choose to grab the healing potion, the healing potion will be added to the user's inventory 
        if free == 'grab a healing potion':
          if 'potion' in gamemap[currentRoom]:
            inventory += ['potion']
            del gamemap[currentRoom]['potion']
            print('')
            print('You picked the healing potion!')
            print('')
            print('')  
           
      print('''If you would like to purchase one of the other items please type:
"buy [item]"
Ex. buy an axe

However it will not be free this time!

''')
      #the users are then asked if they would like to purchase another item
      buying = input('Would you like to purchase one of the other items? ')     
      if buying =='yes':
        tpbuy = input('State which item you would like to buy. ') 
        if tpbuy == 'buy an axe':
          #they can only buy this item if they have enough coins
          if coins >= 10:
            #they can only buy the item once, so after they buy it, it is deleted from the room
            if 'axe' in gamemap[currentRoom]:
              inventory += ['axe']
              del gamemap[currentRoom]['axe']
              coins = coins - 10
              print('')
              print('You purchased an axe!')
              print('')
            else:
              print('')
              print('Sorry! We are currently sold out of axes.')
              print('')
          else:
            print('')
            print('You do not have enough coins to make this purchase')
            print('')
            
        elif tpbuy == 'buy a shield':
          #they can only buy this item if they have enough coins
          if coins >= 10:
            #they can only buy the item once, so after they buy it, it is deleted from the room
            if 'shield' in gamemap[currentRoom]:
              inventory += ['shield']
              del gamemap[currentRoom]['shield']
              coins = coins - 10
              print('')
              print('You purchased a shield!')
              print('')
            else:
              print('')
              print('Sorry! We are currently sold out of shields.')
              print('')
          else:
            print('')
            print('You do not have enough coins to make this purchase')
            print('')
            
        elif tpbuy == 'buy a healing potion':
          #they can only buy this item if they have enough coins
          if coins >= 10:
            #they can only get the item once, so after they buy it, it is deleted from the room
            if 'potion' in gamemap[currentRoom]:
              inventory += ['potion']
              del gamemap[currentRoom]['potion']
              coins = coins - 10
              print('')
              print('You purchased a healing potion!')
              print('')
            else:
              print('')
              print('Sorry! We are currently sold out of healing potions.')
              print('')
          else:
            print('')
            print('You do not have enough coins to make this purchase')
            print('')

      #this is the process if the user is coming into the room for a secod time
      if 'axe' in gamemap[currentRoom] and 'potion' in gamemap[currentRoom] or 'axe' in gamemap[currentRoom] and 'shield' in gamemap[currentRoom] or 'potion' in gamemap[currentRoom] and 'shield' in gamemap[currentRoom] or 'axe' in gamemap[currentRoom] or 'shield' in gamemap[currentRoom] or 'potion' in gamemap[currentRoom]:
        print('Ahh welcome back young traveller. Looking to make a purchase? I\'m running low on some things, but feel free to take a look.')
        print('')
        #it'll tell the user what's in stock based off the items left in the room
        print('In stock we have:')
        if 'axe' in gamemap[currentRoom]:
          print('an axe: 10 coins - this will increase the damage you give to enemies')
        if 'shield' in gamemap[currentRoom]:
          print('a shield: 10 coins - this will reduce the damage you take')
        if 'potion' in gamemap[currentRoom]:
          print('a healing potion: 10 coins - this will restore your health to 100 health points if your health ever falls below 20 health points')
        #asks user if they want to purchase an item.
        buying = input('Would you like to purchase one of the other items? ')     
        if buying =='yes':
          print('')
          tpbuy = input('State which item you would like to buy. ')
          #users can only buy items if they do not have it yet
          if tpbuy == 'buy an axe':
            if coins >= 10:
              if 'axe' in gamemap[currentRoom]:
                inventory += ['axe']
                del gamemap[currentRoom]['axe']
                coins = coins - 10
                print('')
                print('You purchased an axe!')
                print('')
              else:
                print('')
                print('Sorry! We are currently sold out of axes.')
                print('')
            else:
              print('')
              print('You do not have enough coins to make this purchase')
              print('')
              
          elif tpbuy == 'buy a shield':
            if coins >= 10:
              if 'shield' in gamemap[currentRoom]:
                inventory += ['shield']
                del gamemap[currentRoom]['shield']
                coins = coins - 10
                print('')
                print('You purchased a shield!')
                print('')
              else:
                print('')
                print('Sorry! We are currently sold out of shields.')
                print('')
            else:
              print('')
              print('You do not have enough coins to make this purchase')
              print('')
              
          elif tpbuy == 'buy a healing potion':
            if coins >= 10:
              if 'potion' in gamemap[currentRoom]:
                inventory += ['potion']
                del gamemap[currentRoom]['potion']
                coins = coins - 10
                print('')
                print('You purchased a healing potion!')
                print('')
              else:
                print('')
                print('Sorry! We are currently sold out of healing potions.')
                print('')
            else:
              print('')
              print('You do not have enough coins to make this purchase')
              print('')
        


  #The tavern
  if 'text' in gamemap[currentRoom] and 'tavern' in gamemap[currentRoom]['text']:
    if move[0] == 'go':
      #program will prompt user if they want to talk to any of the following 3 people
      print('You walk into the Tavern. It is dim and dusty. You see a drunk sitting at the tabletop, another townsperson, and the bartender.')
      drunk = input('Would you like to speak to the Old Muddled Drunk? ')
      if drunk == 'yes':
        print('Do you get to the cloud district very often? Oh, what am I saying - of course you don\'t.')
        print('')
      townsperson2 = input('Would you like to speak to the other townsperson? ')
      if townsperson2 == 'yes':
        print('It’s getting hard to see the birds outside.')
        print('')
      bartender = input('Would you like to speak to the bartender? ')
      if bartender == 'yes' :
        print('Lemme guess… you\'re here to drink your sorrows away like the rest of the people in this dump eh?')
        print('')
        
  #forest entry
  if 'text' in gamemap[currentRoom] and 'forestentry' in gamemap[currentRoom]['text']:
    if move[0] == 'go':
      friend = input('You see a frantic friend of yours in the distance. Talk to them? ')
      if friend == 'yes':
        print(username + '! I heard you are on your way to the castle. I have to warn you, and please listen. DO NOT. I REPEAT DO NOT LEAVE A ROOM WITH AN ENEMY IN IT OR THINGS COULD GET UGLY.')
        print('')
  #the forest

  #shabby leaves
  if 'text' in gamemap[currentRoom] and 'shabbyleaves' in gamemap[currentRoom]['text']:
    if move[0] == 'go':
      print('')

  #The mystic pond
  if 'text' in gamemap[currentRoom] and 'mysticpond' in gamemap[currentRoom]['text']:
    if move[0] == 'go':
      print('There is nothing here. Turn back now.')

  #Dobson\'s fork
  if 'text' in gamemap[currentRoom] and 'dobsonsfork' in gamemap[currentRoom]['text']:
    if move[0] == 'go':
      print('You arrive at dobson’s fork, and to the east is the entrance to the caves! A sign is placed at the turnoff warning all who enter: “BEWARE PEOPLE WHO ENTER THE CAVES NEVER COME OUT!You should probably take the west path straight to the castle!')

  #The knight's pathway
  if 'text' in gamemap[currentRoom] and 'knightspathway' in gamemap[currentRoom]['text']:
    if move[0] == 'go':
      for i in range(3):
        print('Oh young warrior...')
      print('You have chosen the courageous knight’s pathway. Only brave souls like yourself are deemed worthy of this route, you should feel proud!')
      

  #castle landing
  if 'text' in gamemap[currentRoom] and 'castlelanding' in gamemap[currentRoom]['text']:
    if move[0] == 'go':
      print('You have reached the Castle Landing.')

  #the cave entrance
  if 'text' in gamemap[currentRoom] and 'caveentrance' in gamemap[currentRoom]['text']:
    if move[0] == 'go':
      print('DO NOT PASS! Your path is blocked, turn back and continue your journey!')
      
      
  #castle

  #dungeon
  #dungeon hallway 1
  if 'text' in gamemap[currentRoom] and 'dungeonhallway1' in gamemap[currentRoom]['text']:
    if move[0] == 'go':
      print('You explore the first hallway to the dark and gloomy dungeon.')
      print('From a prisoner in the cell "Help me please!!!! I will do anything, I say. ANYTHING! I don’t deserve this, all my life, I’ve been loyal to the crown!"')

  #dungeon hallway 2
  if 'text' in gamemap[currentRoom] and 'dungeonhallway2' in gamemap[currentRoom]['text']:
    if move[0] == 'go':
      #the sword needed to have a good chance of defeating the wizard is in this room
      sword = input('You see a special enchanted sword! Would you like to pick it up? ')
      if sword == 'yes':
        inventory += ['sword']
        del gamemap[currentRoom]['sword']
        print('You have picked up the enchanted sword')
      print('"Pssst. Hey you." You look over to the prisoner in the cell. "Hey. I am Lord Hilton’s son from across the river. I can assure you that if you get me out of here there is a hefty reward in it for you!"')
      prisoner = input('Let him out? ')
      if prisoner == 'yes':
        health = health - 5
        print('You lost 5 health points for letting a serial killer out of their cell.')
        

  #lavatories
  if 'text' in gamemap[currentRoom] and 'lavatories' in gamemap[currentRoom]['text']:
    if move[0] == 'go':
      print('Yuck! You mistakenly found the lavatories. You should continue to search the castle to save yourself from the horrific smell!')
      

  #place of arms
  if 'text' in gamemap[currentRoom] and 'placeofarms' in gamemap[currentRoom]['text']:
    if move[0] == 'go':
      print('You stumble into the place of arms where you see stack after stack of weapons, swords, blades, bows, and arrows.')
      

  #servants quarters
  if 'text' in gamemap[currentRoom] and 'servantsquarter' in gamemap[currentRoom]['text']:
    if move[0] == 'go':
      print('You have encountered the biggest rat you have ever seen!')
      

  #gatehouse
  if 'text' in gamemap[currentRoom] and 'gatehouse' in gamemap[currentRoom]['text']:
    if move[0] == 'go':
      print('You are in the gatehouse to the castle, which opens out onto the castle landing. But oh no! A possessed guard has spotted you from a distance! You better defeat them, or figure out an escape plan, and quick, he\’s heading your way!')

  #kitchen
  if 'text' in gamemap[currentRoom] and 'kitchen' in gamemap[currentRoom]['text']:
    if move[0] == 'go':
      print('Great! Another rat! And it looks like he snacking on the chef\’s 3-day old pot of stew!')


  #greathall
  if 'text' in gamemap[currentRoom] and 'greathall' in gamemap[currentRoom]['text']:
    if move[0] == 'go':
      print('You try your hardest to avoid the shattered glass scattered around the floor of the great hall. Knives are stabbed in walls, and the dining table is cracked down the middle. It looks like whoever was here didn/’t go down without a fight!')
      

  #buttery
  if 'text' in gamemap[currentRoom] and 'buttery' in gamemap[currentRoom]['text']:
    if move[0] == 'go':
      print('Stacks and stacks of barrels full of wine and beer line the walls. A small section has spilled onto the floor! You are careful not to slip on the red wine! Or is it blood!?!')


  #storage room
  if 'text' in gamemap[currentRoom] and 'storageroom' in gamemap[currentRoom]['text']:
    if move[0] == 'go':
      print('What a mess! This storage room is packed with brooms, bed linens, towels and much more!')
      

  #the study
  if 'text' in gamemap[currentRoom] and 'study' in gamemap[currentRoom]['text']:
    if move[0] == 'go':
      print('Looks like the king left in a hurry, thousands of documents litter the floor of his study!')

  #solar
  if 'text' in gamemap[currentRoom] and 'solar' in gamemap[currentRoom]['text']:
    if move[0] == 'go':
      print('Finally a room that has not been raided and destroyed!') 

  #throne room
  if 'text' in gamemap[currentRoom] and 'throneroom' in gamemap[currentRoom]['text']:
    if move[0] == 'go':
      print('What a grand room. Vaulted ceilings, red and blue decor, and an silk carpet leading up the steps to a solid gold throne! This king lives in style!')
      

  #kingschamber
  if 'text' in gamemap[currentRoom] and 'kingschamber' in gamemap[currentRoom]['text']:
    if move[0] == 'go':
      print('You stumble into the king’s private bedchambers.')

  #wardrobe
  if 'text' in gamemap[currentRoom] and 'wardrobe' in gamemap[currentRoom]['text']:
    if move[0] == 'go':
      print('You can’t believe the clothes the king and queen own! From fine silks, to lavish fur pelts. They have it all!')
      

  #boudoir
  if 'text' in gamemap[currentRoom] and 'boudoir' in gamemap[currentRoom]['text']:
    if move[0] == 'go':
      print('Why the queen is sure spoiled! Her boudoir is filled with the finest jewels, shoes, and salon items!')
      

  #vault
  if 'text' in gamemap[currentRoom] and 'vault' in gamemap[currentRoom]['text']:
    if move[0] == 'go':
      chest = input('There is a treasure chest is in this room, would you like to open it? ')
      if chest == 'yes':
        coins = coins + 10
        print('Wow you found 10 coins in the chest! Nice!')
        del gamemap[currentRoom]['text'] 



  #top of stairwell 3
  if 'text' in gamemap[currentRoom] and 'topofstair3' in gamemap[currentRoom]['text']:
    if move[0] == 'go':
      print('A guard appears, but he is not like the other ones you have fought. He seems to be in a trance but different from the possessed guards. "You there. I cannot let you pass. The only way I will let you pass is if you answer this riddle. ')
      riddle = input('Answer me this. What colour was the cat in the old tale of “The Lone Witch”? ')
      if riddle == 'blue':
        health = health + 50
        print('Correct! You received 50 bonus health points.')
      
        
  #lookout
  if 'text' in gamemap[currentRoom] and 'lookout' in gamemap[currentRoom]['text']:
    if move[0] == 'go':
      print('Finally, you’ve reached the top of the tower. Across the lookout the wizard whirls to see you standing there, not knowing what to do next. He says: “Why why why, honestly I thought you wouldn\'t make it through the forest, but you did! That does not matter now, for you have no chance at beating me! I hold the key to your whole kingdom!')
      wizard = input('This is your last chance to turn back. Type "attack" to fight the wizard. ')
      if wizard == 'attack':
        print('The battle begins.')
        print('')
        if 'enemy' in gamemap[currentRoom] and 'wizard' in gamemap[currentRoom]['enemy']:
          thealth = 300
          print('"You think you you can defeat me in a battle? I don\'t think so youngling" he spits at you. ')
          print('Attack the wizard to defeat him! The enchanted sword would work great if you have one!')
          print('Only flee the battle if you can tolerate a significant hit.')
          print('')
          print('Enemy Health:', thealth)
           
          while thealth > 0:
            #takes in user input
            move = ''
            while move == '':  
              move = input('>')
            move = move.lower().split()
            
            #user chooses to run past thief instead of fighting them
            if move[0] == 'run' and 'enemy' in gamemap[currentRoom] and 'wizard' in gamemap[currentRoom]['enemy']:
              health = health - 30
              print('As you ran out the door, the wizard shot a purple ball of fire. You got hit on the way out and took damages of 30 health points.')  
              if move[1] in gamemap[currentRoom]:
                  currentRoom = gamemap[currentRoom][move[1]]  
              thealth = -1

            #user chooses to leave the room using 'go' command
            #if they type 'go' first
            if move[0] == 'go' and 'enemy' in gamemap[currentRoom] and 'wizard' in gamemap[currentRoom]['enemy']:
              health = health - 30
              print('As you walked out the door, the wizard shot a purple ball of fire. You got hit on the way out and took damages of 30 health points.')  
              #check that they are allowed wherever they want to go
              if move[1] in gamemap[currentRoom]:
                  #moves user from one room to the next
                  currentRoom = gamemap[currentRoom][move[1]]  
                  thealth = -1
              #there is no door (link) to the new room
              else:
                  print('You can\'t go that way! There is no door there!!')
            
                  
            #if user fights without items, the odds are stacked against them and they will probably not live to see the light of
            if move[0] == 'attack' and 'axe' not in inventory and 'sword' not in inventory:
              print('You have attacked the wizard!')
              thealth = thealth - 2
              print('Enemy Health:', thealth)
              print('')
              #while
              if thealth > 0:
                print('The wizard has attacked you!')
                if 'shield' in inventory:
                  health = health - 1
                else:
                  health = health - 5
                print('Your Health:', health)
                
            #if the user has an axe in their inventory the damage they give will be increased
            if move[0] == 'attack' and 'axe' in inventory and 'sword' not in inventory:
              print('You have attacked the wizard!')
              thealth = thealth - 5
              print('Enemy Health:', thealth)
              print('')
              if thealth > 0:        
                print('The wizard has attacked you!')
              #if the user has a shield in their inventory the damage taken will be reduced
                if 'shield' in inventory:
                  health = health - 1
                else:
                  health = health - 5
                print('Your Health:', health)

            #if user is in possession of the enchanted sword
            if move[0] == 'attack' and 'axe' in inventory and 'sword' in inventory or move[0] == 'attack' and 'axe' not in inventory and 'sword' in inventory:
              print('Luckily, you found the enchanted sword! With this powerful item, you\'ll be able to defeat the wizard in no time!')
              print('You have attacked the wizard!')
              #user will only have to attack the wizard 3 times to win the game
              thealth = thealth - 100
              print('Enemy Health:', thealth)
              print('')
              #if wizard dies, the user will not get hit again.
              if thealth > 0:        
                print('The wizard has attacked you!')
              #if the user has a shield in their inventory the damage taken will be reduced
                if 'shield' in inventory:
                  health = health - 1
                else:
                  health = health - 5
                print('Your Health:', health)
            #if the user's health reaches 0
            if health <= 0:
              #if the user has a potion, they can revive themselves
              if 'potion' in inventory :
                usepotion = input('Your health has been depleted to 0 health points, would you like to use your health potion to revive yourself? ')
                if usepotion == 'yes':
                  inventory.remove('potion')
                  health = 100
              #if the user does not have the healing potion that they can pick up at the trading post, they will die
              if 'potion' not in inventory:
                print('Oh no! Unfortunately, the enemy got the best of you.')
                print('GAME OVER...')
              break
              
          #outcome if the user defeats the wizard
          if thealth == 0 or thealth < -1:
            del gamemap[currentRoom]['enemy']
            print('At last, you have defeated the wizard!')
            print('')
            print('CONGRATULATIONS You have saved the "Fergle Plants", and thus the kingdom! After defeating the wizard and completing the quest you are finally back at your small village just outside the kingdom. Upon your return the town praised you for your job well done. The King even had something to say: “I must admit, I didn’t think you’d return.” After a hard battle and journey all is well again in the kingdom of veil. Well done warrior!')
            print('')
            print('You beat the game! Thank you so much for playing, we hope you enjoyed yourself. Now, go, and have a good day, you deserve it!')
            print('')
            print('')
            print('Created by Taryn Wou and Madison Ciulla :D')
            break
          #if the user runs out of the room
          if thealth == -1:
            print('You sacrificed a lot by leaving, you better be preparing yourself to go battle him again. Remember, he restores his health while you are not in his presence.')

        


