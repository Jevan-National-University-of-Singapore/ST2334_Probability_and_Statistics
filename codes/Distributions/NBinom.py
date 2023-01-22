from scipy.stats import nbinom
import os      

'''
n is the number of success
p is the probability of success

x is the number of trials to reach n success, it is the random variable
'''
chapter = 4

class NBinom:
    def __init__(self, n, p):
        self.n = n
        self.p = p

    def pmf(self, x): # probability for a single variable
        return nbinom.pmf(x-self.n,self.n,self.p)

    def cdf(self, x): # is inclusive of x i.e <=x
        return nbinom.cdf(x-self.n, self.n, self.p)

    def range_cdf(self, lower, upper): # lower <= x < upper
        return self.cdf(upper-1)-self.cdf(lower-1)

    @property
    def mean(self):
        return self.n/self.p

    @property
    def variance(self):
        return ((1-self.p)*self.n)/(self.p ** 2)

    @property
    def stats(self):
        return {"mean": self.mean,"variance":self.variance}

    # def to_poisson(self):
    #     return Poisson(mu=self.n*self.p)
        
def formula():
    os.system("NBinom_pmf_formula.png")
# def pmf(n,p,x):
#     return binom.pmf(x,n,p)

# def cdf(n,p,x):
#     return binom.cdf(x,n,p)

# def range_cdf(n, p, lower, upper): # lower <= x < upper
#     return cdf(n, p, upper-1) - cdf(n, p, lower-1)    

# def mean(n, p):
#     return n*p

# def variance(n, p):
#     return n*p*(1-p)

# def stats(n, p):
#     return {"mean": Binom.mean(n,p),"variance":Binom.variance(n,p)}

# def to_poisson(n, p):
#     return Poisson(mu=n*p)