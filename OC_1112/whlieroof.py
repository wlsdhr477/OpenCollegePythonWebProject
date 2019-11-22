sum=0
n=0

while n<11:
    sum=sum+n
    n=n+1

print(sum)
print(n)

#break 여기까지 처리하겠다./continue이번 처리는 Skip하고 그 다음 처리 반복
n=0
while n<10:
    n = n + 1
    if n==3:
        continue
    print("현재 n은" + str(n) + "입니다.")
    if n==5:
        break
    print("현재 n은 " + str(n) + "입니다.")

#List Comprehension
#특정 List에 대한 조작을 심플한 for문으로 표현할 수 있다!

names=["신봉건", "고유빈", "김진옥", "이광우"]
nimNames = []

for name in names:
    nimNames.append(name+"님")

for nimName in nimNames:
    print(nimName)
    
print("+++++++++++++++++++++++++++++++++++")
nimNames2 = [ name + "님" for name in names]

for nimName4 in nimNames2:
    print(nimName4)

#min/max
print("+++++++++++++++++++++++++++++++++++")
numbers = [1, 100, -1, 30, 5, 99, 45, 30, -2, -10]

for i in numbers:

    
