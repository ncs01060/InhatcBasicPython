def circle_area(r):
    return 3.14 * (r ** 2)

def circle_length(r):
    return (2 * r) * 3.14

while True:
    a = int(input("원의 반지름을 입력하세요 >> "))
    if a < 1:
        break
    print("반지름이", a ,"인 원의 넓이는" , circle_area(a), "이고 둘레의 길이는 ", round(circle_length(a),1),"입니다.")