import re

with open("./input.txt") as f:
    f = f.read()

pattern = r'mul\((\d{1,3}),(\d{1,3})\)'

matches = re.findall(pattern, f)

result = 0
for match in matches:
    x = int(match[0])
    y = int(match[1])
    result += x * y

print(result)
    