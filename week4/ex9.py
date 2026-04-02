# 삼항 연산자를 이용해서 조건식 활용
# 점수가 60점 이상이면 합격, 그렇지 않으면 불합격 출력하기

score = 55
if score >= 60:
    print("합격")
else:
    print("불합격")


# 삼항 연산자 이용

result = '합격' if score >= 60 else '불합격'
print(result)