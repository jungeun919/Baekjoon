n = int(input())

cnt = 0
for a in range(n): #3입력시 3번 반복
    word = input() #aaba
    error = 0
    for i in range(len(word)-1): #0 ~ len(string)-2, 뒤에 j+1이 있음
        if word[i] != word[i+1]: #문자가 달라지면 a->b
            new = word[i+1:]  #달라지는 문자부터 끝문자까지로 새로운 단어배열 생성
            if new.count(word[i]) > 0:
                error += 1
                
    if error == 0: #에러가 없으면 그룹 단어
        cnt += 1
print(cnt)