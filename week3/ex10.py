# list의 슬라이싱(slicing) => 일부분을 잘라오기
#          0  1  2  3  4  5  6  7  8
numbers = [10,20,30,40,50,60,70,80,90]

# 슬라이싱 형식 : 리스트변수[start : stop]
print(numbers[2:7])
print(numbers[0:3])
print(numbers[:3]) # start가 생략되면 처음부터
print(numbers[6:9])
print(numbers[6:]) # stop이 생략되면 끝까지
print(numbers[:])

# 슬라이싱 형식 : 리스트변수[start : stop : step]
# step : 증가값, 건너뛰는 개수
print(numbers[1::2])


# listA = ['mango','banana','apple','orange','kiwi']
# # list에 데이터 추가하기 => append() : 맨 뒤에 항목이 추가됨
# listA.append("melon")
# print(listA)
# listB = []
# print(listB)
# data1 = input('데이터 입력 : ')
# listB.append(data1)
# print(listB)

# 빈 리스트에 데이터 추가

listF = []
f = input("과일 입력 : ")
listF.append(f)
f = input("과일 입력 : ")
listF.append(f)
f = input("과일 입력 : ")
listF.append(f)
f = input("과일 입력 : ")
listF.append(f)
f = input("과일 입력 : ")
listF.append(f)

print(listF)
print("첫 번째 과일 : " + listF[0])
print("마지막 과일 : " + listF[-1])
