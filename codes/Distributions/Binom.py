from scipy.stats import binom
from .Poisson import Poisson
from . import Normal

chapter = 4

class Binom:
    def __init__(self, n, p):
        self.n = n
        self.p = p

    def pmf(self, x): # probability for a single variable
        return binom.pmf(x,self.n,self.p)

    def cdf(self, x): # is inclusive of x i.e <=x
        return binom.cdf(x, self.n, self.p)

    def range_cdf(self, lower, upper): # lower <= x < upper
        return self.cdf(upper-1)-self.cdf(lower-1)

    @property
    def mean(self):
        return self.n*self.p
    @property
    def variance(self):
        return self.n*self.p*(1-self.p)
    @property
    def stats(self):
        return {"mean": self.mean,"variance":self.variance}

    def to_poisson(self):
        return Poisson(mu=self.mean)

    def to_normal(self):
        return Normal.Normal(
            mean = self.mean,
            variance=self.variance
        )
        

def pmf(n,p,x):
    return binom.pmf(x,n,p)

def cdf(n,p,x):
    return binom.cdf(x,n,p)

def range_cdf(n, p, lower, upper): # lower <= x < upper
    return cdf(n, p, upper-1) - cdf(n, p, lower-1)    

def mean(n, p):
    return n*p

def variance(n, p):
    return n*p*(1-p)

def stats(n, p):
    return {"mean": Binom.mean(n,p),"variance":Binom.variance(n,p)}

def to_poisson(n, p):
    return Poisson(mu=n*p)

def poisson_estimate_conditions():
    print("n must be large, p  must be smalle")