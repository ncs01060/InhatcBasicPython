# 리스트 조작 함수
# 리스트를 이용한 반복문
aa = [0] * 5
print(aa)
tot = 0

for i in range(len(aa)):  # 0, 1, 2, 3, 4
    aa[i] = int(input('%d 번째 숫자 : ' %i))
    tot += aa[i]

print(aa)
print(tot)
