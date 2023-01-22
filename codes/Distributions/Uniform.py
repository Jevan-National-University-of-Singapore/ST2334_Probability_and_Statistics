import os

class Uniform:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper

    def pdf(self, x): # probability for a single variable
        return 1/(self.upper-self.lower)

    def cdf(self, x): # is inclusive of x i.e <=x
        if x < self.lower:
            return 0
        return 1 if x > self.upper else (x-self.lower)/(self.upper-self.lower)

    def range_cdf(self, lower, upper): # lower <= x < upper
        return self.cdf(upper-1)-self.cdf(lower-1)

    @property
    def mean(self):
        return (self.lower + self.upper)/2

    @property
    def variance(self):
        return ((self.upper-self.lower)**2)/12

    @property
    def stats(self):
        return {"mean": self.mean,"variance":self.variance}


def details():
    os.system("continuous_uniform_distribution.png")