# 문자열 실습
# 이메일 정보에서 아이디 추출하기
# email = 'python1234@naver.com'
# id = email.split('@')
# print(id[0])
# print(email.split('@')[0])


# 비밀번호 일부 마스킹하기
# python1234 => *******34 로 출력하기

password = input()
passwordLen = len(password)
print(f'{"*" * (passwordLen-2)}{password[passwordLen-2:]}')