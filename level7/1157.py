word = input().upper() #apple
unique = list(set(word)) #입력받은 문자 중 중복값 제거 -> A= {} -> ['p', 'a', 'l', 'e']

cnt = []
for i in unique:
    c = word.count(i)
    cnt.append(c) #-> [2, 1, 1, 1], ['p', 'a', 'l', 'e']의 요소 개수와 같음
    
if cnt.count(max(cnt)) > 1: #여러 개 존재하는 경우
    print("?")
else: #가장 많이 사용된 알파벳이 1개 일 경우
    max_index = cnt.index(max(cnt))
    print(unique[max_index])