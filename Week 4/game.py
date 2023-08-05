# import library
import random

# get level
while True:
    try:
        per_lvls = int(input("Level: "))
    except ValueError:
        continue
    if per_lvls > 0:
        break
    if per_lvls <= 0:
        continue

# set random number
randomizer = random.randint(1, per_lvls)

# get guess and check
while True:
    try:
        guesser = int(input("Guess: "))
        if guesser <= 0:
            continue
    except ValueError:
        continue

    if guesser > 0:
        if guesser < randomizer:
            print("Too small!")
        elif guesser > randomizer:
            print("Too large!")
        else:
            print("Just Right!")
            break
