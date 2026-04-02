# 문자열을 정수로 변환 => int()
# 문자열을 실수로 변환 => float()

name = input("이름을 입력하세요 : ")
kor = int(input("국어 성적을 입력하세요 : "))
eng = int(input("영어 성적을 입력하세요 : "))
math = int(input("수학 성적을 입력하세요 : "))
sum_subject = kor+eng+math

print(name,"님의 성적은\n총합", sum_subject, "점, 평균", sum_subject/3, "점입니다.")
