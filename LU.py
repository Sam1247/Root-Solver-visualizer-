# -*- coding: utf-8 -*-
"""
Created on Tue May 14 07:02:38 2019

@author: esabn
"""
from Checker import ParserAndChecker as p

import numpy as np

class LUClass:

    def __init__(self, parser): 
        self.parser = parser
        self.solution = []

    def solve(self):
        return self.LU(self.parser.augmentedMatrix)
    
    def LU(self, A):
        if not self.parser.checkSolvability():
            raise RuntimeError("LU: Not Solvable")
        n = len(A)
        # (1) Extract the b vector
        b = [0 for i in range(n)]
        for i in range(0,n):
            b[i]=A[i][n]
    
        L = [[0 for i in range(n)] for i in range(n)]
        for i in range(0,n):
            L[i][i] = 1
    
        U = [[0 for i in range(0,n)] for i in range(n)]
        for i in range(0,n):
            for j in range(0,n):
                U[i][j] = A[i][j]
    
        for i in range(0,n): # for i in [0,1,2,..,n]
            maxEl = abs(A[i][i])
            maxRow = i
            for k in range(i+1, n):
                if abs(A[k][i]) > maxEl:
                    maxEl = abs(A[k][i])
                    maxRow = k
            for k in range(i, n+1):
                tmp = A[maxRow][k]
                A[maxRow][k] = A[i][k]
                A[i][k] = tmp
    
    		# (4.3) Subtract lines
            for k in range(i+1,n):
                c = -U[k][i]/float(U[i][i])
                L[k][i] = -c # (4.4) Store the multiplier
                for j in range(i, n):
                    U[k][j] += c*U[i][j] # Multiply with the pivot line and subtract
    
    		# (4.5) Make the rows bellow this one zero in the current column
            for k in range(i+1, n):
                U[k][i]=0
    
        y = [0 for i in range(n)]
        for i in range(0,n,1):
            y[i] = b[i]/float(L[i][i])
            for k in range(i+1,n,1):
                b[k] -= b[i]*L[k][i]
    
        n = len(U)
    
    	# (6) Perform substitution Ux=y
        x = [0 for i in range(n)]
        for i in range(n-1,-1,-1):
            x[i] = y[i]/float(U[i][i])
            for k in range (i-1,-1,-1):
                y[k] -= x[i]*U[k][i]
        self.solution = x
        return x
'''
functions = ["2*a + 3*b - 5", "2*a - 3*b + 1"]
ob = p(functions) 
print(ob.variables)
obj = LUClass(ob)
obj.solve()
print(obj.solution)
'''