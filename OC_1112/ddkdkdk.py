menu = {"라면":4000, "만두":3500,"보쌈":28000}

while True:
    b= input("메뉴를 입력하세요")

    if b in menu:
    c=menu[b]
    print(b+"은 "+str(c)+"원 입니다.")
    else:
    print(b+"란 메뉴는 없습니다.")