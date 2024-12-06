import pathlib
import re


data = pathlib.Path('./Day 3/input.txt').read_text()
pattern = r"mul\(\d+,\d+\)|do\(\)|don\'t\(\)" # |do\(\)|don\'t\(\) - Part 2

search = re.findall(pattern, data)
score = 0
do = True

for i in search:
    if i == "do()":
        do = True
        continue
    elif i == "don't()":
        do = False
        continue
    if do == True:
        # Part 1
        first, second = i.split(',')

        first = first.replace('mul(', '')
        second = second.replace(')', '')

        score += int(first) * int(second)

print(score)