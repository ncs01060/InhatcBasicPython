# 연습 문제 2

def bigger(n1,n2):
    if n1 > n2:
        return  n1
    else:
        return  n2

num1 = int(input("첫 번째 숫자 : "))
num2 = int(input("두 번째 숫자 : "))
print("큰 수 :",bigger(num1,num2))