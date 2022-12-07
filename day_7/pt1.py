# Preston Beaty
# Advent Day 7
# Dec 7th, 2022

import os
import re

dir = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

input_file = open(os.path.join(dir, 'test.txt'), "r")
input = input_file.readlines()

total = 0
line_count = 0

#read each line
for line in input:
    split_input = line.split()

    if len(split_input == 3):

        #if you cd into a dir
        if (split_input[0] == '$' and split_input[0] == 'cd' and split_input[0] != '..'):
            print("1")

        #if you back out of a dir
        else:
            print("2")

    else:
        #If the line is an ls command or a dir listing ine skip
        if (split_input[0] == 'dir' or split_input[0] == 'ls'):
            continue
        #Hit a file with an actual size
        elif (split_input[0].isnumeric()):
            print("you hit an actual file")

    if line_count == 0:
        print(split_input)

    line_count += 1