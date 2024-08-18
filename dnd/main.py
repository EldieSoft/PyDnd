from Player import *
from Dice import *
import json
import random

def why(story):
    num = str(random.randint(1,8))
    print("\n"+story["story"]["responses"][num]+"\n")

def menu():
    with open('test.json') as file:
        story = json.load(file)
    print("Enter the number of the option you want to choose:\n1: Character info\t2: Roll a die\n3: Print part of story\t0: Quit")
    try:
        choice = int(input("Choice: "))
    except ValueError:
            print("ERROR")
            menu()
    else:

        match choice:
            case 1:
                np = Player()
                np.display_stats()

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
                 print("What part of story do you want to read? (0-3)")
                 try:
                    read = int(input("Choice: "))
                 except:
                    print("VALUE ERROR\nValue = 0")
                    read = 0
                 if (read > 3) or (read < 0):
                     print("CHOICE OUT OF RANGE")
                 else:
                    printer = "room_"
                    printer+=str(read)
                    print("\n"+story["story"]["rooms"][printer]+"\n")
                 menu()
            case 69:
                why(story)
                menu()
            case 420:
                why(story)
                menu()
            case 666:
                why(story)
                menu()
                menu()
            case 999:
                print("Clearing screen")
                print("\n" * 10)
                menu()
            case 0:
                print("Goodbye")
                file.close()
            case _:
                print("INVALID INPUT")
                menu()
            

print("This is a test for a text-based DND client I'm working on.\nVersion 0.0.1 - Class Debug Demo\n")

menu()
