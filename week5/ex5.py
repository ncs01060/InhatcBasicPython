# 매개변수와 반환값이 있는 함수
# 함수 선언
# 수 개의 숫자를 받아서 합을 반환하는 함수

def plus(num1, num2):
    result = num1 + num2
    return  result

# 메인 코드
# 반환값이 있는 함수인 경우
# 반드시 대입연산자 왼쪽에 변수를 지정해야 함
res = plus(100, 200)
print(res)


