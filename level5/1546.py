N = int(input())
score_list = list(map(int, input().split()))

M = 0
for x in range(N):
    if score_list[x] > M:
        M = score_list[x]
    
hap = 0
for x in range(N):
    score_list[x] = score_list[x] / M * 100
    hap += score_list[x]

avg = hap/N

print(avg)