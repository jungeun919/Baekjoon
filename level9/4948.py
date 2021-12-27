def is_prime(num):
    if num <= 1:
        return False
    if num > 1:
        for i in range(2, int(num**0.5)+1): # 입력값의 제곱근까지만 반복
            if num % i == 0:
                return False
    return True

num_list = list(range(2, 246912)) # 123456*2 까지
prime_list = []
for i in num_list:
    if is_prime(i):
        prime_list.append(i)

while True:
    n = int(input())

    if n == 0:
        break

    # runtime error
    # count = 0
    # for i in range(n+1, 2*n+1):
    #     if is_prime(i):
    #         count += 1
    # print(count)

    count = 0
    for i in prime_list:
        if n < i < 2*n+1:
            count += 1
    print(count)