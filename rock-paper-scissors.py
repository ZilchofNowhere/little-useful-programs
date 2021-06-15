import random
import time
choices = ["rock", "paper", "scissors"]
while True:
    r = random.choice(choices)
    win = "You won!"
    loss = "Computer won"
    x = input("Do you pick rock (r), paper (p), or scissors (s)?\n").lower()
    print(f"Your computer has picked {r}")
    time.sleep(0.5)
    if x == r[0]:
        print("It's a tie!")
    elif x == "r" and r == "paper":
        print(loss)
    elif x == "r" and r == "scissors":
        print(win)
    elif x == "p" and r == "rock":
        print(win)
    elif x == "p" and r == "scissors":
        print(loss)
    elif x == "s" and r == "paper":
        print(win)
    elif x == "s" and r == "rock":
        print(loss)
    else:
        print("Please enter something valid")
    time.sleep(0.5)
    post = input("To play again, type 'play'\nTo end the game, type 'exit'\n").lower()
    if post == "play":
        continue
    elif post == "exit":
        print("Thanks for playing!")
        time.sleep(3)
        break
