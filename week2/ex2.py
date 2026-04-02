#ex2.py
# 파이썬의 기본 데이터형

# 정수형
a = 0xFF    # 16진수
b = 0o77    # 8진수
c = 0b1111  # 2진수
print(a,b,c)


# 실수형
a = 3.14
b = 3.14e5
print(a,b)

# 숫자 연산
# ';' - 두 개의 명령문을 한 줄에 쓸 때 사용
a = 10; b = 20
print(a+b)
print(a-b)
print(a*b)
print(a/b)

# '**' : 제곱승
a = 9
b = 2
print(a**b)

# '//' : 나눈 몫
print(a//b)

# '%' : 나눈 나머지
print(a%b)

# bool형 데이터
a = True
a = (10 > 100)
print(a)

a = (100 == 100)
print(a)

# 문자열
a = "파이썬"
print(type(a))

# 파이썬의 문자열은 반드시 따옴표를 사용 => "",'' 둘 다 사용 가능
print("작은 따옴표는 ' 모양이다.")
print('큰 따옴표는 " 모양이다.')

# 문자열을 여러 줄 출력하기
# a = ("파이썬
#      프로그래밍")

a = "파이썬 \n프로그래밍 \n언어"
print(a)

a = """파이썬
프로그래밍
언어"""
print(a)

# 문자열의 연산 : +, * 만 가능
a = "파이썬"
print(a + a)    # 문자열의 + : 문자열 연결
print(a * 5)    # 문자열의 * : 문자열 반복

# 문자열과 숫자는 + 연산자로 연결할 수 없다!
a = "국어 점수는 "
b = 90
# 숫자를 문자로 변환 => str()
print(a + str(b) + "점입니다.")

# 문자열과 숫자의 상호 변환
# int() : 문자열을 정수로
s1 = "100"
print(int(s1) + 1)

# float() : 문자열을 실수로 변환
s2 = "100.123"
print(float(s2) + 10)


a = 10
a += 5; print(a)
a -= 5; print(a)
a *= 5; print(a)
a /= 5; print(a)
a //= 5; print(a)
a %= 5; print(a)
a **= 5; print(a)


# 관계 연산자 (비교 연산자)
a, b = 100,200
print(a > b)
print(a == b)
print(a != b) # 같지않다 => ! =

# 논리 연산자
print(5 == 5)
print(8 != 5)
print(True == False)
print(True != False)
print(True == 1)
print(True == 0)
print(False == 0)




