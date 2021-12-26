# 1번째원 1까지
# 2번째원 7까지 (6*1 늘어남)
# 3번째원 19까지 (6*2 늘어남)
# 4번째원 37까지 (6*3 늘어남)
# 5번째원 64까지 (6*4 늘어남)

N = int(input())

count = 1
room = 1

while N > room:
    room = room + (6*count)
    count += 1
print(count)