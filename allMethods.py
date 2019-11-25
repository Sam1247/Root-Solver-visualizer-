import newtonRaphason
import secent
import BisectionClass
import FalsePosition
import birgeVieta
import fixedPointIteration
import Muller

from matplotlib import pyplot as plt
import numpy as np

class allMethods():
    def __init__(self, all_methods):
        self.bisection = all_methods[0]
        self.falsePosition = all_methods[1]
        self.fixedPoint = all_methods[2]
        self.newton = all_methods[3]
        self.secant = all_methods[4]
        self.vieta = all_methods[5]
        self.muller = all_methods[6]

    def graph_roots(self):
        # setting the number of iterations for each method
        bi_iterations = self.bisection.solution['iteration']
        false_iterations = self.falsePosition.solution['iteration']
        fixed_iterations = self.fixedPoint.list
        newton_iterations = self.newton.list
        secant_iterations = self.secant.list
        vieta_iterations = self.vieta.list
        muller_iterations = self.muller.list
        # setting list of roots for each method
        bi_roots = self.bisection.solution['root']
        false_roots = self.falsePosition.solution['root']
        fixed_roots = self.fixedPoint.appRoots
        newton_roots = self.newton.appRoots
        secant_roots = []
        secant_roots.append(self.secant.appRoots[0][1])
        secant_roots.extend(self.secant.appRoots)
        vieta_roots = self.vieta.appRoots
        muller_roots = []
        muller_roots.append(self.muller.appRoots[0][1])
        muller_roots.extend(self.muller.appRoots)
        del secant_roots[1]
        del muller_roots[1]
        # plotting each graph
        plt.plot(bi_iterations, bi_roots, "o-", label = 'Bisection')
        plt.plot(false_iterations, false_roots, "o-", label = 'False Position')
        plt.plot(fixed_iterations, fixed_roots, "o-", label = 'Fixed Point')
        plt.plot(newton_iterations, newton_roots, "o-", label = 'Newton Raphson')
        plt.plot(secant_iterations, secant_roots, "o-", label = 'Secent')
        plt.plot(vieta_iterations, vieta_roots, "o-", label='Birge Vieta')
        plt.plot(muller_iterations, muller_roots, "o-", label = 'Muller')
        plt.title("no. of iterations & roots")
        plt.xlabel("No. of iterations")
        plt.ylabel("Roots")
        plt.legend(loc='upper right')
        plt.grid()
        plt.show()


    def graph_errors(self):
        # setting the number of iterations for each method
        bi_iterations = self.bisection.solution['iteration']
        false_iterations = self.falsePosition.solution['iteration']
        fixed_iterations = self.fixedPoint.list
        newton_iterations = self.newton.list
        secant_iterations = self.secant.list
        vieta_iterations = self.vieta.list
        muller_iterations = self.muller.list
        # setting list of errors for each method
        bi_errors = self.bisection.solution['ea']
        false_errors = self.falsePosition.solution['ea']
        fixed_errors = self.fixedPoint.errors
        newton_errors = self.newton.errors
        secant_errors = self.secant.errors
        vieta_errors = self.vieta.errors
        muller_errors = self.muller.errors
        # plotting each graph
        plt.plot(bi_iterations, bi_errors, label = 'Bisection')
        plt.plot(false_iterations, false_errors, label = 'False Position')
        plt.plot(fixed_iterations, fixed_errors, label = 'Fixed Point')
        plt.plot(newton_iterations, newton_errors, label = 'Newton Raphson')
        plt.plot(secant_iterations, secant_errors, label = 'Secent')
        plt.plot(vieta_iterations, vieta_errors, label='Birge Vieta')
        plt.plot(muller_iterations, muller_errors, label = 'Muller')
        plt.title("no. of iterations & errors")
        plt.xlabel("No. of iterations")
        plt.ylabel("Errors")
        plt.legend(loc='upper right')
        plt.grid()
        plt.show()
