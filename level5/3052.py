rest = []

for i in range(10):
    A = int(input())
    rest.append(A % 42)
    
a = set(rest)
difference = len(a)

print(difference)