import parent
import time
import cmath
from matplotlib import pyplot as plt
import numpy as np
from sympy import *
from sympy.abc import x
from sympy import sympify
import sympy


class MullerMethod(parent.parent):
    def __init__(self):
        super(MullerMethod, self).__init__()
        self.secondInitial = 0
        self.thirdInitial = 0
        self.equS = []
        return

   
    def runMethod(self):
        self.list.append(0)
        self.errors.append(None)
        xi = self.initialPoint
        xii = self.secondInitial
        xiii = self.thirdInitial
        self.appRoots.append([float(xi), float(xii), float(xiii)])
        error = 100
        start = time.time()
        while self.iteration < self.maxIteration and error >= self.epsilon:
         
            Xs = [xi, xii, xiii]
            Ys = [self.fx(self.function,xi), self.fx(self.function,xii), self.fx(self.function,xiii)]        
            equ = self.lagrange (Xs, Ys)         
            equ = self.parseFuncion(equ, False)         
            pol = sympy.poly(sympify(equ) , x)
            coeff = pol.all_coeffs()       
            a, b, c = coeff[0], coeff[1], coeff[2]

            try:
                r = (-b + cmath.sqrt(b**2 - 4 *a  * c))/ (2 * a)
                s =   (-b - cmath.sqrt(b**2 - 4 *a  * c))/ (2 * a)
            except ZeroDivisionError:
                raise RuntimeError("Muller: Zero Division in Iteration {}".format(self.iteration))

               
            if isinstance(r,complex) :
                # print(r)
                if r.imag == 0j:#result is real number
                       r = r.real
                else:
                    raise RuntimeError("Muller: Zero Division in Iteration {}".format(self.iteration))
                
            if isinstance(s,complex) :
                # print(s)
                if s.imag == 0j:#result is real number
                       s = s.real
                else:
                    raise RuntimeError("Muller: Zero Division in Iteration {}".format(self.iteration))
            
            
           
            if(abs(self.fx(self.function,r)) < abs(self.fx(self.function,s))):
                    xplus = r
            else:
                    xplus = s

            if isinstance(xplus,complex) :
                if xplus.imag == 0j:#result is real number
                       xplus = xplus.real
                else:
                    raise RuntimeError("Muller: Zero Division in Iteration {}".format(self.iteration))

            xi = xii
            xii = xiii
            xiii = xplus
            
            error = abs(xiii - xii)

            self.appRoots.append(float(xplus))
            self.errors.append(float(error))
            self.equS.append(equ)
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
        f.append(self.appRoots[0][2])
        for i in range(len(self.appRoots)):
            f.append(self.appRoots[i])
        del f[3]
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
        # now we have a list of x range that we can delete from it avoiding complex numbers
        i = 0
        g = []      #to draw the whole curve
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
        # f is roots and f2 is the value y of the roots
        for i in range(counter):
            plt.plot(f[i],f2[i],'ro-')
            plt.plot(f[i+1], f2[i+1], 'ro-')
            plt.plot(f[i+2], f2[i+2], 'ro-')
            plt.plot(f[i+3], f2[i+3], 'ro-')
            self.draw_curve(self.equS[i],min(f) - 1,max(f)+1)
            plt.vlines(f[i + 3], ymin=self.fx(self.function, f[i + 3]), ymax=0, color='g')


        plt.axhline(0, color='grey')
        plt.grid()
        plt.show()


    def draw_curve(self,equation,left,right):
        xx = np.arange(left, right, 0.01)
        x_range = []
        for x in xx:
            x_range.append(x)
        g = []  # to draw the whole curve
        i = 0
        while i < len(x_range):
            sol = self.fx(equation, x_range[i])
            if not isinstance(sol, Mul):
                g.append(sol)
            else:
                del x_range[i]
                i -= 1
            i += 1
        plt.plot(x_range, g, 'y')


    def lagrange(self, Xs, Ys):
       equ = ""
       equ += self.bracket("x", str(Xs[1])) +  self.bracket("x", str(Xs[2]))
       equ += " * " + str(Ys[0])
       equ += " / (" + self.bracket(str(Xs[0]), str(Xs[1]))   + self.bracket(str(Xs[0]), str(Xs[2])) + " )"
       equ += " + "
       equ += self.bracket("x", str(Xs[0])) +  self.bracket("x", str(Xs[2]))
       equ += " * " + str(Ys[1])
       equ += " / (" + self.bracket(str(Xs[1]), str(Xs[0]))   + self.bracket(str(Xs[1]), str(Xs[2])) + " )"
       equ += " + "
       equ += self.bracket("x", str(Xs[0])) +  self.bracket("x", str(Xs[1]))
       equ += " * " + str(Ys[2])
       equ += " / (" + self.bracket(str(Xs[2]), str(Xs[0]))   + self.bracket(str(Xs[2]), str(Xs[1]))  + " )"

       return equ


    def bracket(self,x1,  x2):
        return "(" + str(x1) +" - " + str(x2) +")"




#print(len(obj.list))
#print(len(obj.equS))

#print(obj.list)
#print(obj.equS)


#obj.graph(100)




