'''
    수학점수의 합 구하기
        - sigma
    수학점수의 평균 구하기
        - sigma 활용
'''
score1, score2, score3 = 10, 20, 30
num_student = 3
score_sum = score1+ score2+ score3
score_mean = score_sum/num_student
print(score_sum)
print(score_mean)

score = [10,20,30]
score_sum = 0
count = len(score)
for i in score:
    score_sum += i
print(score_sum/count)



