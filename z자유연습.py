# from random import*

# date = randint(4,28)
# print('스터디 모임은 매월', date, '일로 결정되었습니다')

# jumin = '1234567'
# print(jumin[2])

# python = 'Pyton is Amazing'
# index = python.index('n')
# index = python.index('n', index + 1)
# print(index)

# name='young min'
# index = name.index('n')
# index = name.index('n', index + 1)
# print(index)

# url = 'http://google.com'
# password = url[7:10] + str(len(url[7:12])) + str(url.count('n')) + '!'
# print('생성된 비밀번호는 :', password, '입니다' )


# # -모범답안-
# url = 'http://google.com'
# url = url.replace('http://', '')
# url = url[:url.index('.')]
# password = url[:3] + str(len(url)) + str(url.count('e')) + '!'
# print(password)


# subway = ['유재석', '정형돈', '조세호', '하하', '유재석']



# menu = {'커피', '우유', '주스'}
# print(type(menu))

# from random import*

# users = range(1,21)
# users = list(users)
# winners = sample(users,4)
# print(winners)



# print('-- 당첨자 발표 --')
# print('치킨 당첨자 :', str(winners[0]))
# print('커피 당첨자: ', str(winners[1:4]))
# print('-- 축하합니다 --')

# #모범답안
# print('-- 당첨자 발표 --')
# print('치킨 당첨자 : {0}'.format(winners[0]))
# print('커피 당첨자: {0}' .format(winners[1:]))
# print('-- 축하합니다 --')

# weather = '비'
# if weather == '비':
#     print('우산을 챙기세요')

# temp = int(input('기온이 어때요'))
# if 30<=temp:
#     print('더워요')
# if 10<=temp<30:
#     print('괜찮은 날씨에요')

# nobook = [7]
# for student in range(1, 11):
#     if student in nobook:
#         print('여기까지.{0}, 따라와' .format(student))
#         break
#     else:
#         print('{0}, 책을 읽어봐'.format(student))

# from random import*
# count = 0
# for customer in range(1,51):
#     time = randrange(5,51)
#     if time<=15:
#         print('[O], {0}번째 손님 (소요시간: {1}분)'.format(customer, time))
#         count = count+1
#     else:
#         print('[ ], {0}번째 손님 (소요시간: {1}분'.format(customer, time))
# print('총 탑승 승객: {0} 명'.format(count))



# from random import*
# count = 0
# for number in range(1,51):
#     time=randrange(5,51)
#     if time<=15:
#         print('[O], {0}번째 손님(소요시간:{1}분)' .format(number,time))
#         count += 1
#     else:
#         print('[X], {0}번째 손님(소요시간:{1}분)'.format(number,time))   
# print(count)

# def deposit(balance, money):
#     print('입금완료. 잔액{0}원'.format(balance+money))
#     return balance+money

# print(deposit(1000,2000))

# def profile(name='김영민', age=17, main_lang='파이썬'):
#     print('이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}'\
#         .format(name, age, main_lang), end='')
#     print('asd')

# profile(1,2,3)


# print('ddd', end='')
# print('dfg')

# def profile(name,age,*language):
#     print('이름:{0}\t나이:{1}\t\t언어:'.format(name,age), end='')
#     for lang in language:
#         print(lang,'\t', end='')
#     print()

# profile('영민',25,'파이썬', '자바', '씨언어')

# gun=999
# def checkpoint(gun, soldiers):
#     gun=gun-soldiers
#     print('남은 총:{0}'.format(gun))
#     return gun

# checkpoint(gun,2)
# print(gun)

# def weight(gender, height):
#     if gender =='남자':
#         return round((((height/100)**2)*22),2)
#     else:
#         return round((((height/100)**2)*21),2)

# height=176
# gender='남자'
# std_weight=weight(gender, height)

# print('키{0}cm {1}의 표준 체중은{2}kg 입니다'.format(height,gender,std_weight))


# gun=1000
# def checkpoint(soldiers):
#     global gun #전역변수
#     gun=gun-soldiers
#     print('남은 총:{0}'.format(gun))

# def checkpoint_ret(gun, soldiers):
#     gun=gun-soldiers
#     print('남은 총:{0}'.format(gun)) #지역변수
#     return gun

# print(gun)
# checkpoint_ret(gun,3)
# print(gun)

# print('{0:^>+2 0,.6f}'.format(5000/3))


# score_file = open('score.txt', 'w', encoding = 'utf8')
# print('수학 : 0', file=score_file)
# print('영어 : 50', file=score_file)
# score_file.close()

# score_file = open('score.txt', 'a', encoding='utf8')
# score_file.write('과학 : 80')
# score_file.write('\n코딩 : 100')
# score_file.close()

# score_file = open('score.txt', 'r', encoding='utf8')
# print(score_file.read())
# score_file.close()

# score_file = open('score.txt', 'r', encoding='utf8')
# print(score_file.readline(), end='')
# print(score_file.readline(), end='')
# print(score_file.readline(), end='')
# print(score_file.readline(), end='')
# score_file.close()

# score_file = open('score.txt', 'r', encoding='utf8')
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end='')
# score_file.close()

# score_file = open('score.txt', 'r', encoding='utf8')
# lines = score_file.readlines()
# for line in lines:
#     print(line, end='')

# score_file = open('score.txt', 'w', encoding = 'utf8')
# print('수학 : 0', file=score_file)
# print('영어 : 50', file=score_file)
# score_file.close()

# score_file = open('score.txt', 'a', encoding='utf8')
# score_file.write('과학 : 80')
# score_file.write('\n코딩 : 100')
# score_file.close()

# score_file = open('score.txt', 'r', encoding='utf8')
# print(score_file.readline())

# import pickle
# profile_file=open('profile.pickle', 'wb')
# profile=['김영민','25','코딩']
# print(profile)
# pickle.dump(profile, profile_file)
# profile_file.close()

# profile_file = open('profile.pickle', 'rb')
# profile = pickle.load(profile_file)
# print(profile)
# profile_file.close()




# for i in range(1,51):
#     with open(str(i)+'주차.txt','w',encoding='utf8') as week_report:
#         week_report.write('-{0}주차 주간보고-'.format(i))
#         week_report.write('\n부서 :')
#         week_report.write('\n이름 :')
#         week_report.write('\n업무요약 :')

#일반유닛
# class Unit:
#     def __init__(self,name,hp,speed):
#         self.name=name
#         self.hp=hp
#         self.speed=speed
#         print('{0}유닛이 생성됨, 체력:{1}'.format(self.name, self.hp))

#     def move(self,location):
#         print('[지상유닛 이동], {0}:{1} 방향으로 이동합니다.(속도:{2})'\
#             .format(self.name,location,self.speed))
    
#     def damaged(self, damage):
#         self.hp -= damage
#         print('{0}:{1}데미지를 입었습니다. 남은 체력은 {2} 입니다'\
#             .format(self.name, damage, self.hp))
#         if self.hp <=0:
#             print('{0}:파괴되었습니다'.format(self.name))

# #공격유닛
# class AttackUnit(Unit):
#     def __init__(self,name,hp,damage,speed):
#         Unit.__init__(self, name, hp, speed)
#         self.damage=damage
#         print('{0}유닛이 생성됨. 체력:{1}, 공격력:{2}'\
#             .format(self.name, self.hp, self.damage))

#     def attack(self, location):
#         print('{0} : {1}시 방향으로 적을 공격합니다. 공격력:{2}'\
#             .format(self.name,location, self.damage))

# #공중유닛
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
#     def fly(self, name, location):
#         print('{0}:{1} 방향으로 날아갑니다 (속도:{2})'\
#             .format(name,location,self.flying_speed))

# #공중 공격유닛
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage)
#         Flyable.__init__(self, flying_speed)

# #마린
# class Marine(AttackUnit):
#     def __init__(self):
#         AttackUnit.__init__(self,'마린',40,1,5)

#     def stimpack(self):
#         if self.hp >10:
#             self.hp -= 10
#             print('{0}:스팀팩 사용 (hp 10 감소)'.format(self.name))
#         else:
#             print('{0}:체력부족, 스팀팩 사용 불가'.format(self.name))

# #탱크
# class Tank(AttackUnit):
#     seize_developed = False

#     def __init__(self):
#         AttackUnit.__init__(self,'탱크',150,1,35)
#         self.seize_mode = False

#     def set_seize_mode(self):
#         if Tank.seize_developed == False:
#             return

#         if self.seize_mode == False:
#             print('{0}:시즈모드 전환'.format(self.name))
#             self.damage *= 2
#             self.seize_mode == True
#         else:
#             print('{0}:시즈모드 해제'.format(self.name))
#             self.damage %= 2
#             self.seize_mode == False

# #레이스
# class Wraith(FlyableAttackUnit):
#     def __init__(self):
#         FlyableAttackUnit.__init__(self,'레이스',80,20,5)
#         self.clocked = False

#     def clocking(self):
#         if self.clocked == True
#         print('{0}:클로킹 모드 해제'.format(self.name))
#         self.clocked == False
#         else:
#         print('{0}:클로킹 모드 활성화'.format(self.name))
#         self.clocked == True

# def game_start():
#     print('[알림] 새로운 게임을 시작합니다')

# def game_over():
#     print('Player : GG')
#     print('[Player]님이 게임에서 퇴장하셨습니다')



# class House:
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year

#     def show_detail(self):
#         print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

# product1 = House('강남', '아파트', '매매', '10억', '2010년')
# product2 = House('마포', '오피스텔', '전세', '5억', '2007년')
# product3 = House('송파', '빌라', '월세', '500/50', '2000년')

# products = []
# products.append(product1)
# products.append(product2)
# products.append(product3)

# print('총 {0}개의 매물이 있습니다'.format(len(products)))
# for product in products:
#     product.show_detail()

# try:
#     print('한자리 숫자 나누기 계산기')
#     num1 = int(input('첫 번째 숫자를 입력하세요 :'))
#     num2 = int(input('두 번째 숫자를 입력하세요 :'))
#     if num1 >= 10 or num2 >= 10:
#         raise ValueError
#     print('{0}/{1}={2}'.format(num1,num2,int(num1/num2)))
# except ValueError:
#     print('잘못된 값을 입력하였습니다. 한자리 숫자만 입력하세요')


# class SoldOutError(Exception):
#     pass

# chicken = 10
# waiting = 1
# while(True):
#     try:
#         print('남은 치킨:{0}'.format(chicken))
#         order = int(input('치킨 몇마리 주문하시겠습니까?'))
#         if order > chicken:
#             print('재료가 부족합니다')
#         elif order <= 0:
#             raise ValueError
#         else:
#             print('대기번호{0}, {1}마리 주문이 완료되었습니다'.format(waiting,order))
#             waiting += 1
#             chicken -= order
        
#         if chicken == 0:
#             raise SoldOutError

#     except ValueError:
#         print('숫자를 제대로 입력 해주세요')
#     except SoldOutError:
#         print('재고가 소진되었습니다')
#         break

# import theater_module as abc
# abc.price(3)

# from theater_module import price as bakaji
# bakaji(3)



# a = {'A':90, 'B':80, 'C':70}
# a=list(a)
# print(a)
# a.remove('B')
# print(a)
# a.pop(0)
# print(a)
# del a[0]
# print(a)


# a = [1,1,1,2,2,3,3,3,4,4,5]
# print(a)
# aSet = set(a)
# print(aSet)
# a = list(aSet)
# print(a)

# a=b=[1,2,3]
# a[1] = 4
# print(a)
# print(b)

# money = True
# if money:
#     print('asdf')

# if 1 in [1,2,3]:
#     print('ㅇㅇ')

# a = input('입력하세요')
# print(a)

# class Fourcal:

#     def __init__(self,first,second):
#         self.first = first
#         self.second = second

#     def add(self):
#         result = self.first + self.second
#         return result
        
#     def sub(self):
#         result = self.first - self.second
#         return result

#     def mul(self):
#         result = self.first * self.second
#         return result

#     def div(self):
#         result = self.first / self.second
#         return result




# class MoreFourcal(Fourcal):
#     def pow(self):
#         result = self.first ** self.second
#         return result





# import random
# print(random.randint(1,11))

# import random as abc
# print(abc.randint(1,11))

# from random import randint 
# print(randint(1,11))

# from random import* 
# print(randint(1,11))


# import mod1
# print(mod1.add(3,4))

# import mod1 as x
# print(x.add(3,4))

# from mod1 import add, sub
# print(add(3,4))

# from mod1 import*
# print(add(3,4))

# from mod2 import*
# print(PI)
# a = Math()
# print(a.solv(2))

# import mod2
# a=mod2.Math()
# print(a.solv(2))




# def gugu(a):
#     result = []
#     result.append(a*1)
#     result.append(a*2)
#     result.append(a*3)
#     result.append(a*4)
#     result.append(a*5)
#     result.append(a*6)
#     result.append(a*7)
#     result.append(a*8)
#     result.append(a*9)
#     print(result)

# def gugu(a):
#     result = []
#     for i in range(1,10):
#         result.append(a*i)
#     print(result)
# gugu(3)




# mul3 = []
# mul5 = []
# a=1
# while a*3 < 1000 :
#     mul3.append(a*3)
#     a += 1
# a=1
# while a*5 < 1000:
#     mul5.append(a*5)
#     a += 1
# x = mul3 + mul5
# x = set(x)
# x = list(x)
# result = 0
# for i in x:
#     result += i
# print(result)





# result = 0
# for n in range(1,1000):
#     if n%3 == 0 or n%5 == 0:
#         result += n
# print(result)



# def getTotalPage(m,n):
#     if  m%n == 0:
#         print(m//n)
#     else:
#         print(m//n+1)

# getTotalPage(99,10)


# print(sorted('doughnut'))

# import webbrowser
# webbrowser.open('google.com')

# class Calculator:
#     def __init__(self):
#         self.value = 0

#     def add(self, val):
#         self.value += val

# a = Calculator()
# a.add(3)
# print(a.value)

# class UpgradeCalculator(Calculator):
#     def minus(self, val):
#         self.value -= val

# cal = UpgradeCalculator()
# cal.add(10)
# cal.minus(7)
# print(cal.value)

# class MaxLimitCalculator(Calculator):
#     def add(self, val):
#         self.value += val
#         if self.value >100:
#             self.value = 100

# b = MaxLimitCalculator()
# b.add(90)
# print(b.value)



# list = [0,1]
# a = 0
# while a < 100:
#     list.append(list[a]+list[a+1])
#     a += 1


# def fivo(i):
#     print(list[0:i+1])

# fivo(5)

# def add(*nums):
#     result = 0
#     for i in nums:
#         result += i
#     print(result)

# add(65,45,2,3,45,8)

# list = []

# def gugu(a):
#     for i in range(1,10):
#         list.append(a*i)
#     print(list)

# gugu(2)

# a = open('abc.txt', 'w')
# a.write('AAA')
# a.write('\nBBB')
# a.write('\nCCC')
# a.write('\nDDD')
# a.write('\nEEE')
# a.close()

# f = open('abc.txt', 'r')
# lines = f.readlines()
# f.close()

# lines.reverse()

# f=open('abc.txt', 'w')
# for line in lines:
#     line = line.strip()
#     f.write(line)
#     f.write('\n')
# f.close()

# f = open('sample.txt', 'r')
# lines = f.readlines()
# f.close()
# print(lines)

# result = 0
# for i in lines:
#     i.strip()
#     result += int(i)
# print(result)

# f = open('result.txt', 'w')
# f.write(str(result/len(lines)))
# f.close()

# class Calculator:
#     def __init__(self,numlist):
#         self.numlist = numlist

#     def sum(self):
#         result = 0
#         for i in self.numlist:
#             result += i
#         return result

#     def avg(self):
#         result = 0
#         for i in self.numlist:
#             result += i
#         return result/len(self.numlist)


        

# a = Calculator([1,2,3,4,5])
# print(a.avg())

# b = Calculator([6,7,8,9,10])
# print(b.avg())

# result =0
# try:
#     # [1,2,3][3]
#     'a'+1
#     4/0
# except TypeError:
#     result += 1
# except ZeroDivisionError:
#     result +=2
# except IndexError:
#     result += 3
# finally:
#     result +=4
# print(result)




# data = 'aaabbcccccca'
# data = list(data)
# result = ''
# for i in range(len(data)+1):
#     repeat = 0
#     while data[i] != data[i+1]:
#         repeat += 1
#         print(data[i]+repeat)





# data = 'aaabbcccccca'
# data = list(data)
# print(data[2])

# result = [1,2,3,4]
# print(','.join(result))



# for i in ('1234'):
# #     print (i)

# def Dashinsert(num):   
#     num = map(int, num)
#     num = list(num)
#     result = []
#     for i in range(0, len(num)):
#         if i<len(num)-1 and num[i]%2 == 0 and num[i+1]%2 == 0:
#             result.append(str(num[i]))
#             result.append('*')
#         elif i<len(num)-1 and num[i]%2 == 1 and num[i+1]%2 == 1:
#             result.append(str(num[i]))
#             result.append('-')
#         else:
#             result.append(str(num[i]))
#     print(''.join(result))


# Dashinsert('334455678899')

# def press(word):
#     word = list(word)
#     result = []
#     repeat = 1
#     for i in range(0,len(word)):
#         if i<len(word)-1 and word[i] == word[i+1]:
#             repeat += 1
#         else:
#             result.append(word[i])
#             result.append(str(repeat))
#             repeat = 1
#     print(''.join(result))

# press('aaabbcccccca')



# def Checknum(num):
#     num = map(int, num)
#     num = list(num)
#     result = []
#     for i in range(0,10):
#         if len(num) == 10 and num[i] not in result:
#             result.append(num[i])
            
#         else:
#             return False

#     return len(result) == 10            

# print(Checknum('1234567890'))

# dic = {'.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F','--.':'G','....':'H',\
# '..':'I','.---':'J','-.-':'K','.-..':'L','--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q',\
# '.-.':'R','...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X','-.--':'Y','--..':'Z'}

# def MorsetoEng(code):

#     code = code.replace(' ', '*')  # .... .**... .-..**.**.**.--.
#     codelist = code.split('*')
#     result = []
#     print(codelist)
#     for i in range(0,len(codelist)):
#         if codelist[i] in dic:
#             print(dic[codelist[i]], end='')
#         else:
#             print(' ', end = '')
        

# MorsetoEng('.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--')


# dic2 = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',\
# 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-'\
# , 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', ' ' : '   '}

# def EngtoMorse(eng):
#     eng = list(eng)
#     result = []
#     print(eng)
#     for i in range(0,len(eng)):
#         if eng[i] in dic2:
#             print(dic2[eng[i]], end='   ')
        
    

# EngtoMorse('ABCDEFG')


