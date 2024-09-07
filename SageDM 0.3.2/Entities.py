import json
from random import randint
from Player import *

class NPC:
    def __init__(self, story, name, player): #essentially a helper function so that not everything has to be done in the main loop in Sage.py
        self.story = story
        self.name = name
        self.player = player
        print("\nLet's talk to " + name + ".\n")
        self.talk(story, name, player)
    
    def talk(self, story, name, player):
        try:
            if (story["story"]["NPCs"][name]["req_item"]) == None:
                print("\n"+story["story"]["NPCs"][name]["message_default"]+"\n")
            else:
                if (story["story"]["NPCs"][name]["req_item"]) in player.inv:
                    print("\n"+story["story"]["NPCs"][name]["message_passed"]+"\n")
                    player.inv.remove(story["story"]["NPCs"][name]["req_item"])
                    player.inv.append(story["story"]["NPCs"][name]["give_item"])
                    story["story"]["NPCs"][name]["req_item"] = None
                else:
                    print("\n"+story["story"]["NPCs"][name]["message_quest"]+"\n")
        except:
            print("\n"+ name +" doesn't seem too talkative...\n") #default case, in case of unhandled exception

class Enemy:
    def __init__(self, story=None):
        print("Uh oh, an enemy!!")
