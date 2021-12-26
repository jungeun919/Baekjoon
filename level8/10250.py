# 4층일 경우 (4 4 5)
# 101 201 301 401 | 102 202 302 402 | ...

T = int(input())

for i in range(T):
    h, w, n = map(int, input().split()) # 층, 방, 몇번째 손님

    if n % h == 0:
        floor = h
        ho = n//h
    else:
        floor = n % h
        ho = n//h + 1
    
    print(floor*100 + ho)