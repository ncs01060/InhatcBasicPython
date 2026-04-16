# 동물명 영어사전

animals = {'강아지':'dog',"고양이":"cat",'새':'bird','코끼리':'elephant','물고기':'fish','양':'lamb','호랑이':'tiger'}
while True:
    a = input('동물이름(한글) : ')
    if a == "끝":
        break


    result = animals.get(a)
    if result:
        print(f'{a} = {result}')
    else:
        print(f"없음")
