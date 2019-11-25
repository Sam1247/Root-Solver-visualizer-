class RootFinderReader:
    lines = []
    absPath = ""
    function = ""
    method = ""
    parameters = []
    max_itr = None
    epsilon = None
    def __init__(self, absPath):
        self.absPath = absPath
        self.lines = []
        self.method = ""
        self.parameters = []
        self.read()
        try:
            print(self.lines)
            self.function = self.lines[0]
            print(self.lines[1])
            self.method = self.lines[1]
            self.parameters = self.lines[2].split()
            if len(self.lines) == 4:
                temp = self.lines[3]
                try:
                    self.max_itr = int(temp)
                except:
                    try:
                        self.epsilon = float(temp)
                    except:
                        self.max_itr = None
                        self.epsilon = None
        except Exception as e:
            raise e
            raise RuntimeError("Couldn't Read From File")
    def read(self):
        self.lines.clear()
        try:
            f = open(self.absPath, 'r')
        except Exception:
            raise FileNotFoundError("Couldn't Find The File")
        else:
            for line in f:
                line = line.replace("\n","")   # as without it , at the end on each line will be new line char  ex: '---\n' 
                self.lines.append(line)
            f.close()
            
            
class SystemSolverReader:
    lines = []
    absPath = ""
    equations = []
    method = ""
    n = 0
    parameters = []
    equation = []
    method = ""
    paramters = []
    
    def __init__(self, absPath):
        self.absPath = absPath
        self.lines = []
        self.equations =[]
        self.method = ""
        self.parameters = []
        self.read()
        try:
            self.n = int(self.lines[0])
            for i in range(self.n):
                self.equations.append(self.lines[1+i])
            self.method = self.lines[self.n+1]
            if len(self.lines) == self.n + 3:
                self.parameters = self.lines[self.n+2].split()
        except Exception as e:
            raise e
            #raise RuntimeError("Couldn't Read From File")
    def read(self):
        try:
            f = open(self.absPath, 'r')
        except Exception:
            raise FileNotFoundError("Couldn't Find The File")
        else:
            for line in f:
                line = line.replace("\n","")   # as without it , at the end on each line will be new line char  ex: '---\n' 
                self.lines.append(line)
            f.close()        