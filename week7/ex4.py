# 큐 자료구조 - 먼저 들어간 데이터가 먼저 나오는 구조(FIFO)
# 리스트를 이용해서 큐 구조 구현
parking = []
top = 0
parking.append("자동차 A")
top += 1
parking.append("자동차 B")
top += 1
parking.append("자동차 C")
top += 1

print(parking)
print(top)

for i in range(len(parking)):
    outCar = parking.pop(0)
    print(outCar)

