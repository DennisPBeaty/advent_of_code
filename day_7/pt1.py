# Preston Beaty
# Advent Day 7
# Dec 7th, 2022

import os
import re

dir = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

input_file = open(os.path.join(dir, 'test.txt'), "r")
input = input_file.readlines()

total = 0

#read each line
for line in input:
    