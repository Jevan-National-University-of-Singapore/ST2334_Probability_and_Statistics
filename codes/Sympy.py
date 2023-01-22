import sympy as sym

#subs() function in SymPy replaces all occurrences of the first parameter with the second

theta = sym.Symbol("theta")
x = sym.Symbol("x")

f_1 = theta-x
integral_1 = sym.integrate(f_1, (x, theta-1, theta))

f_2 = x-theta
integral_2 = sym.integrate(f_2, (x, theta, theta+1))


print(sym.simplify(integral_1 + integral_2))
