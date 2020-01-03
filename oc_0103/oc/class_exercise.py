class Car:
    def __init__(self, manufacturer, model, color):
        self.manufacturer = manufacturer
        self.model = model
        self.color = color
        self.fuel = 1000

    def forward(self):
        self.fuel = self.fuel - 50
        print(self.manufacturer, self.model, self.color, "차량 전진중입니다.! 현재 기름양은 : ", self.fuel, "입니다.")
    def backward(self):
        self.fuel = self.fuel - 30
        print(self.manufacturer, self.model, self.color, "차량 전진중입니다.! 현재 기름양은 : ", self.fuel, "입니다.")





class ElectricCar(Car):
    def __init__(self, manufacturer, model, color):
        super().__init__(manufacturer, model, color)
        self.charge = 100

    def forward(self):
        self.charge = self.charge - 10
        print(self.manufacturer, self.model, self.color, "차량 전진중입니다.! 현재 충전잔량은 : ", self.charge, "% 입니다.")
    def backward(self):
        self.charge = self.charge - 5
        print(self.manufacturer, self.model, self.color, "차량 전진중입니다.! 현재 충전잔량은 : ", self.charge, "% 입니다.")

car1 = Car("현대", "흰색", "아반떼")
car2 = Car("BMW", "검은색", "520D")
car3 = Car("Audio", "붉은색", "A7")

car4 = ElectricCar("현대", "흰색", "아반떼")
car5 = ElectricCar("BMW", "검은색", "520D")
car6 = ElectricCar("Audio", "붉은색", "A7")

car1.forward()
car1.backward()
car2.forward()
car2.backward()
car3.backward()
car3.forward()


car4.forward()
car4.backward()
car5.forward()
car5.backward()
car6.backward()
car6.forward()