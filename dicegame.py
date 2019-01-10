import random
import time
import sys
from colorama import *

init(convert = True)

def startGame():
    roll_again = "yes"

    cash = 10000
    computerCash = 100000


    while (roll_again == "yes" or roll_again == "y" or roll_again == "Yes" or roll_again == "Y" or roll_again == "YES" or roll_again == "") and cash != 0:
        print("\nYour Cash: ", cash, "\nComputer Cash: ", computerCash)
        betting = input("How much cash do you want to bet? ")
        if betting.isDigit() == False:
            continue
        if int(betting) > cash:
            print("You don't have that much to bet")
            time.sleep(1.5)
            continue
        if int(betting) > computerCash:
            print("The computer does not have that much to bet")
            time.sleep(1.5)
            continue
        while betting
        
        
        print("\nRolling the dice...")
        time.sleep(2)

        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)

        myScore = dice1 + dice2

        dice3 = random.randint(1,6)
        dice4 = random.randint(1,6)

        compScore = dice3 + dice4
        
        print("You rolled:", dice1, "and", dice2 , " Score:", myScore)
        print("\nComputer rolled :", dice3, "and", dice4 , " Score:", compScore)

        if myScore > compScore:
            print(Fore.GREEN + 'Computer:' + 'You win' + Fore.WHITE)
            cash = cash + int(betting)
            computerCash = computerCash - (int(betting))
            
        if myScore < compScore:
            print (Fore.RED + 'Computer:' + 'You Lose...' + Fore.WHITE)
            cash = cash - int(betting)
            computerCash = computerCash + int(betting)
            
        if myScore == compScore:
            print (Fore.YELLOW + 'It\'s a draw' + Fore.WHITE)
            cash = cash
            computerCash = computerCash

        if cash == 0:
            print(Fore.RED + "Rip... You have been cleaned!" + Fore.WHITE)
            print("Starting over...")
            cash = 10000
            computerCash = 100000
            time.sleep(5)

        if computerCash == 0:
            print(Fore.GREEN + "Computer: Oh no! My money! :c" + Fore.WHITE)
            print("Starting over...")
            cash = 10000
            computerCash = 100000
            time.sleep(5)

        roll_again = input("\nRoll the dice again? (Y/N) ")

startGame()
