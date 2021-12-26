N = int(input())

count = 0
while True:
    if N % 5 == 0: # N이 5의 배수가 되면 종료
        count += N//5
        print(count)
        break

    N -= 3
    count += 1

    if N < 0:
        print(-1)
        break