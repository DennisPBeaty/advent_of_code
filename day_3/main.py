# Preston Beaty
# Advent Day 3 Challenge
# Dec 3rd, 2022

import os

dir = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

input_file = open(os.path.join(dir, 'input.txt'), "r")
input = input_file.readlines()

total_points = 0
total_points_pt2 = 0
count = 0
ruck_sacks = []

#read each line
for line in input:
    #seperate rucksack into compartments
    first_compartment = line[:len(line)//2]
    second_compartment = line[len(line)//2:]
    #find shared char
    shared_char = ''.join(set(first_compartment).intersection(second_compartment))

    if (ord(shared_char) - 96 < 1):
        total_points += ord(shared_char)-38
    else:
        total_points += ord(shared_char)-96

    count += 1
    ruck_sacks.append(line.strip('\n'))

    if (count == 3):
        shared_char = ''.join(set(ruck_sacks[0]).intersection(ruck_sacks[1]).intersection(ruck_sacks[2]))
        if len(shared_char) > 1:
            shared_char = shared_char[1]

        if (ord(shared_char) - 96 < 1):
            total_points_pt2 += ord(shared_char)-38
        else:
            total_points_pt2 += ord(shared_char)-96
        ruck_sacks = []
        count = 0

print("Answer to Pt. 1:",total_points)
print("Answer to Pt. 2:",total_points_pt2)
