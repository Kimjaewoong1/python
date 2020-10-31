class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class Flyableunit(Unit, Flyable): #unit과 flyable을 상속받음 super을 사용하면 뒤의 flyable이 상속받음
    def __init__(self):
        super().__init__()

#드랍쉽
dropship = Flyableunit()

def stimpack(self):
    # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능, 이동 불가.
    seize_developed = False

    def __init__(self):
        AttackUnit.__Unit_