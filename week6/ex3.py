# 문자열 슬라이싱 이용하기
# 주민번호 앞자리 6자를 입력받아
# 태어난 연도, 생일, 나이 출력하기
# 2000년도 이전 생일을 기준

front = input("주민번호 앞자리 입력 : ")
year = '19'+front[:2]
month = front[2:4]
day = front[4:6]

age = 2026 - int(year)

print("당신은", year, "년에 태어나셨군요")
print("당신의 생일은",month,"월",day,"일 이군요")
print("당신의 나이는", age, "입니다.")