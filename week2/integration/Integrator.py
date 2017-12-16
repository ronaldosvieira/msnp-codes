import numpy as np
import math


class Integrator:
    def __init__(self, xMin, xMax, N):
        self.xMin = xMin
        self.xMax = xMax
        self.N = N
        self.delta_x = (xMax - xMin) / (N - 1)
        self.res = 0.0

    def integrate(self):
        X = np.arange(self.xMin, self.xMax, self.delta_x)

        self.res = ((X ** 2)
                    * np.array([math.e ** (-x) for x in X])
                    * np.sin(X)
                    * self.delta_x).sum()

    def show(self):
        print("%.5f" % self.res)


examp = Integrator(1, 3, 200)
examp.integrate()
examp.show()
