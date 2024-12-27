import random

class Dice:

    def roll(self, num=6):
        answer = random.randint(1,num)
        print("\nRolling die with", num, "sides.")
        print("The roll is", answer, "\n")
    
    def battle(self, num1, num2):
        roll = random.randint(1, num2)
        if num1 >= roll:
            print("Roll is", roll, ". Player num is", num1, ". Player wins!")
        else:
            print("Roll is", roll, ". Player num is", num1, ". Comp wins!")


