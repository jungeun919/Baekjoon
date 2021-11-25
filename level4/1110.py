new_Num = N = int(input())
count = 0

while True:
    ten = N // 10 # 10의 자릿수
    one = N % 10 # 1의 자릿수
    
    total = ten + one
    total_one = total % 10
    N = one*10 + total_one
    
    count = count+1
    
    if (new_Num == N):
        break

print(count) # 사이클의 길이