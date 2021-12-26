# 2층 | 1  4 10 20 35
# 1층 | 1  3  6 10 15
# 0층 | 1  2  3  4  5

T = int(input())

for i in range(T):
    k = int(input()) # k층
    n = int(input()) # n호
    
    ho = [i for i in range(1, n+1)] # 3호: [1, 2, 3]
    for j in range(k):
        for x in range(1, n):
            ho[x] = ho[x] + ho[x-1]
        # print(ho)
    print(ho[n-1]) # 인덱스 0부터 시작