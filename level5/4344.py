C = int(input())

for i in range(C):
    score = list(map(int, input().split()))
    avg = sum(score[1:]) / score[0]
    
    up_avg = 0
    for k in score[1:]:
        if k > avg:
            up_avg += 1
            
    print(str("%.3f" %round((up_avg/score[0])*100, 3))+"%")