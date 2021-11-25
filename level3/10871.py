# 정수 N개로 이루어진 수열 A
N, X = map(int, input().split())
A  = list(map(int, input().split()))

for i in range(N):
    if A[i] < X:
        print(A[i], end=" ")