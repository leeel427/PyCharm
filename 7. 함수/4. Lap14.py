'''
    세개의 정수를 인자로 받아,
    합계와 평균을 출력해주는 함수를 만드시오.

    예) 합계:  평균:
'''
# 설명문 (docstring) """ """
def numb(a, b, c):
    sum = a+b+c
    avg = sum/3
    print("합계 : ",sum, "평균 : ",avg)

numb(3,6,9)
numb(6,9,25)
print()

# 승훈
def calculate(a,b,c):
    print("합계 :",a+b+c,"평균 :",(a+b+c)/3)

a = int(input(">>>"))
b = int(input(">>>"))
c = int(input(">>>"))

calculate(a,b,c)

print()
# 강사님
def print_sum_avg(x, y, z):
    """
    세개의 숫자를 받아 함계와 평균을 출력하는 함수
    :param x:
    :param y:
    :param z:
    :return:
    """
    sum = x + y + z
    avg = sum /3
    print(f"합계: {sum} 평균: {avg}")

print_sum_avg(10, 20, 30)
print_sum_avg(30, 40, 50)