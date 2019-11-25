import parent
import sympy
import time
class birgeVietaMethod(parent.parent):
    
    def __init__(self):
       super(birgeVietaMethod, self).__init__()
       self.aCoefficinets = []
       self.bCoefficinets = []
       self.cCoefficinets = []
 
       return
    def findCoeff(self):
        x = sympy.symbols('x')
        self.aCoefficinets = (sympy.poly(self.function, x)).all_coeffs()
    
        for i in range (0, len(self.aCoefficinets) - 1):
            self.aCoefficinets[i] = float(self.aCoefficinets[i])
       
        return


    def getB1(self, xi):      
        self.bCoefficinets.clear()
        if len(self.aCoefficinets) == 0:
            return None
        self.bCoefficinets.append(float(self.aCoefficinets[0]))
        for i in range(1,len(self.aCoefficinets) ):
            self.bCoefficinets.append(float(self.bCoefficinets[i -1] * xi + self.aCoefficinets[i] ))
        return self.bCoefficinets[len(self.bCoefficinets) - 1]

    def getC1(self, xi):
        self.cCoefficinets.clear()
        if len(self.bCoefficinets) == 0:
            return # need to raise an error
        self.cCoefficinets.append(float(self.bCoefficinets[0]))
        for i in range(1,len(self.bCoefficinets) - 1):
            self.cCoefficinets.append(float(self.cCoefficinets[i - 1] * xi + self.bCoefficinets[i] ))
        return self.cCoefficinets[len(self.cCoefficinets) - 1]


    def runMethod(self):
        self.findCoeff()
        
        xi = self.initialPoint
        self.appRoots.append(float(xi))
        self.list.append(0)
        self.errors.append(None)
        error = 100
        start = time.time()
        while self.iteration < self.maxIteration and error >= self.epsilon :
           
            self.iteration = self.iteration + 1
            try:
               xii = xi - (self.getB1(xi) / self.getC1(xi))
            except ZeroDivisionError:
                raise RuntimeError("Bierge-Vieta: Zero Division in Iteration {}".format(self.iteration))
            self.appRoots.append(float(xii))
            
            error = abs(xii - xi)
            # print("error = ", error)
            
            self.errors.append(float(error))
            xi = xii
        end = time.time()
        self.executionTime = end - start
        self.precision = self.getPrecision()
        self.generateDic()
        self.print_table(self.solution)
        return self.appRoots[len(self.appRoots) - 1]
