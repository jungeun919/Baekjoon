A, B, C = map(int, input().split())

if B >= C: # 생산비>판매비, 손익분기점 존재x
    print(-1)
    
else: # 생산비(B)<판매비(C)
    count = int(A / (C-B)) + 1 
    print(count)

# A + B*n = C*n
# A = (C-B)*n
# n = A / (C-B)

#     1000 20 200
# 1 | 1020    200
# 2 | 1040    400
# 3 | 1060    600
# 4 | 1080    800
# 5 | 1100    1000
# 6 | 1120    1200