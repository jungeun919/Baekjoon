N = int(input())

for i in range(N):
    num = input()
    
    count = 0
    total = 0
    
    for k in num:
        if k == 'O':
            count +=1
        else: #'X'
            count = 0
            
        total += count
        
    print(total)