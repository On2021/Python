#-*- coding: utf-8 -*-
'''
Created on 2022. 8. 11.

@author: dhkdr
'''

#출력
print(10)
print('10')
print("10")

#문자 출력시 작은 따옴표/큰 따옴표 사용 (구분x)
print('abc')
print("abc")

#한글처리는 1행에 #-*- coding: utf-8 작성해주기
##-*- coding: utf-8 -*-도 사용가능
print('가나다')
print("가나다")

#문자열 여러개를 연결해서 쓸 때는 쉼표를 이용할 수 있음
print('오늘은 즐거운 월요일 입니다.')
print('오늘은','즐거운','월요일','입니다.')
print('오늘은'+'즐거운'+'월요일'+'입니다.')
print('오늘은''즐거운''월요일''입니다.')

#print에는 기본적으로 엔터가 포함되어 있습니다.
print(10,end='\n') #기본 설정
print(10,end=' ') #따로 설정 가능(띄어쓰기 설정)
print(end='\n')

#파이썬에서는 변수선언을 따로 하지 않습니다. String a = '가나다' (x)
a = '가나다'
print('a=',a)

#여러줄의 문자열을 변수에 넣고싶을 때
b = '''재미있는
파이썬
수업시간'''
print(b)

#숫자+, 문자+
print(1+2) #숫자 처리가 되서 연산 결과가 나옴 (3)
print('1'+'2') #문자 연결 처리가 되서 연결된 문자열이 나옴 (12)

#숫자 => 문자로 변환 : str
#print('ab'+34) #TypeError: can only concatenate str (not "int") to str
print('ab'+'34') #ab34
print(int('12')+34) #46

#서식문자 관련
# %d : 정수 출력할 때 사용하는 서식문자입니다.
# %f : 실수 출력할 때 사용하는 서식문자입니다.
# %s : 문자열 출력할 때 사용하는 서식문자입니다.
print('%d + %d = %d' % (10,3,10+3))
# print('%d/%d=%d') % (10,3,10/3) #TypeError: unsupported operand type(s) for %: 'NoneType' and 'tuple' 
print('%d / %d = %d' % (10,3,10/3)) #10 / 3 = 3 => 정수값으로 출력
print('%d / %d = %f' % (10,3,10/3)) #10 / 3 = 3.333333 => 실수값으로 출력
print('%d / %d = %.2f' % (10,3,10/3)) #10 / 3 = 3.33 => 소수점 두자리수 까지 출력
print('%s' %a) #가나다
print('%5s' %a) #  가나다
