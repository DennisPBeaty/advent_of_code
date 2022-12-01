# Preston Beaty
# Advent Day 1 Challenge
# Dec 1st, 2022

import os

dir = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

elf_cals = open(os.path.join(dir, 'input.txt'), "r")
cals = elf_cals.readlines()
  
count = 0

cal_total = []
elf_totals = []

for snack in cals:
    try:
        calorie = int(snack)
        cal_total.append(calorie)
    except ValueError:
        elf_totals.append(sum(cal_total))
        cal_total = []

max_value = max(elf_totals)
max_index = elf_totals.index(max_value)

print("Elf", max_index, "has", max_value, "calories.")