from scipy.stats import chi2

class ChiSquare:
    def __init__(self, n, variance):
        self.n = n
        self.variance = variance

    def pmf(self, x):
        return chi2.pdf(self.normalise(x), self.n-1)

    def cdf(self, x): # is inclusive of x i.e <=x
        return chi2.cdf(self.normalise(x), self.n-1)

    def normalise(self, x):
        return ((self.n-1)*x)/self.variance

    def range_cdf(self, lower, upper): # lower <= x < upper
        return self.cdf(upper)-self.cdf(lower)

    # def z(self, p):
    #     return norm.ppf(p)

    # def x(self, p):
    #     return self.z(p) * self.std_dev + self.mean

    # @property
    # def std_dev(self):
    #     return math.sqrt(self.variance)


    # @property
    # def stats(self):
    #     return {"mean": self.mean,"variance":self.variance}


# def formula():
#     os.system("continuous_uniform_distribution.png")