# for 반복문, continue 사용
# 1부터 100까지의 합을 구하시오.
# 단, 3의 배수는 제외하시오

result = 0
for i in range(1,101):
    if i%3 == 0:
        continue
    result+=i
print(result)