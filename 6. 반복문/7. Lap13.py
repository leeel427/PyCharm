'''
    순신은 lily라는 이름의 교환학생과 친해지게 되었습니다.
    영어를 잘하지 못하는 순신은 lily에게 한국어를 가르쳐 주기 위해
    한국어 연습 프로그램을 만들게 되었습니다.
        - 연습할 한국어가 담긴 리스트를 만든다
        - 리스트에서 순서대로 단어를 가져와 화면에 출력한다
        - 프로그램 사용자는 단어를 그대로 입력하고
        - 맞추면 다음 단어를 가져온다. 틀리면 프로그램 종료

        Let's Learning Korean
        사랑해
        사랑해
        귀엽다
        귀엽다
        고마워
        고마워
        행복해
        햄복해
        프로그램 종료
'''
'''
test=["사랑해", "귀엽다", "고마워", "행복해"]
print("Let's Learning Korean")
i=0
while i<len(test):
    print(test[i])
    ans=input("=")
    if ans != test[i]:
        print("실패!!")
        break
    i += 1
print("성공")
'''


''' 강사님 풀이
word_list=["사랑해", "귀엽다", "고마워", "행복해"]
print("Let's Learning Korean")
for word in word_list:
    print(word)
    data = input()
    if data != word:
        break
'''

# 전체 문제 개수 : 4개     len(word_list)
# 맞힌 문제 개수 : 2개
# 틀린 문제 개수 : 2개

word_list=["사랑해", "귀엽다", "고마워", "행복해"]
print("Let's Learning Korean")
o = 0
x = 0
for word in word_list:
    print(word)
    data = input("=")
    if data == word:
        o += 1
    elif data != word:
        x += 1
print("전체 문제 개수",len(word_list),"개")
print("맞힌 문제 개수",o,"개")
print("맞힌 문제 개수",x,"개")

'''     강사님 풀이
word_list=["사랑해", "귀엽다", "고마워", "행복해"]
print("Let's Learning Korean")
score = 0
for word in word_list:
    print(word)
    data = input("=")
    if data == word:
        score += 1
print("전체 문제 개수",len(word_list),"개")
print("맞힌 문제 개수",score,"개")
print("맞힌 문제 개수",len(word_list) - score,"개")
'''