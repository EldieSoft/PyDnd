from Sage import *
from Entities import *
import json

def menu():
    print("Type the option you want to choose:\nhouse: Play default story, My House.\tcustom: Load custom story.\n\nquit: Quit")
    try:
        choice = input("Choice: ")
    except ValueError:
            print("ERROR")
            menu()
    else:
        match choice:
            case "house":
                with open('my_house/data.json') as file:
                    story = json.load(file)
                title = story["story"]["title"]
                print("Entering", title + "...\n")
                sage = Sage(story)
                file.close()
                menu()
            case "asylum":
                print("Now how did you know I'm working on that?\nI haven't even started working on that yet.\n")
                menu()
            case "custom":
                print("\nWhat is the name of the folder?\n")
                name = input("Name: ")
                game = (name+"/data.json")
                try:
                    file = open(game)
                except:
                    print("Folder not found...\n")
                else:
                    story = json.load(file)
                    title = story["story"]["title"]
                    print("Entering", title+"...\n")
                    sage = Sage(story)
                    file.close()
                menu()
            #close
            case "quit":
                print("Goodbye")
            #wildcard - returns invalid input
            case _:
                print("\nINVALID INPUT\n")
                menu()
            

print("Welcome to SageDM\nVersion 0.3.1 - NPC Overhaul\n")

menu()
