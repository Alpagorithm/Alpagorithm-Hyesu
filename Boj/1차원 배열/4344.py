c = int(input())

for i in range(c):
    score = list(map(int, input().split()))
    #index 0은 학생수, 이후 점수
    sum = 0

    # 평균구하기
    for j in range(1, score[0] + 1):
        sum = sum + score[j]
    ave = sum / score[0]

    n = 0 #평균넘은학생수
    for j in range(1, score[0]+1):
        if ave < score[j]:
            n = n+1
    print(format(n/score[0]*100,".3f")+ "%")