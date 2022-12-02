# Preston Beaty
# Advent Day 2 Challenge
# Dec 2nd, 2022

import os

dir = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

input = open(os.path.join(dir, 'input.txt'), "r")
strategy_guide = input.readlines()

# A - Rock
# B - Paper
# C - Scissors

# X - Rock
# Y - Paper
# Z - Scissors

total_points = 0

for round in strategy_guide:
    choices = round.split()

    # Rock
    if (choices[1] == "X"):
        round_points = 1

        # Results of round
        if (choices[0] == "A"):
            round_points += 3
        elif (choices[0] == "B"):
            round_points += 0
        elif (choices[0] == "C"):
            round_points += 6
    # Paper
    elif (choices[1] == "Y"):
        round_points = 2

        # Results of round
        if (choices[0] == "A"):
            round_points += 6
        elif (choices[0] == "B"):
            round_points += 3
        elif (choices[0] == "C"):
            round_points += 0
    
    # Scissors
    elif (choices[1] == "Z"):
        round_points = 3

        # Results of round
        if (choices[0] == "A"):
            round_points += 0
        elif (choices[0] == "B"):
            round_points += 6
        elif (choices[0] == "C"):
            round_points += 3

    total_points += round_points

print("Total points scored:",total_points)

# Part 2

# A - Rock
# B - Paper
# C - Scissors

# X - Lose
# Y - Draw
# Z - Win

dir = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

input = open(os.path.join(dir, 'input.txt'), "r")
strategy_guide = input.readlines()

total_points = 0

for round in strategy_guide:
    choices = round.split()

    # Rock
    if (choices[1] == "X"):
        round_points = 0

        # Results of round
        if (choices[0] == "A"):
            round_points += 3
        elif (choices[0] == "B"):
            round_points += 1
        elif (choices[0] == "C"):
            round_points += 2
    # Paper
    elif (choices[1] == "Y"):
        round_points = 3

        # Results of round
        if (choices[0] == "A"):
            round_points += 1
        elif (choices[0] == "B"):
            round_points += 2
        elif (choices[0] == "C"):
            round_points += 3
    
    # Scissors
    elif (choices[1] == "Z"):
        round_points = 6

        # Results of round
        if (choices[0] == "A"):
            round_points += 2
        elif (choices[0] == "B"):
            round_points += 3
        elif (choices[0] == "C"):
            round_points += 1

    total_points += round_points

print("Total points scored:",total_points)