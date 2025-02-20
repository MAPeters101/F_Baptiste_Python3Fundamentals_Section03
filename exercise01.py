"""
Exercise 1
Given two floats a and b, and some tolerance tol, write an expression that
will test whether a and b are within tol of each other.
"""

a = 0.1
b = 0.11
tol = .009
print(abs(a-b) < tol)

a = 0.1
b = 0.11
tol = .012
print(abs(a-b) < tol)


