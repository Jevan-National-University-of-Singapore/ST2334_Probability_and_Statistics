from scipy.stats import norm
import math

class Normal:
    def __init__(self, mean, variance):
        self.mean = mean
        self.variance = variance

    def pmf(self, x):
        return norm.pdf(self.normalise(x))

    def cdf(self, x): # is inclusive of x i.e <=x
        return norm.cdf(self.normalise(x))

    def normalise(self, x):
        return abs(x-self.mean)/self.std_dev

    def range_cdf(self, lower, upper): # lower <= x < upper
        return self.cdf(upper)-self.cdf(lower)

    def z(self, p):
        return abs(norm.ppf(p))

    def x(self, p):
        return self.z(p) * self.std_dev + self.mean

    @property
    def std_dev(self):
        return math.sqrt(self.variance)


    @property
    def stats(self):
        return {"mean": self.mean,"variance":self.variance}


# def formula():
#     os.system("continuous_uniform_distribution.png")

class StandardNormal(Normal):
    def __init__(self):
        super().__init__(mean=0, variance=1)