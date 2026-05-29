Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
'''
operators
---------
art(+,-,*,/,//,%,**)
comparsion(<,>,<=,>=,==,!=)
assignment(=,+=,-=,*=,/=,%=,**=)
logical(and or not )
membership(in not in)
identity(is isnot)
bit(& | ^ ~ << >>)
'''
'\noperators\n---------\nart(+,-,*,/,//,%,**)\ncomparsion(<,>,<=,>=,==,!=)\nassignment(=,+=,-=,*=,/=,%=,**=)\nlogical(and or not )\nmembership(in not in)\nidentity(is isnot)\nbit(& | ^ ~ << >>)\n'
a=5
b=6
a+b
11
a-b
-1
a*b
30
a/b
0.8333333333333334
a//b
0
a%b
5
a**b
15625
a,b
(5, 6)
a<b
True
a>b
False
a<=b
True
a>=b
False
a==b
False
a!=b
True
a=b
a+=b
a-=b
a*=b
a/=b
a%=b
a**=b
a and b
0.0
a or b
6
a not b
SyntaxError: invalid syntax
a not b
SyntaxError: invalid syntax
True and False
False
True and true
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    True and true
NameError: name 'true' is not defined. Did you mean: 'True'?
True and True
True
a=True
b=False
a and b
False
a or b
True
a%==b
SyntaxError: invalid syntax
a%==b
SyntaxError: invalid syntax
a%10==10
False
a%10==0
False
a=`python programming`
SyntaxError: invalid syntax
a'python programming'
SyntaxError: invalid syntax
a'python programming'
SyntaxError: invalid syntax
a='python programming'
a
'python programming'
'y'in a
True
'g'in a
True
'z' not in a
True
'r' not in a
False
L=['java','python','mysql','keyword']
L
['java', 'python', 'mysql', 'keyword']
'mysql' in L
True
"k" in L
False
d={'egg':8,'oil':120,'sugar':40,'salt':30}
'oil' in d
True
120 in d
False
'sugar' in d
True
'chill' in d
False
l=[1,2,3,4,5]
m=[1,2,3,4,5]
l==m
True
n=m
n
[1, 2, 3, 4, 5]
n==m
True
l is m
False
n is m
True
l is not m
True
n is not l
True
8& 14
8
8&7
0
>>> 8\7
SyntaxError: unexpected character after line continuation character
>>> 10^11
1
>>> 8|7
15
>>> ~12
-13
>>> 8>>3
1
>>> 15..1
SyntaxError: invalid syntax
>>> 15>>1
7
>>> 15>>3
1
>>> 15..216<<1
SyntaxError: invalid syntax
>>> 4<<2
16
>>> 16<<1
32
>>> 15>>3
1
>>> 4<<2
16
>>> #output formating
>>> print("a=",a,'b=',b,'c=',sep='',='@@@@')
SyntaxError: invalid syntax
>>> print("a=",a,'b=',b,'c=',sep='',end='@@@@')
a=python programmingb=Falsec=@@@@
>>> print(f'a={a} b={b} c= {c}')
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    print(f'a={a} b={b} c= {c}')
NameError: name 'c' is not defined
>>> a=1
>>> b,c=5,6
>>> print(f'a={a} b={b} c= {c}')
a=1 b=5 c= 6
>>> print('a=%d b%.2f c=%s'%(a,b,c))
a=1 b5.00 c=6
>>> print('a={} b={} c={}'.format(a,b,c))
a=1 b=5 c=6
>>> print('a={2} b={0} c={1}'.format(a,b,c))
a=6 b=1 c=5
