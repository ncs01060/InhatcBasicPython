# 함수 연습

def average(n1,n2,n3):
    return (n1+n2+n3) / 3

num1 = int(input("숫자 1 : "))
num2 = int(input("숫자 2 : "))
num3 = int(input("숫자 3 : "))

print("평균 :",round(average(num1,num2,num3),1))