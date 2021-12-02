T = int(input())

for i in range(T):
    R, S = input().split()
    R = int(R)
    for k in S:
        print(R * k, end="")
    print()