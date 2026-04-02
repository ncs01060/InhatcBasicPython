num = int(input("출력한 구구단의 숫자를 입력하세요(2~9) : "))
print("=== 구구단" ,num , "단 ===")
for i in range(1,10):
    print(num, "*", i, "=", num*i)
