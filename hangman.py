#hangman but wont bother making shapes so its all written
import random
import time

words = [
    "apple",
    "orange",
    "banana",
    "peach",
    "melon",
    "fruit",
    "tomato",
    "potato"
]
usedltrs = []

w = random.choice(words)
class A:
    done = False
def lose():
    y = 0
    for l in usedltrs:
        if l in w:
            y += 0
        else:
            y += 1
    print(f"You have {10 - y} turns left")
    if y == 10:
        A.done = True
def word():
    for c in w:
        if c in usedltrs:
            print(c)
        else:
            print("_")
word()
def ask():
    global r
    r = input("Guess a letter or the whole word\n").lower()
def add():
    if r not in usedltrs:
        usedltrs.append(r)
    else:
        return
def winning():
    x = 0
    for c in w:
        if c in usedltrs:
            x += 1
        else:
            x += 0
    if x == len(w):
        print("Congrats! You found the hidden word!")
    else:
        return   

while A.done == False:
    ask()
    if len(r) == 0:
        print("Please enter an input")
    elif len(r) == 1:    
        if r in w:
            print("You are right!")
            add()
            word()
            print(f"Used letters are {usedltrs}")
        else:
            print("You are wrong!")
            add()
            print(f"Used letters are {usedltrs}")
            lose()
    elif len(r) == len(w):
        if r == w:
            print("Congrats! You found the hidden word!")
            break
        else:
            print("You are wrong! Try again")
            lose()
    else:
        print("Please respect the instructions and play fairly")
    if A.done == True:
        print("You lost!")
        break
    x = 0
    for c in w:
        if c in usedltrs:
            x += 1
        else:
            x += 0
    if x == len(w):
        print("Congrats! You found the hidden word!")
        break
    """
    winning()
    if winning():
        break
    """
del usedltrs
print("Thanks for playing!")
time.sleep(3)
