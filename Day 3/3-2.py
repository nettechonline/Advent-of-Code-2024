import re

with open("./input.txt") as f:
    f = f.read()

pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
do_dont = r'(do\(\)|don\'t\(\))'

mul = True

results = 0

split = re.split(f'({do_dont}|{pattern})', f)
    
for i in split:
    if not i:
        continue
    if i == 'do()':
        mul = True

    elif i == "don't()":
        mul = False

    elif re.match(pattern, i):
        
        match = re.match(pattern, i)
        x = int(match[1])
        y = int(match[2])
        
        if mul:
            results += x * y

print(results)