Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> type(c)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    type(c)
NameError: name 'c' is not defined
>>> a=10
>>> a
10
>>> b=10
>>> type(b)
<class 'int'>
>>> t=999.9
>>> type(c)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    type(c)
NameError: name 'c' is not defined
>>> type(t)
<class 'float'>
>>> c=12+8j
>>> type(c)
<class 'complex'>
>>> s='PYTHON'
>>> type(s)
<class 'str'>
>>> s=''dfghhhjkl''
SyntaxError: invalid syntax. Is this intended to be part of the string?
>>> s="' dfghjkl"
>>> type(s)
<class 'str'>
>>> 
==================================================================================== RESTART: Shell ====================================================================================
