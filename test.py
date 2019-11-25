# -*- coding: utf-8 -*-
"""
Created on Sun May 12 05:16:06 2019

@author: esabn
"""
import math
import PyQt5
from PyQt5 import QtWidgets
from BisectionClass import Bisection
from FalsePosition import FalsePosition
from fixedPointIteration import FixedPointIterationMethod
from birgeVieta import birgeVietaMethod
from Muller import MullerMethod
function = "x^2 - 2 * x - 1"

x_lower = 4
x_upper = 4

b = birgeVietaMethod()
b.setFuncionAndIntialpoint(function, x_lower)

b.runMethod()

print (b.solution)
