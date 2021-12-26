T = int(input())

for i in range(T):
    x, y = map(int,input().split())

    distance = y - x
    count = 0
    move_distance = 1
    move_total = 0

    while move_total < distance:
        count += 1
        move_total += move_distance

        if count % 2 == 0:
            move_distance += 1
    print(count)