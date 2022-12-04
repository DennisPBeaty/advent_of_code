# Preston Beaty
# Advent Day 4 Challenge
# Dec 4th, 2022

import os

dir = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

input_file = open(os.path.join(dir, 'input.txt'), "r")
input = input_file.readlines()

count = 0
count_pt2 = 0

#read each line
for line in input:
    line = line.strip('\n')

    serperate_vals = line.split(",")
    serperate_vals[0] = serperate_vals[0].split("-")
    serperate_vals[1] = serperate_vals[1].split("-")

    # part 1
    if (int(serperate_vals[0][0]) <= int(serperate_vals[1][0]) and int(serperate_vals[0][1]) >= int(serperate_vals[1][1])):
        count += 1

    elif (int(serperate_vals[1][0]) <= int(serperate_vals[0][0]) and int(serperate_vals[1][1]) >= int(serperate_vals[0][1])):
        count += 1
    

    # part 2
    if (int(serperate_vals[0][0]) <= int(serperate_vals[1][0]) and int(serperate_vals[0][1]) >= int(serperate_vals[1][0])):
        count_pt2 += 1

    elif (int(serperate_vals[0][0]) <= int(serperate_vals[1][1]) and int(serperate_vals[0][1]) >= int(serperate_vals[1][1])):
        count_pt2 += 1

    elif (int(serperate_vals[1][0]) <= int(serperate_vals[0][0]) and int(serperate_vals[1][1]) >= int(serperate_vals[0][0])):
        count_pt2 += 1

    elif (int(serperate_vals[1][0]) <= int(serperate_vals[0][1]) and int(serperate_vals[1][1]) >= int(serperate_vals[0][1])):
        count_pt2 += 1

print("Part 1 Answer:", count)
print("Part 2 Answer:", count_pt2)