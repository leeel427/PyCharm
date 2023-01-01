# 1. 아래 문자열의 길이를 구하시오.
# q1 = "fjdldionelamdmsd'1322qdmfgvfvc'xv-=dfdfdsf"
q1 = "fjdldionelamdmsd'1322qdmfgvfvc'xv-=dfdfdsf"
print(len(q1))

# 2. 화면에 기호 * 100개를 표시하시오.
a='*'*100
print(a)
print(len(a))

# 3. 문자열 "30"을 각각 정수형, 실수형, 복소수형, 문자형으로 변환하시오.
b = int("30")
print(b,type(b))
c = float("30")
print(c,type(c))
d = complex("30")
print(d,type(d))
e = str("30")
print(e,type(e))

# 4. 다음 문자열 "Niceyear"에서 "year" 문자열만 추출하시오.
#     str = "Niceyear"
str = "Niceyear"
print(str[4:])

# 5. 다음 문자열을 거꾸로 출력하시오.
#     str = "Strawberry"
str = "Strawberry"
print(str[::])
print(str[::-1])

# 6. 다음 문자열에서 '-'을 제거 후 출력하시오.
#     phoneNumber = "010-5555-9999"
phoneNumber = "010-5555-9999"
print(phoneNumber.replace('-',''))

# 7. 다음 문자열(URL)에서 "http://" 부분을 제거 후 출력하시오.
#    url = "http://ezenac.co.kr"
url = "http://ezenac.co.kr"
print(url[7:])

# 8. 다음 문자열을 모두 대문자, 소문자로 각각 출력해 보시오.
#   str = "NiceYear"
str = "NiceYear"
print(str.upper())
print(str.lower())

# 9. 다음 문자열을 슬라이싱을 이용해서 "cde"만 출력하시오.
#   str = "abcdefghijklmn"
str = "abcdefghijklmn"
print(str[2:5])

# 10. 다음 리스트에서 "Apple" 항목만 삭제하시오.
#   list = ["Banana" , "Apple", "Orange"]
list = ["Banana" , "Apple", "Orange"]
del list[1]
print(list)

