import random as rnd
my_number=rnd.randint(1,20)
guess=int(input("Guess my number: "))
while guess > 21:
    guess = int(input("Try lower: "))
while guess<21:
    guess=int(input("Try higher: "))
    while guess>21:
        guess=int(input("Try lower: "))
    if guess == 21:
        print("Bullseye.")