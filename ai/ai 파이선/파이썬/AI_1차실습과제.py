Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> yut=['xxxx', 'xxxo', 'xxox', 'xxoo', 'xoxx', 'xoxo', 'xoox', 'xo', 'oxxx', 'oxxo', 'oxox', 'oxoo', 'ooxx', 'ooxo', 'ooox', 'oooo']
>>> throw=random.choice(yut)
>>> print(throw)
ooxx
>>> n=throw.count('o')
>>> if n==4: print("모")
... elif n==3: print("도")
... elif n==2: print("개")
... elif n==1: print("걸")
... elif n==0: print("윷")
... 
개
