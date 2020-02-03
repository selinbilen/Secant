import math
from math import e

def f(x):
  return 2*math.cosh(x/4)-x

def secant(x1,x2):
  for i in range(10):
    xnew = x2-(f(x2)*(x2-x1)/f(x2)-f(x1))
    if(abs(xnew-x2)<10**-5):
      break
    else:
      x1=x2
      x2=xnew
    print(xnew)
secant(1,2)


import math
from math import e

def cosh(x):
  return (((e*x) + (e*(-x)))/2)

def sinh(x):
  return (((e*x) - (e*(-x)))/2)

def f(x):
  return (2*math.cosh(x/4))-x

def Df(x):
  return (0.5*math.sinh(x/4))-1

def Newton(x):
  for i in range(1,10):
    xn= x-(f(x)/Df(x))
    print(xn)
    x=xn
Newton(2)
