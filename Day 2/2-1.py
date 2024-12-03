with open('./input.txt') as f:
    lines = f.readlines()

safe_reports = 0

for line in lines:
    lst = [int(x) for x in line.strip().split(" ")]
    
    if len(lst) != len(set(lst)):
        continue
    

   
    dir1 = [] 
    for i in range(len(lst)-1):
        
        
        if lst[i] < lst[i+1]:
            dir1.append("up")
        else:
            dir1.append("down")
        
    if "up" in dir1 and "down" in dir1:
        continue
    

    greater = []
    for i in range(len(lst)-1):
        
        
        if abs(lst[i] - lst[i+1]) > 3:
            greater.append("greater")

    if "greater" in greater:
        continue
    
    
    safe_reports += 1


print(safe_reports)







