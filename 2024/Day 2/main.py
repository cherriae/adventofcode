# Day 2
# The unusual data (your puzzle input) consists of many reports, one report per line. Each report is a list of numbers called levels that are separated by spaces. For example:

# 7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9
# This example data contains six reports each containing five levels.

# The engineers are trying to figure out which reports are safe. The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the following are true:

# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.
# In the example above, the reports can be found safe or unsafe by checking those rules:
#7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
# 1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
# 9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
# 1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
# 8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
# 1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.

with open('./Day 2/input.txt') as file:
    data = file.read().splitlines()

example_levels = [[7, 6, 4, 2, 1], [1, 2, 7, 8, 9], [9, 7, 6, 2, 1], [1, 3, 2, 4, 5], [8, 6, 4, 4, 1], [1, 3, 6, 7, 9]]

levels = [[int(x) for x in level.split(' ')] for level in data]
safes = 0

for level in levels:
    is_valid = True
    increasing = None
    edit = 0 # Part 2

    for i in range(len(level) - 1):
        diff = level[i+1] - level[i]

        if increasing is None:
            increasing = diff > 0

        if (abs(diff) > 3) or (diff == 0) or (increasing and diff < 0) or (not increasing and diff > 0):
            if edit < 1:
                edit += 1
            else:
                is_valid = False
                break

    if is_valid:
        safes += 1

print(safes)