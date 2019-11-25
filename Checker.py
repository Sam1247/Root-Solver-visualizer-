from sympy import *
import sympy.abc 
from sympy.parsing.sympy_parser import (parse_expr, eval_expr,  stringify_expr,  _token_splittable,standard_transformations,
                                       implicit_multiplication_application,split_symbols_custom, implicit_application,
                                      function_exponentiation, convert_xor, factorial_notation)
import numpy
import re

class ParserAndChecker:
    coefficients = []
    numOfVariables = 0
    transformations = (standard_transformations + (implicit_multiplication_application, convert_xor, factorial_notation, function_exponentiation))
    solvable = True
    variables = []
    B = []
    augmentedMatrix = []

    def __init__(self, functions):
        self.coefficients = list()
        self.B = list()
        self.augmentedMatrix = list()
        self.parseFunction(functions)
        self.checkSolvability()
        self.numOfVariables = len(self.coefficients)
        
    def parseFunction(self,functions) :
        pattern = "([+-]?\s?[0-9]*[\.]?[0-9]*)?[*]?([a-zA-Z])"  # "(([-+]\s*\d*)?[*]?[x])"     "(([-+]\s*\d*)?[*]?[x]$)"
        var_pattern = "[a-zA-Z]"
        b_pattern = "([-+]?[0-9]*\.?[0-9]*)?$"
        

        # parsing equations to find variables & costants
        for i in range(len(functions)):
            functions[i] = str( parse_expr(functions[i] , transformations = self.transformations))
            functions[i] = functions[i].replace(" ", "")
            result = re.findall(var_pattern, functions[i] )
            result2 = re.findall(b_pattern, functions[i])
            self.B.append(result2[0])
            if self.B[i] == "":
                self.B[i] = "0"
            elif self.B[i][0] == "+":
                self.B[i] = self.B[i].replace("+","-")
            elif self.B[i][0] == "-":
                self.B[i] = self.B[i].replace("-","+")

            for i in range(len(result)):
                self.variables.append(result[i])

        self.variables = list(dict.fromkeys(self.variables))
                
        #check if number of equations equals number of variables
        if len(self.variables) != len(functions):
            self.solvable = False
            return

        #construct coefficients matrix
        for function in functions :
            if not self.solvable:
                return
            result = re.findall(pattern, function) 
            
            row = [0 for i in range(len(self.variables))]
            

            for i in range(len(result)):
               temp = result[i][0]
               if temp == "" or temp == "+":
                   temp = "+1"
               elif temp == "-":
                    temp = "-1"
               try:
                    row[self.variables.index(result[i][1])] = float(temp) 
               except:
                   self.solvable = False
                   raise SyntaxError
                   return

            
            self.coefficients.append(row)


        for i in range(len(self.B)):
            try:
                self.B[i] = float(self.B[i])
            except:
                raise SyntaxError
        return self.coefficients


    def checkSolvability(self):

        if(not self.solvable):

            return False
        self.augmentedMatrix = []
        for i in range (len(self.coefficients)) :
            self.augmentedMatrix.append(self.coefficients[i].copy()) #There was a bug here
            self.augmentedMatrix[i].append(float(self.B[i]))
        A = numpy.matrix(self.coefficients)
        B = numpy.matrix(self.augmentedMatrix)
        rankA = numpy.linalg.matrix_rank(A)
        rankB = numpy.linalg.matrix_rank(B)
        if(rankA == rankB and rankA == len(self.variables)):
            return True
        else:
            return False

    def getCoefficintsMatrix(self):
        return self.coefficients
    def getConstantsMatrix(self):
        return self.B
    def getAugmentedMatrix(self):
        return self.augmentedMatrix


#functions = ["x+y+z", "x-y-z-3", "x-2*y+3*z+5.1"]
#obj = ParserAndChecker(functions)           

#print(obj.checkSolvability())

        
       



        
        
       

           
           
               
        
        
   




