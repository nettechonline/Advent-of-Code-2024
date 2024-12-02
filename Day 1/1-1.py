with open('./input.txt') as f:
    lines = f.readlines()

col1 = []
col2 = []

difference = 0

for line in lines:
    a = line.split("   ")
    col1.append(int(a[0]))
    col2.append(int(a[1][0:-1]))

col1 = sorted(col1)
col2 = sorted(col2)

for i in range(len(col1)):
    dif = col1[i] - col2[i]
    difference += abs(dif)

print(difference)