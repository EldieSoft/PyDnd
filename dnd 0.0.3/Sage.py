import json

class Sage:
    with open("test.json") as file:
        story = json.load(file)

    def __init__(self):
        print("\nThis is the Sage DM test.\nIf this printed properly, that means it worked.\n")

    def menu(self):
        print("\nSage DM menu\nWhat do you want to do?\ntype 'start' to start demo\ntype 'quit' to quit")
        choice = input("Choice: ")
        match choice:
            #basic menu choices
            case "quit":
                print("\nGoodbye - going back to demo\n")
            case "look":
                print("\nLooking...looking...looking...there's nothing here at the moment...\n")
                self.menu()
            case "help":
                print("\nLook, buddy, if you made it this far, you've probably been looking at the code. If you don't know what you're doing, thats on you.\n")
                self.menu()
            case "start":
                self.play(self.story)
                self.menu()
            case _:
                print("INVALID INPUT\n")
                self.menu()
    
    #story
    def play(self, story, current_room="room_0"):
        print("\n"+story["story"]["rooms"][current_room]["message"]+"\n")
        print("\nWhat direction do you want to go?")
        choice = input("Choice: ")
        if choice in (story["story"]["rooms"][current_room]["available_dir"]):
            print("\nYou go", choice, "\n")
            x = (story["story"]["rooms"][current_room]["available_dir"].index(choice))
            current_room = (story["story"]["rooms"][current_room]["connected_rooms"][x])
            self.play(story, current_room)
        elif choice == "quit" or choice == "exit":
            print("Quitting...\n")
        elif choice == "look":
            items_iter = (story["story"]["rooms"][current_room]["items"])
            items = "The room has: "
            if items_iter != None:
                for i in items_iter:
                    items = items + i + ", "
            else:
                items = "The room is empty."
            print("\n"+items,"\n")
            self.play(story, current_room)
        elif choice == "help":
            print("\n"+story["story"]["help"]+"\n")
            self.play(story, current_room)
        else:
            print("\nInvalid Response\n")
            self.play(story, current_room)
