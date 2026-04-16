parking = []
top = 0
parking.append("자동차 A")
top += 1
parking.append("자동차 B")
top += 1
parking.append("자동차 C")
top += 1

print(parking)
print(f"top = {top}")

outCar = parking.pop()
top -= 1
print(outCar)
outCar = parking.pop()
top -= 1
print(outCar)
outCar = parking.pop()
top -= 1
print(outCar)

#스택 활용 : 문자열을 거꾸로 출력할 때
word = input('문자열 : ')
# 문자열을 리스트로 변환 => list()
wlist = list(word)
print(wlist)

result = []
for i in range(len(wlist)):
    result.append(wlist.pop())
print(result)
print(f'word 문자열을 거꾸로 출력 = {word[::-1]}')