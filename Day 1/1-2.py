with open('./input.txt') as f:
    lines = f.readlines()

col1 = []
col2 = []

simularity = 0

for line in lines:
    a = line.split("   ")
    col1.append(int(a[0]))
    col2.append(int(a[1][0:-1]))

col1 = sorted(col1)
col2 = sorted(col2)

for i in col1:
    if i not in col2:
        simularity += i * 0
    else:
        for j in col2:
            if i == j:
                simularity += i * 1

print(simularity)
