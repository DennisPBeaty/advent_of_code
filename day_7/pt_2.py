# Preston Beaty
# Advent Day 7 Pt. 1
# Dec 7th, 2022

import os
import re

dir = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

input_file = open(os.path.join(dir, 'input.txt'), "r")
input = input_file.readlines()

total = 0
line_count = 0
folder_sizes = []
folder_name = []
folder_dict = {}
latest_dir = ''

#read each line
for line in input:
    split_input = line.split()

    if len(split_input) == 3:
        #if you cd into a dir
        if (split_input[0] == '$' and split_input[1] == 'cd' and split_input[2] != '..'):
            folder_sizes.append(0)
            folder_name.append(split_input[2])
            latest_dir = split_input[2]
        #if you back out of a dir
        else:
            folder_dict[folder_name.pop()] = folder_sizes.pop()

    else:
        #If the line is an ls command or a dir listing ine skip
        if (split_input[0] == 'dir' or split_input[1] == 'ls'):
            continue
        #Hit a file with an actual size
        elif (split_input[0].isnumeric()):
            for i in range(len(folder_sizes)):
                folder_sizes[i] += int(split_input[0])

for i in range(len(folder_sizes)-1, -1, -1):
    folder_dict[folder_name[i]] = folder_sizes[i]

total_disk_space = 70000000
space_for_update = 30000000

space_available = total_disk_space - folder_dict['/']

delete_amount = space_for_update - space_available

options = {key:val for key, val in folder_dict.items() if val > delete_amount}
sorted_values = sorted(options.values())
print("Smallest value of directory that could be delted for update", sorted_values[0])