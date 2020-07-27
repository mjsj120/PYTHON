#다중 상속 코드를 작성했을 때, super() 를 쓰면 순서상 맨 "마지막" 이 아닌, 맨 "처음" 클래스(예제에서는 Flyable) 에 대해서 __init__ 함수가 호출된다.
class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        super().__init__()

#드랍쉽
dropship = FlyableUnit()
# Unit 생성자


class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        super().__init__() 

#드랍쉽
dropship = FlyableUnit()
#Flyable 생성자


class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        super().__init__() 
        Unit.__init__(self)
        Flyable.__init__(self)

#드랍쉽
dropship = FlyableUnit()
# Unit 생성자
# Flyable 생성자