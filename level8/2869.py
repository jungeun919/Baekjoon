A, B, V = map(int, input().split())

# (A-B)*n + A = V
# (A-B)*n = V-A

day = (V-A) % (A-B)
if day == 0:
    print((V-B) // (A-B))
else: # 나누어 떨어지지 않으면
    print((V-B) // (A-B) + 1)