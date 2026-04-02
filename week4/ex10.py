# 반복문 - 횟수반복(for), 조건반복(while)
for i in [1,2,3,4,5,6,7,8,9,10]:
    print(i,'hello')

menu = ['americano','latte','moca','ccino']

for item in menu:
    print(item)

# 반복문에 많이 사용하는 함수 : range()
for i in range(1,101): # range(시작, 마지막, 증가값)
    print(i)

for i in range(1,10,2):
    print(i)

for i in range(10, 1, -1):
    print(i)