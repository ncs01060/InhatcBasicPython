# 점수가 90점 이상인 경우 체크
# 그 중에 95점 이상이면 'A+'
# 그렇지 않으면 'A'
# 90점 미만이면 '90점 미만' 출력

# 중첩 조건문
score = int(input())
if score >= 90:
    # 참인 경우 (90점 이상)
    if score >= 95:
        print("A+")
    else:
        print("A") # score >= 90 그리고 score < 95인 경우
else:
    print('90점 미만') # score < 90인 경우
