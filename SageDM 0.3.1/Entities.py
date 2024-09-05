import json
from random import randint

class NPC:
    def __init__(self, story, npc, player=None): #essentially a helper function so that not everything has to be done in the main loop in Sage.py
        self.story = story
        self.npc = npc
        print("\nLet's talk to " + npc + ".\n")
        num = str(randint(1,4))
        message = "message_"
        message+=num
        print("\n"+story["story"]["NPCs"][npc][message]+"\n")
        if player == None:
            print("\nDon't forget to pass 'player'! That would cause problems...\n")
    
    def talk(self):
        print("This will be the main talking function, all above is boilerplate.")

class Enemy:
    def __init__(self, story=None):
        print("Uh oh, an enemy!!")
