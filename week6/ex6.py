# f-string 포맷 문자열 사용법
# 출력 자리수
num = 7
print(f'{num}')
print(f'{num:03}')

# 문자열 정렬
print(f'{"파이썬"}')
print(f'{"파이썬":>5}') # 오른쪽 정렬

# 소수점 자리수
pi = 3.141592
print(f'PI = {pi:.2f}')

name = '홍길동'
score = 87.456
print(f"{name}의 점수는 {score:.1f}점 입니다.")

# 파일명 만들기 : file_1.txt, file_2.txt, .....
for i in range(1, 11):
    print(f'file_{i:02}.txt')

# 천 단위 쉼표 출력
fruit = 'apple'
price = 2500
count = 7
print(f'{fruit}의 단가는 {price:,}원이고,')
print(f'총 구매금액은 {price*count:,}원입니다.')