
# Human 이라는 Class가 있고
# 그 Class 이용하여 김도한이라는 Object를 생성한 것!
# Constructor 를 이용하여 Object를 만들 수 있습니다.
# 클레스안에 정의되어있는거 필드이자 멤버변수
# 그리고 그 밑에 함수같은건 메소드라 부른다.
class Human:
    def __init__(self, name, age, gender, height, blood):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.blood = blood

    def introduceMySelf(self):
        print("제 이름은", self.name, "이고 나이는", self.age, "입니다.")

Jinok = Human("김도한", 20, "Male", 179, "AB")
YusunJung = Human("정유선", 31, "Female", 168, "O")

Jinok.introduceMySelf()
YusunJung.introduceMySelf()