class Player:
    def __init__(self):
        print("What is your name?")
        name = input("Name: ")
        self.name = name
        print("How old are you?")
        try:
            age = int(input("Age: "))
        except:
            print("INVALID INPUT\nAGE = 24")
            self.age = 24
        else:
            self.age = age
    
    def display_stats(self):
        print("\nNAME:", self.name,"\nAGE:", self.age, "\n")

    def check_inv(self):
        pass


