import re


class Parser:
    """description of class"""
    coefficients = []
    variables = []
    B = []
    def parseFunction(self, functions):
        x = 1
        # "x+y+z+1", "1+x-y-z", "x-2*y+3*z+5.1"
        pattern = "([+-]?\s?[0-9]*[\.]?[0-9]*)?[*]?([a-zA-Z])"  # "(([-+]\s*\d*)?[*]?[x])"     "(([-+]\s*\d*)?[*]?[x]$)"
        var_pattern = "[a-zA-Z]"
        b_pattern = "([-+]?[0-9]*\.?[0-9]*)?$"
        # finding variables
        for function in functions:
            function = function.replace(" ", "")
            result = re.findall(var_pattern, function)
            # print(result)
            for i in range(len(result)):
                self.variables.append(result[i])
        self.variables = list(dict.fromkeys(self.variables))
 #       print(self.variables)

        # finding results
        for function in functions:
            function = function.replace(" ", "")
            result = re.findall(b_pattern, function)
            # print(result)
            self.B.append(result[0])
        for i in range(len(self.B)):
            if self.B[i] == "":
                self.B[i] = "0"
            elif self.B[i][0] == "+":
                self.B[i] = self.B[i].replace("+","-")
            elif self.B[i][0] == "-":
                self.B[i] = self.B[i].replace("-","+")
#        print(self.B)

        # finding coefficients
        for function in functions:
            function = function.replace(" ", "")
            result = re.findall(pattern, function)
            #print(result)
            row = []
            for i in range(len(result)):
                temp = result[i][0]
                if temp == "" or temp == "+":
                    temp = "+1"
                elif temp == "-":
                    temp = "-1"
                row.append(temp)
                self.variables.append(result[i][1])
            # print(row)
            self.coefficients.append(row)
        # print(self.variables)
        # self.variables = list(set(self.variables))
        # print(self.variables)
        return self.coefficients


