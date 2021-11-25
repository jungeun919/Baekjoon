N = int(input())
num = list(map(int, input().split()))

max = num[0]
min = num[0]
for i in range(N):
    if num[i] > max:
        max = num[i]
    elif num[i] < min:
        min = num[i]
        
print(min, max)