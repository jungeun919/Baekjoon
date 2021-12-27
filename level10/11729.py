def hanoi(n, left, temp, right):
    if n == 1:
        print(left, right)
    else:
        hanoi(n-1, left, right, temp)
        print(left, right)
        hanoi(n-1, temp, left, right)

N = int(input())

count = 1
for i in range(N-1):
    count = count*2 + 1
print(count)
hanoi(N, 1, 2, 3)