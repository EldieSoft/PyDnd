from Player import *
from Dice import *
from Sage import *
import json
import random

def why(story):
    num = str(random.randint(1,15))
    print("\n"+story["story"]["responses"][num]+"\n")

def menu():
    with open('test.json') as file:
        story = json.load(file)
    print("Enter the number of the option you want to choose:\n1: Character info\t2: Roll a die\n3: Sage DM demo\t\t0: Quit")
    try:
        choice = int(input("Choice: "))
    except ValueError:
            print("ERROR")
            menu()
    else:

        match choice:
            case 1:
                np = Player("Leo", 24)
                np.display_stats()
                np.check_inv()

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
                print("Entering Sage DM\n")
                sage = Sage()
#                sage.menu()
                menu()
            #secret options
            case 69:
                why(story)
                menu()
            case 420:
                why(story)
                menu()
            case 666:
                why(story)
                menu()
            case 999:
                print("Clearing screen")
                print("\n" * 10)
                menu()
            case 12345:
                why(story)
                menu()
            #close
            case 0:
                print("Goodbye")
                file.close()
            #wildcard - returns invalid input
            case _:
                print("INVALID INPUT")
                menu()
            

print("Welcome to SageDM\nVersion 0.1 - Early Gameplay Test\n")

menu()
