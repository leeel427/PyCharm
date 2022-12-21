'''
    사용자로부터 국어, 수학, 영어 성적이 입력됩니다.
    세 과목의 평균점수가 80점 이상이면 합격입니다.
    그런데 프로그램의 오류가 발생했습니다.
    80 점 이상일 경우 불합격이 표시되도록 프로그램을 작성해 보시오.
    (단, 0점에서 100점 사이의 숫자를 입력하지 않으면 "잘못 입력했습니다"를 출력하시오)

    예시)
        국어 >>>
        수학 >>>
        영어 >>>

        불합격         합격       잘못입력했습니다
'''

# 방법 1

korean = int(input("국어 >>>"))
math = int(input("수학 >>>"))
english = int(input("영어 >>>"))
obj_num = 3
score_sum = (korean + math + english)
score_mean = score_sum/obj_num
if 0 <= korean <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
    if score_mean >= 80:
        print(score_mean, "점 불합격")
    else:
        print(score_mean, "점 합격")
else:
    print("잘못 입력하셨습니다")

# 방법 2
if korean <0 or korean > 100 or math <0 or math >100 or english <0 or english >100:
    print("잘못 입력하셨습니다")
elif score_mean >= 80 :
    print(score_mean, "점 불합격")
else:
    print(score_mean, "점 합격")

# 방법3
if not(0 <= korean <= 100 and 0 <= math <= 100 and 0 <= english <= 100):
    print("잘못 입력하셨습니다")
elif score_mean >= 80:
    print(score_mean, "점 불합격")
else:
    print(score_mean, "점 합격")

# 방법4
subject = ["국어","수학","영어"]
sum = 0
success = True;
for i in subject:
    score = int(input(i +" >>> "))
    if 0 <= score <= 100:
        sum += score
    else:
        print("잘못 입력하셨습니다");
        success=False;
        break
if success :
    if sum/len(subject) >= 80:
        print(sum/len(subject),"점 불합격")
    else:
        print(sum/len(subject),"점 합격")



