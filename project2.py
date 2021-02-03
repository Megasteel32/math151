from sympy import *
# Question 1
x = Symbol('x')
prob1a = solve(-exp(3*x) + 10 * exp(2*x))
pprint(prob1a)

prob1b = solve(log(x-1) + log(x+2) - 2)
pprint(prob1b)

# Question 3
plot(sin(2*x) - 2 * sin(x), xlim = [0, 2*pi])

prob3b = solve(sin(2*x) - 2 * sin(x))
pprint(prob3b)

prob3c = solve(2 * cos(2*x) - 2 * cos(x))
pprint(prob3c)