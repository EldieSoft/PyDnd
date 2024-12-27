import json

class Player:
    def __init__(self, story, name=None, level=None):
        if name == None:
            print("What is your name?")
            name = input("Name: ")
        self.name = name
        if level == None:
            print("How old are you?")
            try:
                level = int(input("Level: "))
            except:
                print("INVALID INPUT\nAGE = 24")
                self.level = 1
            else:
                self.level = level
        else:
            self.level = level
        self.story = story

        self.inv = []
    
    def display_stats(self):
        print("\nNAME:", self.name,"\nLEVEL:", self.level, "\n")

    def check_inv(self):
        print("\nPlayer inventory:")
        for i in self.inv:
            print(i + " - " + self.story["story"]["items"][i]["message"])
        print("")


