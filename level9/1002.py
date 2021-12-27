import math

T = int(input())

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    if distance == 0:
        if r1 == r2: # 동심원일 경우
            print(-1)
        else: # 중심만 같음
            print(0)

    else: # 두 원의 중심이 다름
        if (r1+r2 == distance) or (abs(r2-r1) == distance): # 외접 or 내접
            print(1)
        elif (abs(r2-r1) < distance) and (r1+r2 > distance):
            print(2)
        else:
            print(0)