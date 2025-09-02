import   random

class Dice:
    def __init__(self,sides=6):
        self.sides = sides #by default 6 sides

    def roll(self):
        return random.randint(1,self.sides)
    
    #Program run function 
if __name__ == "__main__":
        dice = Dice()

        while True:
            user_input =input("Roll the dice? (y/n): ").lower()
            if(user_input) =='y':
                print("You rolled: ", dice.roll())

            elif(user_input) =="n":
                print("Game Over bye!") 
                break
            else:
                print("Please type Y or N.")
                  
