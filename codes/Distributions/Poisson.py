from scipy.stats import poisson

class Poisson:
    def __init__(self, mu):
        self.mu = mu

    def pmf(self, x): # probability for a single variable
        return poisson.pmf(x, self.mu)

    def cdf(self, x): # is inclusive of x i.e <=x
        return poisson.cdf(x, self.mu)

    @property
    def mean(self):
        return self.mu

    @property
    def variance(self):
        return self.mu

    def stats(self):
        return {"mean": self.mean,"variance":self.variance}

    # @staticmethod 
    # def pmf(n,p,x):
    #     return poisson.pmf(x,n,p)

    # @staticmethod
    # def cdf(n,p,x):
    #     return binom.cdf(x,n,p)

    # @staticmethod
    # def mean(n, p):
    #     return n*p

    # @staticmethod
    # def variance(n, p):
    #     return n*p*(1-p)

    # @staticmethod
    # def stats(n, p):
    #     return {"mean": Binom.mean(n,p),"variance":Binom.variance(n,p)}
