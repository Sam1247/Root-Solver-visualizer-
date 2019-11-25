import newtonRaphason
import secent
import BisectionClass
import FalsePosition
import birgeVieta
import fixedPointIteration
import allMethods
import sympy
from sympy.abc import x
from sympy import *
import matplotlib.pyplot as plt
import numpy as np
import sympy as sym
from sympy import symbols
from sympy.plotting import plot

secantObj = secent.secantMethod()
secantObj.setFuncionAndIntialpoint("a*x + b", 1.5, 1)
secantObj.runMethod()
print(secantObj.getAppRoots())
print(secantObj.getErrors())
print(secantObj.saveDate())
# secantObj.graph(101)


# print()
# print()
# print()

# BiObj = BisectionClass.Bisection("x^2 - 2 * x - 1", 2, 4)
# BiObj.runMethod()
# # BiObj.graph(190)
#
#
# falseObj = FalsePosition.FalsePosition("x^2 - 2 * x - 1", 1, 4)
# falseObj.runMethod()
# # # falseObj.graph(200)
#
#
#
#
# newtonObj = newtonRaphason.NewtonRaphasonMethod()
# newtonObj.setFuncionAndIntialpoint("x^2 + 2 * x - 1", 4)
# newtonObj.runMethod()
# newtonObj.saveDate()
# # newtonObj.graph(200)


# fixedObj = fixedPointIteration.FixedPointIterationMethod()
# fixedObj.setFuncionAndIntialpoint("x^2 + 2* x - 1", 0.4)                                      #"cos x - 2x**2 + 7 x + e^x"
# fixedObj.runMethod()
# #print(obj4.getAppRoots())
# #print(obj4.getErrors())
# fixedObj.saveDate()                             #"7 x + sin 2*x**x + cos 2**x - x**2 + e^x + 2^x + x + 2**x + x**x + 2**(2*x) + log 2*x "

# fixedObj.graph(200)


# exp = sym.sympify(obj4.function)
# exp2 = sym.sympify("2**x")
# p = plot(exp)
# #p1 = plot(obj4.appRoots)
# p2 = plot(exp2) # keda kol wa7da lwa7daha
# p.extend(p2)
# p.show()

# obj3 = birgeVieta.birgeVietaMethod()
# obj3.setFuncionAndIntialpoint("x^2 + x - 1", 4)
# obj3.runMethod()
# print(obj3.list)
# obj3.saveDate()
#
# all = allMethods.allMethods(BiObj,falseObj,fixedObj,newtonObj,secantObj,obj3)
# print(all.graph_roots())
# all.graph_errors()
