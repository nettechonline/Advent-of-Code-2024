with open('./input.txt') as f:
    lines = f.readlines()

safe = 0
unsafe = []

for line in lines:
    lst = [int(x) for x in line.strip().split(" ")]
    
    differ = []

    for i in range(len(lst)-1):
        dif = lst[i+1] - lst[i]
        differ.append(dif)
    
    if all(1 <= value <= 3 for value in differ):
        safe += 1
    elif all(-3 <= value <= -1 for value in differ):
        safe += 1
    else:
        unsafe.append(lst)




print(safe)
