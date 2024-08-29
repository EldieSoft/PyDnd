import json
from Player import *
#TODO - Clean up code a lot. Refactor some areas, get rid of redundant menus.
class Sage:
    def __init__(self, story):
        self.story = story
        print("\nThis is the Sage DM test.\nIf this printed properly, that means it worked.\n")
        np = Player("N/A", 99) # new instance of player, np.
        self.menu(np)
        
    def menu(self, np): #kinda redundant, but good for debugging, will replace with main.py
        print("\nSage DM menu\nWhat do you want to do?\ntype 'start' to start demo\ntype 'quit' to quit\n")
        choice = input("Choice: ")
        match choice:
            #basic menu choices
            case "quit":
                print("\nGoodbye - going back to demo\n")
            case "look":
                print("\nLooking...looking...looking...there's nothing here at the moment...\n")
                self.menu(np)
            case "help":
                print("\nLook, buddy, if you are reading this, you probably already saw the code. Just keep looking.\n")
                np.display_stats() #temp
                self.menu(np)
            case "start":
                self.play(self.story, np)
                self.menu(np)
            case _:
                print("INVALID INPUT\n")
                self.menu(np)
    
    #story and main loop
    def play(self, story, np, current_room="main"):
        #prints message of current room
        print("\n"+story["story"]["rooms"][current_room]["message"]+"\n")
        print("\nWhat do you want to do?")
        choice = input("Choice: ") 
        if choice in (story["story"]["rooms"][current_room]["available_dir"]): #if player types direction, looks in json and prints message if it's there
            x = (story["story"]["rooms"][current_room]["available_dir"].index(choice))
            next_room = (story["story"]["rooms"][current_room]["connected_rooms"][x])
            if (story["story"]["rooms"][next_room]["obstacles"]) == None: #checks for an obstacle
                print("\nYou go", choice, "\n")
                self.play(story, np, next_room) #next_room is passed into the "current_room" param in self.play(self, story, current_room)
            else: #deny entry, go back
                obs = story["story"]["rooms"][next_room]["obstacles"]
                print("\nThere is a",(story["story"]["rooms"][next_room]["obstacles"]), "in the way.\n")
                if story["story"]["obstacles"][obs]["req_item"] in np.inv:
                    print("You use the", story["story"]["obstacles"][obs]["req_item"]+".\nThe", obs, "is open.")
                    if obs == "safe":
                        print("You win!!\nType 'exit' or 'quit' to leave, or keep playing for eternity.")
                    story["story"]["rooms"][next_room]["obstacles"] = None #retry, and it's unlocked
                    np.inv.remove(story["story"]["obstacles"][obs]["req_item"])
                self.play(story, np, current_room)
        elif choice == "quit" or choice == "exit": #exit case
            print("Quitting...\n")
        elif choice == "look": #find items/obstacles
            items_iter = (story["story"]["rooms"][current_room]["items"])
            items = "The room has: "
            if items_iter != None:
                for i in items_iter:
                    items = items + i + ", "
            else: 
                items = "The room is empty."
            print("\n"+items,"\n")
            self.play(story, np, current_room)
        elif choice == "take": #enter take mode
            if (story["story"]["rooms"][current_room]["items"]) == None:
                print("\nThere is nothing to take.\n")
            else:
                print("\nWhat do you want to take?")
                take = input("Take: ")
                if take in (story["story"]["rooms"][current_room]["items"]):
                    print("\nYou took the", take+".\n")
                    np.inv.append(take)
                    story["story"]["rooms"][current_room]["items"] = None
                else:
                    print("There's no", take, "to take.")
            self.play(story, np, current_room)
        
        elif choice == "inv": #check inv
            np.check_inv()
            self.play(story, np, current_room)

        elif choice == "help": #prints help message
            print("\n"+story["story"]["help"]+"\n")
            self.play(story, np, current_room)
        else: #default case
            print("\nInvalid Response\n")
            self.play(story, np, current_room)
