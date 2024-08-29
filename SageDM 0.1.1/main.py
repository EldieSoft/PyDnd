from Player import *
from Dice import *
from Sage import *
import json
import random

def menu():
    with open('my_house/data.json') as file:
        story = json.load(file)
    print("Enter the number of the option you want to choose:\n1: Enter SageDM\t\t2: Roll a die\n3: Character Test\t0: Quit")
    try:
        choice = int(input("Choice: "))
    except ValueError:
            print("ERROR")
            menu()
    else:

        match choice:
            case 1:
                print("Entering Sage DM\n")
                sage = Sage(story)
                menu()            
            case 2:
                print("How many sides?")
                try:
                    sides = int(input("Sides: "))
                except:
                    print("INVALID INPUT")
                    sides = 6
                die = Dice()
                die.roll(sides)
                menu()
            case 3:
                np = Player()
                np.display_stats()
                np.check_inv()
                menu()
            
            case 999:
                print("Clearing screen")
                print("\n" * 10)
                menu()
            #close
            case 0:
                print("Goodbye")
                file.close()
            #wildcard - returns invalid input
            case _:
                print("INVALID INPUT")
                menu()
            

print("Welcome to SageDM\nVersion 0.1.1\n")

menu()
