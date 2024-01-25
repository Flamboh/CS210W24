"""
CIS 210 proj1 - types
Author: Oliver Boorstein
Credits: N/A
Demonstrating 5 examples of properties of real numbers that do not hold up for floating point numbers in Python
"""

# Asosciative property of multiplication. The result would be True if the numbers were real numbers
a = 10
b = 0.6
c = 0.2

print((a*b)*c == a*(b*c))

# Associative property of addition. The result would be True if the numbers were real numbers
d = 5
e = .4
f = .7

print(d+(e+f) == (d+e)+f)

# The below should not be equal as they are different numbers. It prints True as Python rounds them. Reference: https://ricomariani.medium.com/non-properties-of-floating-point-numbers-fc05ba2a919e
g = 1.1111111111111111111111111111111111111111111
h = 1.111111111111111111

print(g == h)

# Rounding with .5s. From math classes you would expect a constant rule of rounding up but Python rounds to the nearest even integer in this case.
i = 3.5
j = 2.5

print(f"round(3.5) = {round(i)}\nround(2.5) = {round(j)}")

# 0.1 is not exactly 1/10 so adding 3 of them will not equal to exactly 0.3 either. Reference: https://docs.python.org/3/tutorial/floatingpoint.html
k = 0.3
l = 0.1

print(l + l + l == k)