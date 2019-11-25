import parent
from matplotlib import pyplot as plt
import numpy as np
from sympy import *
import time

class secantMethod(parent.parent):
    secondInitial = 0

    def __init__(self):
        super(secantMethod, self).__init__()
        return

   

    def runMethod(self):
        self.list.append(0)
        self.errors.append(None)
        xi = self.initialPoint
        xii = self.secondInitial
        self.appRoots.append([float(xi), float(xii)])
        error = 100
        start = time.time()
        while self.iteration < self.maxIteration and error >= self.epsilon:
            try:
                xiii = xii - (self.fx(self.function, xii) * (xi - xii)) / (
                            self.fx(self.function, xi) - self.fx(self.function, xii))
            except ZeroDivisionError:
                raise RuntimeError("Secent: Zero Division in Iteration {}".format(self.iteration)) 

            self.appRoots.append(float(xiii))

            error = abs(xiii - xii) 
            self.errors.append(float(error))
            xi = xii
            xii = xiii
            self.iteration = self.iteration + 1
        end = time.time()
        self.executionTime = end - start
        self.generateDic()
        self.print_table(self.solution)
        return self.appRoots[len(self.appRoots) - 1]



    def graph(self, counter):
        if counter > len(self.appRoots)-2:
            counter = len(self.appRoots)-1

        f = []
        f.append(self.appRoots[0][0])
        f.append(self.appRoots[0][1])
        for i in range(len(self.appRoots)):
            f.append(self.appRoots[i])
        del f[2]
        # now f contains the appRoots with the two initial points
        left = max(f, key=abs)
        right = 0
        if left == abs(left):
            right = left
            left = - right
        right = - left
        # range of f(x)
        xx = np.arange(left - 1, right + 1, 0.01)
        x_range = []
        for x in xx:
            x_range.append(x)
        g = []
        # now we have a list of x range that we can delete from it avoiding complex numbers
        i = 0
        while i < len(x_range):
            sol = self.fx(self.function, x_range[i])
            if not isinstance(sol, Mul):
                g.append(sol)
            else:
                del x_range[i]
                i -= 1
            i += 1
        # plotting f(x)
        plt.plot(x_range, g, 'b')
        # f2 is the value of f(x) for all roots in f
        f2 = []
        for x in f:
            f2.append(self.fx(self.function, x))
        # matching the 2 intial points and indicate the new point
        for i in range(counter):
            plt.plot([f[i], f[i+1]], [f2[i], f2[i+1]], 'ro-')
            plt.plot([f[i+1], f[i+2]], [f2[i+1], 0], 'ro-')
            # a vertical line showing the new root
            plt.vlines(f[i+2], ymin=self.fx(self.function,f[i+2]), ymax=0, color='g')

        plt.axhline(0, color='grey')
        plt.grid()
        plt.show()