print("두 정수를 입력하세요.")

# first_num = input("첫 번째 정수? ")
# second_num = input("두 번째 정수? ")
#
# # input() 함수로 입력된 값 => 문자열(str)
# # 문자열을 정수로 변환 => int()
#
# print("두 정수의 합은 ", first_num+second_num, " 입니다.")

first_num = int(input("첫 번째 정수? "))
second_num = int(input("두 번째 정수? "))

result = first_num+second_num
print("두 정수의 합은", result  , "입니다.")

# 문자열의 연결 => '+'
print("두 정수의 합은 " + str(result) + "입니다")
