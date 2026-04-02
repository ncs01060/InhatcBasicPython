# 주석(comment) - 코드에 대한 설명, 프로그램 실행과는 무관
# int(정수), float(실수), bool(참/거짓), str(문자열)


# '=' : 오른쪽 값을 왼쪽 변수에 대입
# 변수 지정
intVar = 0
floatVar = 3.14
strVar = "홍길동"
boolVar = True
# print(intVar, floatVar, strVar, boolVar)

# type() : 변수가 저장하고 있는 데이터 타입을 확인
# print(type(intVar))
# print(type(floatVar))
# print(type(strVar))
# print(type(boolVar))

# 파이썬 키워드
# import keyword
# print(keyword.kwlist)


# 변수의 사용
intVar = 200
floatVar = 100.123
strVar = "파이썬"
boolVar = False

print(intVar, floatVar, strVar, boolVar)

var1 = 100
var2 = var1 + 100
print(var1,var2)

var1 = 100 + 200
print(var1)

var4 = 300
var3 = var4
var2 = var3
var1 = var2
print(var1)

var1 = var2 = var3 = var4 = 500
print(var1)