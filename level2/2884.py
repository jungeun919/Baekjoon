H, M = map(int, input().split())

#20:50 ->20:05
if (M>=45):
    M = M-45
    print(H, M)

#6:15 -> 5:30
elif (M<45) and (H>0):
    H = H-1
    M = 60+M-45
    print(H, M)

#0:35 -> 23:45
else:
    H = 23
    M = M+15
    print(H, M)