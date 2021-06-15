import random
import time

def dice():
    print("Rolling your dice")
    time.sleep(1)
    x = random.randint(1,6)
    print(f"Your number turned out to be {x}")
    global k
    k = input('Type "again" to roll your dice again\nType "exit" to exit\n').lower()

dice()
while k == "again":
    dice()
if k == "exit":
    print("Thanks for playing")
    time.sleep(3)
