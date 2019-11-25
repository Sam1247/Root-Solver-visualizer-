from sympy import *
from math import *
from sympy.abc import x, y, z, a, b 
from sympy.parsing.sympy_parser import (parse_expr, eval_expr,  stringify_expr,  _token_splittable,standard_transformations,
                                       implicit_multiplication_application,split_symbols_custom, implicit_application,
                                      function_exponentiation, convert_xor, factorial_notation) # to reformulate equation. ex: 2x -> 2*x
from matplotlib import pyplot as plt
import numpy as np
import time
from BracketMethods import BracketMethods
import math

class FalsePosition(BracketMethods):
    
    def __init__(self, function, x_lower, x_upper, epsilon = 0.00001, i_max = 50):
        super(FalsePosition, self).__init__()
        self.function = self.parseFuncion(function)
        try:
            self.sub(x_upper)
        except:
            raise RuntimeError("More than one variable")
        self.solution['iteration'] = []
        self.solution['x_lower'] = []
        self.solution['x_upper'] = []
        self.solution['root'] = []
        self.solution['ea'] = []
        
     #   self.solution = dict(iteration = [], x_lower = [], x_upper = [], root = [], ea = [])
        self.epsilon = epsilon
        self.i_max = i_max
        self.x_lower = x_lower
        self.x_upper = x_upper

    def runMethod(self):
        x_lower = self.x_lower
        x_upper = self.x_upper
        root = 0
        prev_root = root
        ea = None
        start = time.time()
        if self.sub(x_lower) * self.sub(x_upper) >= 0: 
            raise RuntimeError("False Position: Guesses do not bracket")
        root = x_lower
        for i in range(self.i_max):
            itr = i + 1
            
            prev_root = root
            root = (x_lower * self.sub(x_upper) - x_upper * self.sub(x_lower)) / (self.sub(x_upper) - self.sub(x_lower))
            
            if (i != 0):
                ea = abs(root - prev_root)

            if (ea != None) and (ea < self.epsilon):
                end = time.time()
                self.executionTime = end - start
                self.root = root
                self.itr_num = itr
                self.precision = self.getPrecision()
                self.solution['iteration'].append(itr)
                self.solution['x_lower'].append(x_lower)
                self.solution['x_upper'].append(x_upper)
                self.solution['root'].append(root)
                self.solution['ea'].append(ea)
                self.print_table(self.solution)
                print("Found Solution Before Reaching Max Iterations")
                return root
            
            f_xl = self.sub(x_lower)
            f_xr = self.sub(root)
            test = f_xl * f_xr
            if test < 0:
                self.solution['iteration'].append(itr)
                self.solution['x_lower'].append(x_lower)
                self.solution['x_upper'].append(x_upper)
                self.solution['root'].append(root)
                self.solution['ea'].append(ea)
                x_upper = root 
            elif test > 0:
                self.solution['iteration'].append(itr)
                self.solution['x_lower'].append(x_lower)
                self.solution['x_upper'].append(x_upper)
                self.solution['root'].append(root)
                self.solution['ea'].append(ea)
                x_lower = root
            else:
                end = time.time()
                self.executionTime = end - start
                ea = 0
                self.solution['iteration'].append(itr)
                self.solution['x_lower'].append(x_lower)
                self.solution['x_upper'].append(x_upper)
                self.solution['root'].append(root)
                self.solution['ea'].append(ea)
                self.root = root
                self.itr_num = itr
                if i == 0:
                    self.precision = len(str(self.root))
                else:
                    self.precision = self.getPrecision()
                self.print_table(self.solution)
                print("Found Exact Solution")
                return root
        
        end = time.time()
        self.executionTime = end - start
        self.root = root
        self.itr_num = itr
        self.precision = self.getPrecision()
        self.print_table(self.solution)
        print("Reached Max Iterations")        
        return root

    def graph(self, counter):
        if counter > len(self.solution['root']):
            counter = len(self.solution['root'])
        left = self.x_lower
        right = self.x_upper

        # range of f(x)
        xx = np.arange(left -1, right + 1, 0.01)
        f = []
        for x in xx:
            f.append(self.sub(x))
        # plotting f(x)
        plt.plot(xx, f, 'b')
        for i in range(counter):
            xu = self.solution['x_upper'][i]
            xl = self.solution['x_lower'][i]
            xr = self.solution['root'][i]
            # drawing a line from xu to xl cutting the x axis in the new xr
            plt.plot([xu, xl], [self.sub(xu), self.sub(xl)],'ro-')
            # a vertical line showing the new root
            plt.vlines(xr, ymin = self.sub(xr),ymax=0, color='g')
        plt.axhline(0, color='grey')
        plt.grid()
        plt.show()

'''   
function = "x^3 - 4"
x_lower = -4
x_upper = 4    
false = FalsePosition(function, x_lower, x_upper)
false.runMethod()
print(false.solution)
'''