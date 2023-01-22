import os
import math
'''
Exponential distribution
lambda_ is lambda (cannot use lambda because it is a python keyword)
'''
chapter = 4

class Expon:
    def __init__(self, lambda_):
        assert lambda_ > 0
        self.lambda_ = lambda_

    def pdf(self, x): # probability for a single variable
        return 0 if x < 0 else self.lambda_ * (math.e**(-self.lambda_ * x))

    def cdf(self, x): # is inclusive of x i.e <=x
        return 0 if x <= 0 else 1-(math.e**(-self.lambda_ * x))

    def range_cdf(self, lower, upper): # lower <= x < upper
        return self.cdf(upper)-self.cdf(lower)

    @property
    def mean(self):
        return 1/self.lambda_

    @property
    def variance(self):
        return 1/(self.lambda_**2)

    @property
    def std_dev(self):
        return self.variance ** 0.5

    @property
    def stats(self):
        return {"mean": self.mean,"variance":self.variance}


def details():
    os.system("exponential_distribution.png")

def get_lambda_from_mean(mean:float):
    return 1/mean