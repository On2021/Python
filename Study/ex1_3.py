#-*- incording:utf-8
'''
Created on 2022. 8. 11.

@author: dhkdr
'''

#뒤에 괄호()가 있으면 함수래요
#print(), input(), int(), str()

#사칙연산 + 수연산
print(15+6) #21 덧셈
print(15-6) #9 뺄셈
print(15*6) #90 곱셈
print(15/6) #2.5 나눗셈
print(15//6) #2 나눗셈(몫)
print(15%6) #3 나눗셈(나머지)
print(divmod(15,6)) #(2,3) 나눗셈(몫과 나머지)

# +=
a = 20
b = 6
a += b #a = a+b
print('a=',a,'b=',b) #a= 26 b= 6

#승
a2 = 2
b2 = 6
a2 **= b2 #a2 = a2**b2 (2의 6승)
print('a2=',a2,'b2=',b2) #a2= 64 b2= 6
print(a2==b2) #False
print(a2>b2) #True

#동시에 만족할 때는 and (&& 사용불가)
print(a>0 and b>0) #True

#둘 중 하나만 만족할 때는 or (|| 사용불가)
print(a2>0 or b<0) #True

#not연산자 (! 사용불가)
print(not(a>0) and b>0) #False

#문자열 비교 여부
s = "Hello World"
print('World' in s) #True
print('hello' in s) #False
print('hello world' not in s) #True