import parent
from matplotlib import pyplot as plt
import numpy as np
from sympy import *
import time
class NewtonRaphasonMethod(parent.parent):
    slopes = []

    def __init__(self):
        super(NewtonRaphasonMethod, self).__init__()
        return

    def runMethod(self):

        xi = self.initialPoint
        self.appRoots.append(float(xi))
        self.list.append(0)
        self.errors.append(None)
        error = 100
        start = time.time()
        while self.iteration < self.maxIteration and error >= self.epsilon:
            
            print(self.derivative)

            self.iteration = self.iteration + 1
            deriv = self.derivfx(self.derivative, xi)
            print(deriv)
            if (abs(deriv)<= 10 ** -10):
                print("yes")
                deriv = 0
            self.slopes.append(float(deriv))
            try:  # in order to avoid division by zero when f'(x) = 0
                # print(self.fx(self.function, xi), "------", deriv)
               
                xii = xi - (self.fx(self.function, xi) / deriv)
            except ZeroDivisionError:
                self.appRoots.append(None)
                self.errors.append(None)
                raise RuntimeError("Newton Raphson: Zero Division in Iteration {}".format(self.iteration))

            error = abs(xii - xi)

                 
            self.appRoots.append(float(xii))
            self.errors.append(float(error))
            xi = xii
        end = time.time()
        self.executionTime = end - start
        self.generateDic()
        self.precision = self.getPrecision()
        self.print_table(self.solution)
        return self.appRoots[len(self.appRoots) - 1]


    def graph(self, counter):
        if counter >= len(self.appRoots):
            counter = len(self.appRoots)-1
        # left = min(self.appRoots) - 1
        # right = max(self.appRoots) + 1
        left = max(self.appRoots, key=abs)
        right = 0
        if left == abs(left):
            right = left
            left = - right
        right = - left
        xx = np.arange(left-1, right+1, 0.01)
        x_range = []
        for x in xx:
            x_range.append(x)
        f = []
        # now we have a list of x range that we can delete from it avoiding complex numbers
        i = 0
        while i < len(x_range):
            sol = self.fx(self.function, x_range[i])
            if not isinstance(sol, Mul):
                f.append(sol)
            else:
                del x_range[i]
                i -= 1
            i += 1
        # plotting f(x)
        plt.plot(x_range, f, 'b')
        f = []
        for x in self.appRoots:
            f.append(self.fx(self.function, x))
        # plotting tangents
        # plot lines
        for i in range(counter):
            plt.plot([self.appRoots[i], self.appRoots[i+1]], [f[i], 0],'ro-')
            # a vertical line showing the new root
            plt.vlines(self.appRoots[i+1], ymin=0, ymax=f[i+1], color='g')

        # plotting x-axis
        plt.axhline(0, color='grey')
        plt.grid()
        plt.show()