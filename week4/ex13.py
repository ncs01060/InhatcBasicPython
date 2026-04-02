# 조건반복문 - while
i = 1
while i < 10: # 조건식이 참인 경우 반복
    print(i)
    i += 1

# 무한루프 만들기 : while True:
# 두 수를 입력받아서 합을 출력해 주는 계산기 만들기

while True:

    num1 = int(input('숫자 1 입력 : '))
    # 숫자 1에 0이 입력되면 반복문을 종료하자
    if num1 == 0: # a무한루프를 종료하는 조건
        break
    num2 = int(input('숫자 2 입력 : '))
    sum = num1 + num2
    print(num1, '+', num2, '=', sum)

print("프로그램 종료")

