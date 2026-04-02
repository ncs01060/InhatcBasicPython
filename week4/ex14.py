# 반복문 제어 - break
for i in range(1,11):
    if i == 5:
        break   # 반복문 탈출
    print(i)

# continue - 반복문의 처음으로 돌아가게 하는 제어문

for i in range(1,11):
    if i == 5:
        continue # 값을 건너뛰는 효과
    print(i)