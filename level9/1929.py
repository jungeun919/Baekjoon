M, N = map(int, input().split())

def is_prime(num):
    if num <= 1:
        return False
    if num > 1:
        for i in range(2, int(num**0.5)+1): # 입력값의 제곱근까지만 반복
            if num % i == 0:
                return False
    return True

for i in range(M, N+1):
    if is_prime(i):
        print(i)