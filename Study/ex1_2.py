#-*- incoding: utf-8
'''
Created on 2022. 8. 11.

@author: dhkdr
'''


#값을 입력받아서 출력
name = input('이름을 입력하세요: ')
print('name:'+name)

#입력받은 값은 문자타입이다.
age = input('나이를 입력하세요: ')
print('age:'+age) #문자로 출력(+)
#입력받은 (문자)수를 숫자로 바꾸고 싶을 때~
age2 = int(input('나이2를 입력하세요: '))
#print('age2:'+age2) #TypeError: can only concatenate str (not "int") to str
print('age2:',age2) #숫자로 출력(,)
print(type(age)) #<class 'str'>
print(type(age2)) #<class 'int'>

#실습 : 서식문자 이용해서 이름은 아이유이고, 나이는 30살 입니다. 출력
name = input('이름: ')
age = input('나이: ')
#age = int(input('나이: '))
#print('%d', %age) SyntaxError: invalid syntax

#내답안
#print('이름은 %s' %name +'이고,', end=' ')
#print('나이는 %d' %age +'살 입니다')

#방법1
print('이름은 %s이고, 나이는 %s입니다.' %(name,age))
#print('이름은 %s이고, 나이는 $s입니다.' %(name,age))
#TypeError: not all arguments converted during string formatting

#방법2
age= int(age)
print('이름은 %s이고, 나이는 %d입니다.' %(name,age))

#방법3
print('이름은 {}이고, 나이는 {}입니다.'.format(name,age))

#방법4
print('이름은 {0}이고, 나이는 {1}입니다.'.format(name,age))

#방법5
print('이름은 {name}이고, 나이는 {age}입니다.'.format(name='아이유',age=30))
