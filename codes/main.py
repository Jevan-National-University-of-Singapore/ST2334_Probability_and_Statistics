from Distributions import Binom, NBinom, Poisson, Uniform, Expon, Normal, T, ChiSquare, F
import Stats
from math import comb, perm
import sympy as sym
import math

ball = Binom.Binom(4, 3/8)
less_than = 0.5*ball.cdf(1)

#more than 1
more = 1-ball.cdf(1)
tails = (3/7) * (0.5) * more

print(ball.pmf(1) + (ball.pmf(3)))
