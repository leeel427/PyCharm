'''
    로또 예상번호 추출 프로그램을 구현하려고 합니다.
    다음 조건에 따라 프로그램을 완성해 보시오.
        1) 로또 번호를 6개 생성한다
        2) 로또 번호는 1~45까지의 숫자중 랜덤한 번호다
        3) 6개의 숫자 모두 달라야 한다
        4) get_random_number() 함수를 사용해서 구현한다

        출력 예) 1 8 11 13 26 42

        - 리스트, 반복문, 조건문, .sort(정렬)
'''
import random
def get_random_number():
    number = random.randint(1,45)
    return number

def check_num(ran_num, num):
    if ran_num not in num:
        num.append(ran_num)

lotto=[]
while len(lotto) <6:
    check_num(get_random_number(),lotto)

lotto.sort()
print(lotto)

print()


# 강사님
# 로또 번호를 저장할 리스트
lotto_num = []
# 현재 뽑은 숫자 개수
count = 0

while True:
    if count > 5:
        break
    random_number = get_random_number()
    if random_number not in lotto_num:
        lotto_num.append(random_number)
        count += 1

lotto_num.sort()
for num in lotto_num:
    print(num, end=" ")
print()
print("1등 당첨 확률 1/8145060")