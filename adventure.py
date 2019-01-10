#Python Text RPG
#Markus Tousant

import cmd
import textwrap
import sys
import os
import time
import random



screenWidth = 100

##### Player Setup ####
class player:
    def __init__(self):
        self.name = ''
        self.job = ''
        self.hp = 0
        self.mp = 0
        self.statusEffects = []
        self.backpack = []
        self.location = 'top'
        self.gameOver = False
        self.puzzlesSolved = 0
myPlayer = player()

#### Title Screen ####
def titleScreenSelections():
    option = input("> ")
    if option.lower() == ("play"):
        setupGame()
    elif option.lower == ('help'):
        helpMenu()
    elif option.lower() == ('quit'):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid command.")
        option = input("> ")
        if option.lower() == ("play"):
            setupGame()
        elif option.lower == ('help'):
            helpMenu()
        elif option.lower() == ('quit'):
            sys.exit()

def titleScreen():
    os.system('clear')
    print('############################')
    print('# Welcome to the Text RPG! #')
    print('############################')
    print('          - Play -          ')
    print('          - Help -          ')
    print('          - Quit -          ')
    print('Copyright2018 Markus Tousant')
    titleScreenSelections()

def helpMenu():
    print('############################')
    print('# Welcome to the Text RPG! #')
    print('############################')
    print('- Use up,down, left, right to move')
    print('- Type your commands to do them')
    print('- Use "look" to inspect something')
    print('- Use "invo" or "inventory" to check your backpack')
    print('- Good luck and have fun!')
    titleScreenSelections()

#### Map ####
"""
------------- #Player Starts at: TOP
|a1|a2|a3|a4|
-------------
|b1|b2|b3|b4|
-------------
|c1|c2|c3|c4|
-------------
|d1|d2|d3|d4|

"""

ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
PUZZLE = ''
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'east'
RIGHT = 'right', 'west'

solvedPlaces = {'top': False, 'bottom': False, 'north': False, 'south': False,
                'east': False, 'west': False,
                }

zonemap = {

    'top':{
        ZONENAME: "Home",
        DESCRIPTION: 'This is your home!',
        EXAMINATION: "",
        PUZZLE: "",
        SOLVED: False,
        UP: 'north',
        DOWN: 'south',
        LEFT: 'east',
        RIGHT: 'west'
    },
    'north':{
        ZONENAME: "Jay's House",
        DESCRIPTION: "He does seem to be home right now, Maybe I should look around.",
        EXAMINATION: 'There is a note on the door... It seems to be a riddle.',
        PUZZLE: "What get's wetter as it dries? (1 word)\n",
        SOLVED: False,
        UP: 'top',
        DOWN: 'bottom',
        LEFT: 'west',
        RIGHT: 'east'
    },
    'bottom':{
        ZONENAME: "Mom's House",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        PUZZLE: "",
        SOLVED: False,
        UP: 'north',
        DOWN: 'south',
        LEFT: 'west',
        RIGHT: 'east'
    },
    'east':{
        ZONENAME: "Joel's House",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        PUZZLE: "",
        SOLVED: False,
        UP: 'north',
        DOWN: 'south',
        LEFT: 'bottom',
        RIGHT: 'top'
    },
    'west':{
        ZONENAME: "Dad's House",
        DESCRIPTION: 'Your brother, Jay, lives here.',
        EXAMINATION: 'Looks like he left a clue on the table...',
        PUZZLE: "",
        SOLVED: False,
        UP: 'north',
        DOWN: 'south',
        LEFT: 'top',
        RIGHT: 'bottom'
    },
    'south':{
        ZONENAME: "Jesica's House",
        DESCRIPTION: 'This is your home!',
        EXAMINATION: "",
        PUZZLE: "",
        SOLVED: False,
        UP: 'bottom',
        DOWN: 'top',
        LEFT: 'west',
        RIGHT: 'east',
    },


}



#### GAME INTERACTIVITY ####
def printLocation():
    print('\n' + ('#' * (4 + len(myPlayer.location))))
    print('#' + myPlayer.location.upper() + '#')
    print('#' + zonemap[myPlayer.location][DESCRIPTION] + '#')
    print('\n' + ('#' * (4 + len(myPlayer.location))))

def prompt():
    print("\n" + "=====================")
    print("What would you like to do?")
    action = input("> ")
    acceptableActions = ['inventory','invo', 'backpack', 'move', 'go', 'travel', 'walk', 'quit', 'examine', 'interact', 'inspect', 'look']
    while action.lower() not in acceptableActions:
        print("Unknown action, try again.\n")
        action = input("> ")
    if action.lower() == quit:
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        playerMove(action.lower())
    elif action.lower() in ['examine', 'interact', 'inspect', 'look']:
        playerExamine(action.lower())
    elif action.lower() in ['inventory', 'invo', 'backpack']:
        playerInventory(action.lower())

def inventory(action):
    print("[UNDER CONSTRUCTION]")
    return

def playerMove(myAction):
    ask = "Where would you want to move to?"
    dest = input(ask)
    if dest in ['up', 'north']:
        destination = zonemap[myPlayer.location][UP]
        if destination == '':
            print("Invalid destination...")
            ask = "Where would you want to move to?"
            dest = input(ask)
        else:
            movementHandler(destination)
    elif dest in ['down', 'south']:
        destination = zonemap[myPlayer.location][DOWN]
        movementHandler(destination)
    elif dest in ['left', 'east']:
        destination = zonemap[myPlayer.location][LEFT]
        movementHandler(destination)
    elif dest in ['right', 'west']:
        destination = zonemap[myPlayer.location][RIGHT]
        movementHandler(destination)

def movementHandler(destination):
    print("\n" + "You have move to the " + destination + ".")
    myPlayer.location = destination
    printLocation()

def playerExamine(action):
    if zonemap[myPlayer.location][SOLVED] == False:
        print("\n" + (zonemap[myPlayer.location][EXAMINATION]))
        print((zonemap[myPlayer.location][PUZZLE]))
        puzzleAnswer = input("> ")
        checkPuzzleAnswer(puzzleAnswer)
    else:
        print("There is nothing new to see here")
        print("Puzzles Solved: " + str(myPlayer.puzzlesSolved))

def checkPuzzleAnswer(puzzleAnswer):
    if myPlayer.location == 'north':
        if puzzleAnswer.lower() == 'towel':
            print("Correct!")
            zonemap[myPlayer.location][SOLVED] = True
            myPlayer.puzzlesSolved += 1
            print ("Puzzles Solved: " + str(myPlayer.puzzlesSolved))
        else:
            print("Incorrect! Try again...")
            playerExamine('examine')


#### GAME FUNCTIONALITY ####
def startGame():
	return
	
def mainGameLoop():
	while myPlayer.gameOver is False:
		prompt()
		#here handle if puzzles have been solved, boss defeated, explored everything, etc.
		

		
		
def setupGame():
	os.system('cls')
	
	#Name Collecting
	question1 = "Hello, whats your name?\n"
	for character in question1:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	playerName = input('> ')
	myPlayer.name = playerName
	
	#Name Collecting
	question2 = "What role do you want to play?\n"
	question2added = "(You can play as a warrior, mage, or priest)\n"
	for character in question2:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	for character in question2added:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.01)
	playerJob = input('> ')
	validJobs = ['warrior', 'mage', 'priest']
	
	if playerJob.lower() is validJobs:
		myPlayer.job = playerJob
		print ("You are now a " + playerJob + "!\n")
	while playerJob.lower() not in validJobs:
		playerJob = input("> ")
		if playerJob.lower() is validJobs:
			myPlayer.job = playerJob
			print ("You are now a " + playerJob + "!\n")
	


	#### PLAYER STATS ####
	if myPlayer.job is 'warrior':
	    self.hp = 120
	    self.mp = 40
	if myPlayer.job is 'mage':
	    self.hp = 40
	    self.mp = 120
	if myPlayer.job is 'priest':
	    self.hp = 80
	    self.mp = 80
		
		
	#### INTRODUCTION ####
	playerName = playerName.lower().capitalize()
	playerJob = playerJob.lower().capitalize()
	question3 = "Welcome, " + playerName + " the " + playerJob + ".\n"
	for character in question3:
	    sys.stdout.write(character)
	    sys.stdout.flush()
	    time.sleep(0.05)
		
	speech1 = "Welcome home,"+playerName+"!\n"
	speech2 = "I'm sorry to hear about your father passing away.\n"
	speech3 = "I'm sure you will make a great"+playerJob+", just like him.\n"
	speech4 = "Oh he also left this note\n"
	
	for character in speech1:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.03)
	for character in speech2:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.03)
	for character in speech3:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	for character in speech4:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.1)
		
	os.system('cls')
	print('############################\n')
	print("# Let's Start Now! #\n")
	print('############################\n')
	mainGameLoop()
	
		
		
titleScreen()














