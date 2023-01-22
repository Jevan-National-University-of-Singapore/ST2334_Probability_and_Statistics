from scipy.stats import t
import math

class T:
    def __init__(self, mean, variance, n):
        self.mean = mean
        self.variance = variance/n
        self.n = n

    def pmf(self, x):
        return t.pdf(self.normalise(x), self.n-1)

    def cdf(self, x): # is inclusive of x i.e <=x
        return t.cdf(self.normalise(x), self.n-1)

    def normalise(self, x):
        return abs(x-self.mean)/self.std_dev

    def range_cdf(self, lower, upper): # lower <= x < upper
        return self.cdf(upper)-self.cdf(lower)

    def z(self, p):
        return abs(t.ppf(p, self.n-1))

    # def x(self, p):
    #     return self.z(p) * self.std_dev + self.mean

    @property
    def std_dev(self):
        return math.sqrt(self.variance)


    @property
    def stats(self):
        return {"mean": self.mean,"variance":self.variance}

class StandardT(T):
    def __init__(self, n):
        super().__init__(mean=0, variance=1, n=n)

# def formula():
#     os.system("continuous_uniform_distribution.png")