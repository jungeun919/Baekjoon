def is_prime(num):
    if num <= 1:
        return False
    if num > 1:
        for i in range(2, int(num**0.5)+1): # 입력값의 제곱근까지만 반복
            if num % i == 0:
                return False
    return True

T = int(input())

for i in range(T):
    n = int(input())

    a = n//2
    b = n//2

    for j in range(n//2):
        if is_prime(a) and is_prime(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1