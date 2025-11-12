'''
Python Operators
'''
#1.Arithmetic operators
a=20
b=10
print("a+b:",a+b)#a+b: 30
print("a-b:",a-b)#a-b: 10
print("a*b:",a*b)#a*b: 200
print("a/b:",a/b)#a/b: 2.0
print("a//b:",a//b)#a//b: 2
print("a%b:",a%b)#a%b: 0
print("a**b:",a**b)#a**b: 102400000000
#2.Comparsion Operators
c=30
d=40
print('c<d:',c<d)#c<d: True
print('c>d:',c<d)#c>d: False



print('c<=d:',c<d)#c<=d: True
print('c>=d:',c<d)#c>=d: False
print('c!=d:',c<d)#c!=d: True
print('c==d:',c<d)#c==d: False
#3.Assignment Operators
'''
var = var op val
var op=val
'''
e=100
e+=100
print('e+=100:',e)
e-=100
print('e-=100:',e)
e*=100
print('e*=100:',e)
e/=100
print('e/=100:',e)
e//=100
print('e//=100:',e)
e%=100
print('e%=100:',e)
e**=100
print('e**=100:',e)
#output:
#e+=100: 200
#e-=100: 100
#e*=100: 10000
#e/=100: 100.0
#e//=100: 1.0
#e%=100: 1.0
#e**=100: 1.0
#4.Logical Operators:
x=100
y=50
print("x%20==0 and y%20==0 :",x%20==0 and y%20==0)
print("x%20==0 or y%20==0 :",x%20==0 or y%20==0)
print("not x%20==0:",not x%20==0)
print("not y%20==0:",not y%20==0)
#output:
#x%20==0 and y%20==0 : False
#x%20==0 or y%20==0 : True
#not x%20==0: False
#not y%20==0: True
#5.Membership operator(in,notin)
s="python programming"
print("'i' in s: ",'i' in s)
print(" 'x' not in s:","x" not in s)
l=[1,2,3,4,5]
print(" 3 in l:",3 in l)
print("10 not in l:",10 not in l)
t=(10,20,30,40,50)
print("108 in t:",108 in t)
print("104 not in t:",104 not in t)
s={10,20,30,40}
print("40 in s:",40 in s)
print("50 not in s:",50 not in s)
d={1:1,2:4,3:9,4:16,5:25}
print("1 in d:",1 in d)
print("9 in d:",2 in d)
#output:
#'i' in s:  True
#'x' not in s: True
#3 in l: True
#10 not in l: True
#108 in t: False
#104 not in t: True
#40 in s: True
#50 not in s: True
#1 in d: True
#9 in d: True
#6.identity operator(is,is not)
a=[1,2,3,4]
b=[1,2,3,4]
print('a is b:',a is b)
c=a
print('a is c:',a is c)
print('id(a):',id(a))
print('id(b):',id(b))
print('id(c):',id(c))
print('a is not b:',a is not b)
print('a is not c:',a is not c)
#output:
#a is b: False
#a is c: True
#id(a): 2684704137280
#id(b): 2684705354176
#id(c): 2684704137280
#a is not b: True
#a is not c: False
#7.Bitwise operators(& | ^ ~ << >>)
'''^-Gate    
0-0
11-0
10-1
01-1
~ Gate
0-1
1-0
<<-operator
8<<2-1000
100000-32
>>-operator
16>>2-4
'''
print("11|12:",11|12)
print("4&5:",4&5)
print("0^10:",0^1)
print('~16:',~16)
print("8<<1:",8<<1)
print("16>>2:",16>>2)
#output:
#11|12: 15
#4&5: 4
#0^10: 1
#~16: -17
#8<<1: 16
#16>>2:4