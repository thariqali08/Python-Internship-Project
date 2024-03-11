import random

def roll_dics():
    print("Dics Rolling Simulator")
    while True:
        input("Press Enter to roll the dics")
        
        #To generate random number beteween 1 and 6
        dics_result= random.randint(1,6)
        print("You Rolled:",dics_result)
        
        #To continue roll the dics
        quit_roll=input("Do you want to quit(y/n):")
        if quit_roll.lower() == 'y':
            break

    print("Thanks for Playing!")


if __name__ == '__main__':
    roll_dics()
    