from random import *

date = randint(4,28)
print("오프라인" + str(date) + "입니다.")

python = "Python is amazing"

index = python.index("n")
print(index)
index = python.index("n", index+1)
print(python.find("java")) #find는 원하는값이 없을때 -1 반환

print("백문이 불여일견\n백견이 불여일타")

url = "http://naver.com"
my_str = url.replace("http://","")
#print(my_str)
my_str = my_str[:my_str.index(".")]
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print(password)

subway= ["유재석","조세호","박명수"]

print(subway.index("조세호"))

subway.insert(1,"정형돈")
print(subway)

num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)

num_list.clear()
print(num_list)

cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet.get(5,"사용 가능")) #5가있으면 5 출력 없으면 사용가능 출력
print(3 in cabinet) #true
print(5 in cabinet) #false

print(cabinet)
cabinet["C"] = "김종국"
print(cabinet)

del cabinet[100]
print(cabinet)

print(cabinet.keys())

print(cabinet.items()) #쌍으로 출력하기

#목욕탕 폐점
cabinet.clear()
print(cabinet)

#tuple 변경이나 수정불가 대신 속도가 빠름

menu = ("돈가스","치즈까스")
print(menu[0])
print(menu[1])

name = "김종국"
age = "20"
hobby =" 노래"
print(name + age + hobby)

name, age, hobby = ("김종국", 20, "코딩")
print(name, age, hobby)

#집합(set) 중복안됨, 순서없음
my_set = {1,2,3,4,4}
print(my_set)

java = {"유재석","김태호","양세형"}
python = set(["유재석","박명수"])

#교집합(java, python 모두 출력)
print(java & python)
print(java.intersection(python))

#합집합
print(java | python)
print(java.union(python))

#차집합
print(java - python)
print(java.difference(python))

# python을 할줄 아는 사람이 늘어남
python.add("김태호")
print(python)

#java를 까먹었어요
java.remove("김태호")
print(java)

#자료형이 변환
menu = {"커피","우유","주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))
print(menu, tuple(menu))

from random import *
lst = range(1, 21) #1부터 21 직전까지 숫자를 생성. list가 아님
lst = list(lst)
print(lst)
shuffle(lst)
print(lst)
print(sample(lst,1)) #lst중에서 1개를 샘플로 뽑겠다.

winners = sample(lst, 4) #4명중에서 1명은 치킨 3명은 커피
print("치킨 당첨자: {0}".format(winners[0]))
print("커피 당첨자: {0}".format(winners[1:]))

'''temp = int(input( '기온이 어때요?'))
if 30<= temp:
    print("너무 더워요")
elif 30>temp>203:
    print("그저 그래요")
else:
    print("글쎄요")
'''

for waiting_no in range(1,6):
    print("대기번호: {0}".format(waiting_no))

starbucks = ["아이넌맨", "토르","그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비돼었습니다.".format(customer))

#while
customer = "토르"
index = 5
while index >=1 :
    print("{0}, 커피가 준비되었습니다. {1} 번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기되었습니다.")

'''
customer = "아이언맨"
index = 1
while True:
    print("{0}, 커피가 준비되었습니다. 호출{1}회.".format(customer, index))
'''

customer = "토르"
person = "Unknown"

absent =[2,5]
no_book = [7] #책을 깜박함
for student in range(1,11):
    if student in absent:
        continue #다음 반복으로 이어서 실행시킴
    elif student in no_book:
        print("오늘 수업은 여기까지. {0}은 교무실로 따라와".format(student))
        break;
    print("{0},책을 읽어봐".format(student))

# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101 102 103 104
student = [1,2,3,4,5]
print(student)
student = [i+100 for i in student]
print(student)

#학생 이름을 길이로 변환
student = ["Iron man", "Thor","grout"]
student = [len(i) for i in student]
print(student)

def open_account():
    print("새로운 계좌가 생성되었습니다.")

open_account()


def deposit(balancem, money):
    print("{0}은 {0}입니다. money는 {1}입니다.".format(balance, money))
    return balance + money

def withdraw(balance, money): #출금
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
        return balance

def withdraw_night(balance, money):
    commision = 100
    return commision, balance - money - commision

balance = 0
money = 2000
balance = (deposit(balance, 1000))
print(balance)
commision, balance = withdraw_night(balance, 500)
print("수수료는 {0}원이며, 잔액은 {1}원입니다.".format(money, balance))

def profile(name, age=17, main_lang="자바"):
    print("이름: {0}\t나이: {1}\t주 사용 언어: {2}".format(name, age, main_lang))


#profile("유재석", 20, "파이썬")
#profile("김태호", 25, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업


'''profile("유재석")

def profile(name, age, lang1, lan2, lang3, lang4, lang5):
    print("이름 : {0}\t나이: {1}".format(name, age), end= " ")
    print(lang1, lang2, lang3, lang4, lang5)

profile("유재석", 20, "python", "java", "c,", "c++")
profile("김태호", 25, "kotlin", "swift", "","","")'''

print("python", "java", "javascript", sep=",", end="?")# end는 한줄로 다음문장과 사용하고 싶을때 사용
print("무어싱 더 재밌을까요??")

import sys
print("Python", "java", file=sys.stdout)
print("Python", "java", file=sys.stderr)#표준에러로 처리되는 부분 찾아내기(에러처리)

scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    #print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")

#은행 대기순번표
# 001, 002, 003, 004...
for num in range(1, 21):
    print("대기번호:" +str(num).zfill(3)) # zfill() 빈공간에는 0을 채운다

#answer = input("아무값이나 입력하세요:")
#print("입력하신 값은" + answer + "입니다.")

# 빈자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))

print("{0: >+10}".format(500))
#<는 왼쪽정렬 ,는 3자리마다 출력하기
print("{0:^<+30,}".format(10000000000))

'''score_file = open("score.txt", "w", encoding="utf8")#덮어서 작성하기
print("수학: 0", file = score_file)
print("영어: 50", file = score_file)
score_file.close()
'''

score_file = open("score.txt", "a", encoding="utf8")# 이어서 작성하기
score_file.write("과학 : 80")
score_file.write("/코딩: 100")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")#한번에 읽어서 다 출력
print(score_file.read())
score_file.close

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline())#줄별로 읽기, 한 줄로 읽고 커서는 다음 줄로 이동
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close

score_file = open("score.txt", "r", encoding="utf8")
while 1:
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()

#데이터를 파일 형태로 사용
import pickle
'''
profile_file = open("profile.pickle", "wb")
profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프"]}
print(profile)
pickle.dump(profile, profile_file) #profile에 있는 정보를 file에 저장
profile_file.close()
'''

profile_file = open("profile.pickle", "rb") #profile_file을 가져오기
profile = pickle.load(profile_file)
print(profile)
profile_file.close()

with open("study.txt", "w", encoding="utf-8" ) as study_file:
    study_file.write("안녕하세요")

with open("study.txt", "r", encoding="utf-8") as study_file:
    print(study_file.read())

#마린 : 공격 유닛, 군인, 총을 쏠 수 있음

name = "마린" #유닛의 이름
hp = 40
damage = 5

print("{}유닛이 생성되었습니다,".format(name))
print("체력이 {}, 공격력{}".format(hp,damage))

#탱크: 공격유닛, 탱크, 포를 쏠 수 있는데, 일반모드, 시즈모드.
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{0} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format( name, location, damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.damage = damage
        self.hp = hp
        print("{0}유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 =Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)

wraith1 = Unit("레이스", 80, 5)
print("유닛 이름: {0} ,공격력 : {1}".format(wraith1.name, wraith1.damage))

wraith2 = Unit("레이스" ,80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태 입니다.".format(wraith2.name))

class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack (self, loaction):
        print("{0} : {1}방향으로 공격합니다. [공격력은 {2}] 입니다.\n".format(self.name, loaction, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0}유닛은 파괴되었습니다.".format(self.name))  

firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25)

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1}방향으로 날아갑니다. [속도{2}]".format(name, loaction, self.flying_speed))

#공중 공격 유닛 클라스 
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

#발키리 : 공중공격 유닛
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__("레이스", 80, 20, 5)
        self.clocked = False #클로킹 모드 (해제 상태)

    def clocking(self):
        if self.clocked == True: # 클로킹 모드 -> 모드 해제
            print("{0} : 클로킹 모드 해제 합니다.".format(self.name))
            self.clocked = True
def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Player : gg" ) # good gmae
    print("[Player]님이 나가셨습니다.")

game_start()

m1=Marine()
m2=Marine()
m3=Marine()

t1 = Tank()
t2 = tank()

w1 = Wraith()

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

for unit in attack_units:
    unit.move("1시")

for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()
        
# 게임 종료
game_over()

