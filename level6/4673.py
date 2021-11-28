def d(n):
    a = 0
    for x in list(str(n)):
        a = a + int(x) 
    return int(n) + a

a= [] #[d(1), d(2), d(3), ... ,d(10000)]
for i in range(1,10001):
    k = d(i)
    a.append(k)

for b in range(1, 10001):
    if b in a:
        pass
    else:
        print(b)