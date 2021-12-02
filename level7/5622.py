word = input()
string = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

time = 0
for i in range(len(word)): #BEAR: 4
    for j in string:
        if word[i] in j:
            time = time + string.index(j) + 3 #숫자 1을 걸려면 2초 필요, index는 0부터
            
print(time)