'''
    턱걸이 평균 층정 프로그램을 만들어 보시오.
    먼저, 턱걸이 횟수를 저장할 빈 리스트를 만드시오.
    그리고 일주일간의 턱걸이 횟수를 입력 받아 리스트에 저장하시오.
    리스트에 저장된 데이터의 평균을 구해 출력하시오.

    예)
        1일차 턱걸이 횟수 >>>
        2일차 턱걸이 횟수 >>>
        3일차 턱걸이 횟수 >>>
        4일차 턱걸이 횟수 >>>
        5일차 턱걸이 횟수 >>>
        6일차 턱걸이 횟수 >>>
        7일차 턱걸이 횟수 >>>

        평균숫자
'''
# 빈 리스트 만들기
chinning = []

chinning.append(int(input("1일차 턱걸이 횟수 >>>")))
chinning.append(int(input("2일차 턱걸이 횟수 >>>")))
chinning.append(int(input("3일차 턱걸이 횟수 >>>")))
chinning.append(int(input("4일차 턱걸이 횟수 >>>")))
chinning.append(int(input("5일차 턱걸이 횟수 >>>")))
chinning.append(int(input("6일차 턱걸이 횟수 >>>")))
chinning.append(int(input("7일차 턱걸이 횟수 >>>")))
print(chinning)

total = chinning[0] + chinning[1] + chinning[2] + chinning[3] + chinning[4] + chinning[5] + chinning[6]
avg = total/7

print("턱걸이 평균 횟수>>", int(avg))


