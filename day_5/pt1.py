# Preston Beaty
# Advent Day 5 Pt 1 Challenge
# Dec 5th, 2022

import os
import re

dir = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

input_file = open(os.path.join(dir, 'input.txt'), "r")
input = input_file.readlines()

count = 0
cargo_crane = []

for i in range(9):
    cargo_crane.append([])

#read each line
for line in input:
    #Read in Data Structure
    if count < 8 :

        cargo_crane_index = 0

        for i in range(1, len(line), 4):

            if (line[i].isalpha()):
                cargo_crane[cargo_crane_index].insert(0,line[i])

            cargo_crane_index += 1

    # Read and Process Commands
    if count > 9 :
        numbers = re.findall(r'\d+',line)

        for i in range(int(numbers[0])):
            remove = cargo_crane[int(numbers[1])-1].pop()
            cargo_crane[int(numbers[2])-1].append(remove)

    count += 1

result = ""

for i in range(len(cargo_crane)):
    result = result + (cargo_crane[i][-1])

print(result)