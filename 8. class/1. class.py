#예시
# 마린 :  공격 유닛, 군이니, 총을 쏠 수 있음
name = "마린" #유닛의 이름
hp = 40 #유닛의 체력
damage = 5 #유닛의 공격력

print("{0} 유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp, damage))


#마린 유닛이 생성되었습니다.
# 체력 40, 공격력 5



#탱크 : 공격 유닛, 탱크, 포를 쏠 수 있는데, 일반모드와 시즈모드(공격력 쎔)가 있음
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{0} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# 마린 유닛이 생성되었습니다.
# 체력 40, 공격력 5

tank2_name = "탱크"
tank2_hp = 150
tank2_damage = 35

print("{0} 유닛이 생성되었습니다.".format(tank2_name))
print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))


def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력{2}]".format( \
        name, location, damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
attack(tank2_name, "1시", tank2_damage)

# 마린 : 1시 방향으로 적군을 공격합니다. [공격력5]
# 탱크 : 1시 방향으로 적군을 공격합니다. [공격력35]
# 탱크 : 1시 방향으로 적군을 공격합니다. [공격력35]

#class

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

# 마린 유닛이 생성되었습니다.
# 체력 40, 공격력 5
# 마린 유닛이 생성되었습니다.
# 체력 40, 공격력 5
# 탱크 유닛이 생성되었습니다.
# 체력 150, 공격력 35