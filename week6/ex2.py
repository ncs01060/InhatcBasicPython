# 문자열의 인덱스
# 문자열의 모든 글자를 하나씩 출력 => 인덱스 이용
ss = "파이썬 Python"
ssLen = len(ss)

for i in range(ssLen):
    # 0,1,2,3,...... => 인덱스로 사용 가능
    print(ss[i], end='')

print()

# 문자열 인덱스 관련 함수
ss = 'We are studing Python. Python is easy~^^'
print(ss.count('Python'))
print(ss.find('Python'))
print(ss.find('Python',20))
print(ss.find('C++'))
print(ss.startswith('We'))
print(ss.endswith('^^'))
