import os

class Distribution:
    def __init__(self, distribution: dict): # x: p
        self.distribution = distribution

    @property
    def mean(self):
        return sum([x*p for x,p in self.distribution.items()])

    @property
    def variance(self):
        mean = self.mean
        return sum([p*((x-mean)**2) for x, p in self.distribution.items()])

class Sample:
    def __init__(self, samples):
        self.samples = samples

    @property
    def size(self):
        return len(self.samples)

    @property
    def mean(self):
        return sum(self.samples)/self.size

    @property
    def variance(self):
        mean = self.mean
        return sum([(x-mean)**2 for x in self.samples])/(self.size-1)


def get_confidence_interval_conditions():
    os.system("confidence_intervals_conditions.png")
