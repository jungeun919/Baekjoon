N = int(input()) #숫자의 개수
num = list(input()) #N개의 숫자

result = 0
for i in num:
    result += int(i)
print(result)