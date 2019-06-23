Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> type(1)
<class 'int'>
>>> type('hello')
<class 'str'>
>>> type('hello'+1)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    type('hello'+1)
TypeError: must be str, not int
>>> type('hello'+' ' +'world')
<class 'str'>
>>> 'hello'+' ' +'world'
'hello world'
>>> hello world
SyntaxError: invalid syntax
>>> n = 'hello'
>>> print(n)
hello
>>> n == '1+1'
False
>>> n==1+1
False
>>> n = 1 + 3
>>> print(n)
4
>>> str()
''
>>> help(str)

>>> num = 1
>>> word = 'Useless_word'
>>> //comment = 228
SyntaxError: invalid syntax
>>> #comment = 228
>>> /comment = 228
SyntaxError: invalid syntax
>>> 
