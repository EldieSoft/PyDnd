from Sage import *
import json

def menu():
   # with open('my_house/data.json') as file:
    #    story = json.load(file)
    print("Type the option you want to choose:\nstart: Play default story, My House.\tcustom: Load custom story.\nquit: Quit")
    try:
        choice = input("Choice: ")
    except ValueError:
            print("ERROR")
            menu()
    else:
        match choice:
            case "start":
                with open('my_house/data.json') as file:
                    story = json.load(file)
                title = story["story"]["title"]
                print("Entering", title + "...\n")
                sage = Sage(story)
                file.close()
                menu()            
            case "custom":
                print("\nWhat is the name of the folder?\n")
                name = input("Name: ")
                game = (name+"/data.json")
                try:
                    file = open(game)
                except:
                    print("Foler not found...\n")
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
            

print("Welcome to SageDM\nVersion 0.2\n")

menu()
