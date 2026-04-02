birth = int(input("출생 연도를 입력하세요 : "))
age = 2026 - birth
print("당신의 나이는",age,"세 입니다.")
if age >= 20:
    print("성인입니다.")
else:
    print("미성년자입니다.")