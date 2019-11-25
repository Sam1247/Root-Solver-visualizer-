from Checker import ParserAndChecker as p


class gaussJordanClass:
    
    def __init__(self, parser): 
        self.parser = parser
        self.solution = []


    def solve(self):
        return self.gauss_jordann(self.parser.augmentedMatrix)
    
    def gauss_jordann(self, m):
        if not self.parser.checkSolvability():
            raise RuntimeError("GaussJordan: Not Solvable")
        (h, w) = (len(m), len(m[0]))
        for y in range(0,h):
            maxrow = y
            for y2 in range(y+1, h):
                if abs(m[y2][y]) > abs(m[maxrow][y]):
                    maxrow = y2
            (m[y], m[maxrow]) = (m[maxrow], m[y])
            for y2 in range(y+1, h):       
                c = m[y2][y] / m[y][y]
                for x in range(y, w):
                    m[y2][x] -= m[y][x] * c
        for y in range(h-1, 0-1, -1): 
            c = m[y][y]
            for y2 in range(0,y):
                for x in range(w-1, y-1, -1):
                    m[y2][x] -= m[y][x] * m[y2][y] / c
            m[y][y] /= c
            for x in range(h, w):             
                m[y][x] /= c
        sol = []
        for i in range(0, h):
            sol.append(m[i][w-1])
        self.solution = sol
        
        
        
#functions = ["r+y+z", "r-y-z-3", "r-2*y+3*z+5.1"]
#ob = p(functions) 
#print(ob.variables)
#obj = gaussJordanClass(ob)
#obj.solve()
#print(obj.solution)
