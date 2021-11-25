A = int(input())
B = int(input())
C = int(input())

mul = A * B * C
mul = str(mul)

result = []

for i in mul:
    result.append(i)

for i in range(10):
    count = result.count(str(i))
    print(count)