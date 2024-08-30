Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> X_train = np.array([
...     [0, 0, 0],
...     [0, 0, 1],
...     [0, 1, 0],
...     [0, 1, 1],
...     [1, 0, 0],
...     [1, 0, 1],
...     [1, 1, 0],
...     [1, 1, 1]
... ])
>>> y_train = np.array([-1, 1, -1, 1, -1, -1, 1, 1])
>>> for i, (x, y) in enumerate(zip(X_train, y_train), start=1):
...     print(f'x{i}={x}, y{i}={y}')
... 
...     
x1=[0 0 0], y1=-1
x2=[0 0 1], y2=1
x3=[0 1 0], y3=-1
x4=[0 1 1], y4=1
x5=[1 0 0], y5=-1
x6=[1 0 1], y6=-1
x7=[1 1 0], y7=1
x8=[1 1 1], y8=1
