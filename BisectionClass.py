from sympy import *
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import time
from BracketMethods import BracketMethods
import math
class Bisection(BracketMethods):
    

    def __init__(self, function, x_lower, x_upper, epsilon = 0.00001, i_max = 50):
        super(Bisection, self).__init__()
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
        root = 0
        x_lower = self.x_lower
        x_upper = self.x_upper
        ea = None
        start = time.time()
        f_xl = self.sub(x_lower)
        f_xu = self.sub(x_upper)
        test = f_xl * f_xu

        if test >= 0:
            raise RuntimeError("Bisection: Guesses do not bracket")
        
        for i in range(self.i_max):
            itr = i + 1
            prev_root = root
            root = (x_lower + x_upper) / 2
       #     if i == 0 and abs(self.sub(root)) < 0.0000001:
       #         self.solution['iteration'].append(itr)
       #         self.solution['x_lower'].append(x_lower)
       #         self.solution['x_upper'].append(x_upper)
       #         self.solution['root'].append(root)
       #         self.solution['ea'].append(0)
       #         self.save(self.solution, "bisecion.csv")
       #         return root
            if (i == 0):
                ea = None
            else:
                ea = abs(root - prev_root)
            
            #self.solution['iteration'].append(itr)
            #self.solution['x_lower'].append(x_lower)
            #self.solution['x_upper'].append(x_upper)
            #self.solution['root'].append(root)
            #self.solution['ea'].append(ea)
  
            if (ea != None) and (ea < self.epsilon):
                end = time.time()
                self.executionTime = end - start
                self.root = root
                self.itr_num = itr
                #self.precision = self.getPrecision()
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
                
                #self.root = root
                #self.itr_num = itr
                #self.precision = 0
                
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
        xx = np.arange(left -2, right + 2, 0.01)
        f = []
        for x in xx:
            f.append(self.sub(x))
        # plotting f(x)
        plt.plot(xx, f, 'b')
        for i in range(counter):
            # plot x lower
            plt.axvline(self.solution['x_lower'][i], color = 'g')
            # plot x upper
            plt.axvline(self.solution['x_upper'][i], color = 'y')
            # plot x r
            plt.axvline(self.solution['root'][i], color = 'r')
        plt.axhline(0, color='grey')
        plt.grid()
        plt.show()
    
    def getTheUpperBoundOfIterations(self):
        try:
            x = math.ceil(math.log(((self.x_upper - self.x_lower) / self.epsilon), 2))
        except Exception:
            x = None
        return x
'''        
function = "x^2 - 2 * x - 1"
x_lower = 0
x_upper = 4
bisection = Bisection(function, x_lower, x_upper)
bisection.runMethod()
print(bisection.solution['root'])
'''