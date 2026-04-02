subject = []

kor = int(input("국어 점수 입력 : "))
math = int(input("수학 점수 입력 : "))
eng = int(input("영어 점수 입력 : "))

subject.append(kor)
subject.append(math)
subject.append(eng)
print(subject)
print("국어 :", subject[0],"점, 수학 :", subject[1], "점, 영어 :", subject[2] , "점")
total = subject[0] + subject[1] + subject[2]
print("총점 = ", total)
print("평균 = ", total/3)

slice_list = subject[0:2]
print(slice_list)