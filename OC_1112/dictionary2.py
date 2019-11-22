a = {'김도한' : '010-7188-7777', '신봉건' : '010-9798-8888'}

for name in a:
    print(name)

#for 상자 in (list, tuple, string, dictionary)
#iterable 변수

for key in a.keys():
    print(key)

for item in a.items():
    print(item)

#반복하고싶은 걸 for 안에 넣는데 얼마만큼 반복할건지(range) range 10을 넣으면 박스 10개 구해와서 순서대로
a=range(10)

for i in a:
    print(i)

#