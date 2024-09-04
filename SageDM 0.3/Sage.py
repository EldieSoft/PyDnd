import json
from random import randint
import os
from Player import *

class Sage:
    def __init__(self, story):
        self.story = story
        np = Player(story, "N/A", 99) # new instance of player, np. Will change after next update probably.
        self.play(story, np)
 
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
                    print("You use the", story["story"]["obstacles"][obs]["req_item"]+".\nThe", obs, "is now open.")
                    if story["story"]["obstacles"][obs]["victory_condition"] == True:  #checks to see if the obstacle is a victory condition
                        print("You win!!\nType 'exit' or 'quit' to leave, or keep playing for eternity.")
                    story["story"]["rooms"][next_room]["obstacles"] = None #retry, and it's unlocked
                    np.inv.remove(story["story"]["obstacles"][obs]["req_item"])
                self.play(story, np, current_room)
        elif choice == "quit" or choice == "exit": #exit case
            print("Quitting...\n")
        elif choice == "look": #find items/obstacles/people to talk to
            #TODO: FIND A WAY TO MAKE 'LOOK' PRINT IF SOMEONE IS IN THE ROOM WITHOUT BREAKING BACKWARDS COMPATIBILITY
            items_iter = (story["story"]["rooms"][current_room]["items"])
            items = "The room has: "
            if items_iter != None:
                for i in items_iter:
                    items = items + i + ", "
            else: 
                items = "There are no items in the room.."
            print("\n"+items,"\n")
            try:
                if (story["story"]["rooms"][current_room]["NPCs"]) == None:
                    print("\nThere is nobody to talk to.\n")
                else:
                    print("\n"+story["story"]["rooms"][current_room]["NPCs"]+" is in the room.\n")
            except:
                print("\nThere is nobody to talk to.\n")
            finally:
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
        elif choice == "clear": #clear screen
            os.system("clear")
            self.play(story, np, current_room)

        elif choice == "talk": #talk to a person in the room
            try: #checks to see if 'NPCs' is a field in JSON
                if (story["story"]["rooms"][current_room]["NPCs"]) == None:
                    print("\nThere is nobody to talk to.\n")
                else:
                    print("\nLet's talk to " + story["story"]["rooms"][current_room]["NPCs"]+".\n")
                    npc = (story["story"]["rooms"][current_room]["NPCs"])
                    i = str(randint(1, 4)) #so far it just picks a random message from the list
                    message = "message_"+i
                    print("\n"+story["story"]["NPCs"][npc][message]+"\n")
            except: #if error, just assume there is no person
                print("\nThere is nobody to talk to!\n")
            finally:
                self.play(story, np, current_room)

        elif choice == 'say':
            print("\nWhat do you want to say?\n")
            say = input("Say: ")
            print("You said", say+". Nothing else happened...\n")
            self.play(story, np, current_room)
        elif choice == "help": #prints help message
            print("\n"+story["story"]["help"]+"\n")
            self.play(story, np, current_room)
        else: #default case
            print("\nInvalid Response\n")
            self.play(story, np, current_room)
