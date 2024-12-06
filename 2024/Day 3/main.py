import re


with open('./Day 3/input.txt') as file:
    data = file.read()

pattern = r"mul\(\d+,\d+\)|do\(\)|don\'t\(\)" # |do\(\)|don\'t\(\)

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
        first, second = i.split(',')

        first = first.replace('mul(', '')
        second = second.replace(')', '')

        score += int(first) * int(second)
    
    

print(score)