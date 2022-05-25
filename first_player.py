import random


def fristmove():
    print("Welcome to the game, we will role a dice to see who is the first.")
    print("Even means you go first.")
    print("Odd means I go first.")
    roll = random.randint(1,7)
    print("")
    ready = input("Enter 'y' if your ready to play: ")
    if ready == "y":
        print(roll)
        if roll == 2 or roll == 4 or roll == 6:
            print(("The number was {} so you go first.").format(roll))
        else:
            print(("The number was {} so I go first").format(roll))

    return ready



firstmove = fristmove()
