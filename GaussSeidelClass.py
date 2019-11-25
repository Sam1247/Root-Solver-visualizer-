# -*- coding: utf-8 -*-
"""
Created on Thu May  2 12:20:27 2019

@author: esabn
"""

import pandas as pd
from Checker import ParserAndChecker as p
from matplotlib import pyplot as plt

class GaussSeidel:
    
    def __init__(self, parser, epsilon = 0.00001, i_max = 50, initial = [0]):
        self.parser = parser
        if (initial == [0]):
            self.inital = [0] * self.parser.numOfVariables
        else:
            self.inital = initial
        self.epsilon = epsilon
        self.i_max = i_max
        self.solution = [0] * self.parser.numOfVariables
        self.steps_dict = {}
        self.steps_dict["iteration"] = []
      #  l = ["x"+str(j+1) for j in range(self.parser.numOfVariables)]
      #  l2 = ["e" for j in range(self.parser.numOfVariables)]

        for j in self.parser.variables:
            self.steps_dict[j] = []
            self.steps_dict["e"+j] = []
      #  for j in l2:
       #     self.steps_dict[j] = []
    
    def solve(self):
        if not self.parser.checkSolvability():
            raise RuntimeError("GaussSeidel: Not Solvable")
        n = self.parser.numOfVariables
        A = self.parser.coefficients
        B = self.parser.B
        solutions = self.inital
        errors = [100] * n
        for itr in range(self.i_max):
            itr_num = itr + 1
            for k in range(n):
                solution_old = solutions[k]
                num =sum(-A[k][j] * solutions[j] for j in range(n) if k != j)
                solutions[k] = (B[k] + num) / A[k][k]
                errors[k] = abs(solutions[k] - solution_old)
                
            self.steps_dict["iteration"].append(itr_num)
            for j in range(n):
                var_name = self.parser.variables[j]
                var_value = solutions[j]
                err_name = "e"+self.parser.variables[j]
                err_value = errors[j]
                self.steps_dict[var_name].append(var_value)
                self.steps_dict[err_name].append(err_value)
            if (max(errors) < self.epsilon):
                self.solution = solutions
                return
        self.solution = solutions
        return
    
    def graph(self):
        n = self.parser.numOfVariables
        var_list = self.parser.variables
        for i in range(n):
            # setting the variable name
            var_name = var_list[i]
            # setting the number of iterations
            iterations = self.steps_dict["iteration"]
            # setting list of roots
            roots = self.steps_dict[var_name]
            # plotting each graph
            plt.plot(iterations, roots, "o-", label = var_name)
        plt.title("no. of iterations & roots")
        plt.xlabel("No. of iterations")
        plt.ylabel("Roots")
        plt.legend(loc='upper right')
        plt.grid()
        plt.show()
    def save(self, path):
         data_table = pd.DataFrame.from_dict(self.steps_dict)
         data_table.to_csv(path, index = False)

'''
functions = ["2*a + 3*b - 5", "2*a - 3*b + 1"]
ob = p(functions) 
print(ob.variables)
obj = GaussSeidel(ob)
obj.solve()
print(obj.solution)
print(obj.steps_dict)
'''