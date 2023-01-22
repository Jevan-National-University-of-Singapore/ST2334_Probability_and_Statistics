from scipy.stats import f

class F:
    def __init__(self, sample_1, sample_2): # :param sample: dict[n, variance]
        self.sample_1 = sample_1 #numerator
        self.sample_2 = sample_2 #denominator

    def pmf(self, x):
        return f.pdf(self.normalise(x), self.n-1)

    def cdf(self, x): # is inclusive of x i.e <=x
        return f.cdf(self.normalise(x), self.sample_1[0]-1, self.sample_2[0]-1)

    def normalise(self, x):
        return x * (self.sample_2[1]/self.sample_1[1])

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