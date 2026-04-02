# 사칙연산을 처리하는 계산기 프로그램
# 필요한 데이터 - 연산자(+,-,*,/) , 숫자 1, 숫자 2
def calc(op,x,y):
    result = 0
    if op == "+":
        result = x+y
    elif op == "-":
        result = x-y
    elif op == "*":
        result = x*y
    elif op == "/":
        result = x/y
    return result

# main code
# 무한 루프를 이용한 반복 프로그램으로 확장하기
# 종료조건 : 'q'를 입력하면 프로그램 종료
while True:
    oper = input("연산자를 입력해주세요 : (종료 q)")
    if oper == "q":
        break
    num1 = int(input("첫 번째 정수를 입력해주세요 : "))
    num2 = int(input("두 번째 정수를 입력해주세요 : "))
    print(calc(oper,num1,num2))