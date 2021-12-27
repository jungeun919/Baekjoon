N = int(input())
nums = map(int, input().split())

def is_prime(num):
    if num <= 1:
        return False
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
    return True

count = 0
for num in nums:
    if is_prime(num):
        count += 1
print(count)