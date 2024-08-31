import json

class Player:
    def __init__(self, story, name=None, age=None):
        if name == None:
            print("What is your name?")
            name = input("Name: ")
        self.name = name
        if age == None:
            print("How old are you?")
            try:
                age = int(input("Age: "))
            except:
                print("INVALID INPUT\nAGE = 24")
                self.age = 24
            else:
                self.age = age
        else:
            self.age = age
        self.story = story

        self.inv = []
    
    def display_stats(self):
        print("\nNAME:", self.name,"\nAGE:", self.age, "\n")

    def check_inv(self):
        print("\nPlayer inventory:")
        for i in self.inv:
            print(i + " - " + self.story["story"]["items"][i]["message"])
        print("")


