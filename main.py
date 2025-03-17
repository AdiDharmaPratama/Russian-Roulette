import random
import time

def play_game():
    chambers = input("Input The Number of Bullet Chambers (Default = 6): ")

    if not chambers:
        chambers = 6
    elif not chambers.isdigit():
        quit("Invalid Number of Chambers!")

    fatal_bullet = random.randint(1, int(chambers))
    print(f"Now The Chambers Contain {chambers} Bullets!!")
    time.sleep(2)
    print("")
    
    for x in range(1, int(chambers) +1):
        input("Press Enter to Pull The Trigger!")
        if x == fatal_bullet:
            print("You Dead!")
            print("Game Over!")
            startAgain = input("Do You Want to Start Again? (y/N): ")
            if startAgain and startAgain.lower()[0] == "y":
                return play_game()
            else:
                break
        print("You Will Live to See Another Day")
play_game()