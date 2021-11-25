num = []
max_num = 0

for i in range(9):
    num.append(int(input()))
    
    if num[i] >= max_num:
        max_num = num[i]
        
print(max_num, num.index(max_num)+1)