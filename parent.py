from sympy import *
import math
from sympy.abc import x
from sympy.parsing.sympy_parser import (parse_expr, eval_expr,  stringify_expr,  _token_splittable,standard_transformations,
                                       implicit_multiplication_application,split_symbols_custom, implicit_application,
                                      function_exponentiation, convert_xor, factorial_notation)
import pandas as pd
class parent:
    
   def __init__(self):      
       self.list = []
       self.function = None
       self.derivative = None
       self.maxIteration = 50
       self.iteration = 0
       self.executionTime = 0
       self.epsilon = 0.00001
       self.initialPoint = 0
       self.appRoots = []
       self.errors = []    
       self.executionTime = 0;
       self.solution = {}
       self.precision = 0
       self.secondInitial = 0
       self.thirdInitial  = 0
       self.solution = {}

       return

   def setFuncionAndIntialpoint(self, function, xi, xii = None, xiii = None):
       self.function = self.parseFuncion(function)
       self.initialPoint = xi
       self.secondInitial = xii
       self.thirdInitial = xiii
       try:
           self.fx(self.function,xi)
       except:
           raise RuntimeError("More than one variable")
       self.calculateDerivative()
       return
   
   def setMaxIteration(self, maxIteration):
       self.maxIteration= maxIteration
       return

   def setEpsilon(self, epsilon):
        self.epsilon = epsilon
        return

   def print_table(self, dict):
         data_table = pd.DataFrame.from_dict(dict)
         print(data_table)
         
   def parseFuncion(self, function, f = True):
       transformations = (standard_transformations + (implicit_multiplication_application, convert_xor, factorial_notation, function_exponentiation))
       function = str( parse_expr(function, transformations = transformations))
       if f:
            function = function.replace("e", "2.7182818284590452") # to be solved later
       # print("after parsing : " , function)
       return function

   def calculateDerivative(self):
       self.derivative = str(diff(self.function))
       # print("after derivative : " , self.derivative)
       return

   def fx(self,function, approx):
       x = float(approx)
       return eval(function)
       

   def derivfx(self, function, approx):
        x = float(approx)
        return eval(function)

   def getErrors(self):
       return self.errors

   def getAppRoots(self):
       return self.appRoots

   def getSlopes(self):
       return self.slopes
   def getNumOfIteration(self):
       return self.list[-1]

   def getRoot(self):
       return self.appRoots[-1]

   def generateDic(self):
       for i in range(self.iteration):
           self.list.append(i+1)
       self.solution = {}
       self.solution['iterations'] = self.list
       self.solution['appRoots'] = self.appRoots
       self.solution['errors'] = self.errors
       
   def saveDate(self):
       self.solution = {}
       self.solution['iterations'] = self.list
       self.solution['appRoots'] = self.appRoots
       self.solution['errors'] = self.errors
       # print(self.solution)
       self.save(self.solution, "save.csv")
       return self.solution
   def save(self, dict, filename):
        print(dict)
        data_table = pd.DataFrame.from_dict(dict)
        data_table.to_csv(filename, index = False)


   def getPrecision(self):
       relativeError = 0
       try:
             relativeError  =  self.errors[len(self.errors) - 1] * 100 / self.appRoots[len(self.appRoots) - 1]
             relativeError = abs(relativeError)
       except ZeroDivisionError:
           return "-"

       if relativeError == 0:
           n = len(str(abs(self.appRoots[len(self.appRoots) - 1])))

           if 'e' in str(self.appRoots[len(self.appRoots) - 1]):
               n = str(abs(self.appRoots[len(self.appRoots) - 1])).index('e')

           if str(abs(self.appRoots[len(self.appRoots) - 1]))[0] == '0':
               n -= 1

           if '.' in str(self.appRoots[len(self.appRoots) - 1]):
               n -= 1

           return n

       return math.floor( 1 + math.log10(5) - math.log10(relativeError)) # = |_ 1 + log5 - log(ea) _| in which ea is the last relative error saved

