# 알파벳 개 숫자는 개 스페이스는 개 기타 개 (% 서식)
# 알파벳 개 숫자는 개 스페이스는 개 기타 개 (f-string 서식)
s = input("문자열을 입력하세요 : ")
alph = 0
num = 0
space = 0
other = 0
for i in range(len(s)):
    if s[i].isalpha():
        alph += 1
    elif s[i].isdigit():
        num+=1
    elif s[i].isspace():
        space+=1
    else:
        other+=1

print("알파벳은 %d개, 숫자는 %d개, 스페이스는 %d개, 기타 %d개입니다." % (alph,num,space,other))
print(f"알파벳은 {alph}개, 숫자는 {num}개, 스페이스는 {space}개, 기타 {other}개입니다.")