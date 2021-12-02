S = input()
alphabet = list('abcdefghijklmnopqrstuvwxyz')

for i in alphabet:
    if S.find(i)  >= 0:
        print(S.find(i), end=" ")
        
    else:
        print(-1, end=" ")