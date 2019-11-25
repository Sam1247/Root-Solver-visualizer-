import parent
from sympy.parsing.sympy_parser import (parse_expr, eval_expr, stringify_expr, _token_splittable,
                                        standard_transformations,
                                        implicit_multiplication_application, split_symbols_custom, implicit_application,
                                        function_exponentiation, convert_xor, factorial_notation)
from sympy import *
import re
import time
from matplotlib import pyplot as plt
import numpy as np

class FixedPointIterationMethod(parent.parent):  
    def __init__(self):
       super(FixedPointIterationMethod, self).__init__()
       self.g_equation = None      
       return
   
    def setFuncionAndIntialpoint(self, function, xi ):
       super(FixedPointIterationMethod, self).setFuncionAndIntialpoint(function,xi)
       self.g_equation = self.get_g_equation()
       return

    def get_g_equation(self):
        g_equation = self.parseFuncion(self.function)

        # print(g_equation, " before start")
        g_equation = " " + g_equation + " "
        pattern = "(([-+])?\s*(\d*\.*\d*)?\*?[x])[\s][+-]?"             # "(([-+]\s*\d*)?[*]?[x])"     "(([-+]\s*\d*)?[*]?[x]$)"
        result = re.findall(pattern, g_equation)
        i = 0
        # print(result)
        while i < len(result) and len(result) > 1:
            if result[i][2] == "" and result[i][1] == "":
                # print(result[i])
                del result[i]
                i -= 1
            i+=1
        # print(result)                                                       #"(([-+])*\s*(\d*\.*\d*)?[*]?[x])[\s][+-]"
        try:
            sign = result[0][1]
            if sign == "":
                sign = '+'
            if result[0][2] == "":
                denomerator = "1"
            else:
                denomerator = result[0][2]
            if sign == "+":
                # print(g_equation , "before any edit")
                g_equation = g_equation + "-" + result[0][0]
                g_equation = self.parseFuncion(g_equation)
                # print(g_equation, "after editing")
                g_equation = "(" + g_equation + ")/-" + denomerator
                # print(g_equation, "after factoring")
            else:
                # print(g_equation, "before any edit")
                g_equation = g_equation + sign + result[0][0]
                g_equation = self.parseFuncion(g_equation)
                # print(g_equation, "after editing")
                g_equation = "(" + g_equation + ")/" + denomerator
                # print(g_equation, "after factoring")

            # print(denomerator, " denomerator")
        except:
            raise RuntimeError("Fixed Point: No First Degree")

        return g_equation

    def check_convergence(self):
        g_dash = self.get_g_dash()
        try:
            return (0 <= abs(g_dash) < 1)
        except:
            return False

    def get_g_dash(self):   
        x = float(self.initialPoint)
        return eval(str(diff(self.g_equation)))

    def runMethod(self):
        error = 100
        x_prev = self.initialPoint
        start = time.time()
        self.appRoots.append(float(x_prev))
        self.list.append(0)
        self.errors.append(None)
        # if not self.check_convergence():
        #     print("Diverge !")
        #     self.maxIteration = 6
        converge = self.check_convergence()
        if not converge:
            raise RuntimeError("Fixed Point: Diverge")

        while converge and self.iteration < self.maxIteration and self.epsilon <= error:
            self.iteration = self.iteration + 1
            x_next = self.fx(self.g_equation, x_prev)
            self.appRoots.append(float(x_next))

            error = abs(x_next - x_prev)
            self.errors.append(float(error))

            if (self.fx(self.function, x_next) == 0):
                break
               
            x_prev = x_next
        end = time.time()
        self.generateDic()
        self.executionTime = end - start
        
#       precision remains 3ashan mesh 3aref heya anho wa7da

    def graph(self, counter):
        if counter > len(self.appRoots):
            counter = len(self.appRoots)
        left = max(self.appRoots, key=abs)
        right = 0
        if left == abs(left):
            right = left
            left = - right
        right = - left
        # range of el xat for the equation
        xx = np.arange(left-1, right+1, 0.01)
        x_range = []
        f = []
        for x in xx:
            x_range.append(x)
        # now we have a list of x range that we can delete from it avoiding complex numbers
        i = 0
        while i < len(x_range):
            sol = self.fx(self.g_equation, x_range[i])
            if not isinstance(sol, Mul):
                f.append(sol)
            else:
                del x_range[i]
                i -= 1
            i+=1
        g_of_x = []
        for x in self.appRoots:
            g_of_x.append(self.fx(self.g_equation,x))

        # plot function and g function
        plt.plot(x_range, f, 'b')
        plt.plot(x_range, x_range, 'r')
        merged_list = []
        if not len(self.appRoots) == 1:
            merged_list = [(self.appRoots[i], g_of_x[i]) for i in range(0, counter)]
        # plot lines
        for x, y in merged_list:
            plt.plot([x, x], [x, y], 'g')
            plt.plot([x, y], [y, y], 'g')
        # plt.ion()
        plt.axhline(0, color='grey')
        plt.grid()
        # plt.savefig('foo')
        plt.show()
