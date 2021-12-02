word = input()
a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in a:
    word = word.replace(i, 'A') #바꿀 문자: i, 새 문자:'A', i->'A'
    
print(len(word))