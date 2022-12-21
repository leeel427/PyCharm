# 비만도 계산기를 만들어 보시오.

'''
 예시 )
    BMI 계산기 입니다.
    신장: (입력)
    몸무게 : (입력)
    BMI :
'''
print("BMI 계산기 입니다.")
height = int(input("신장 : "))
weight = int(input("몸무게 : "))
BMI = weight/((height)**2)*10000
print("BMI : ",BMI)
print("BMI지수 : ",BMI)
if BMI<=18.5:
    print("저체중")
elif BMI<=22.9:
    print("정상")
elif BMI<=24.9 :
    print("과체중")
else:
    print("비만")