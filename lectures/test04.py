# a = 3

# b = 6

# print(a, b)

# a, b = b, a

# print(a, b)

# str_a = "ABCDEFGHIJKL"

# print(str_a[1::3])

t = list(range(10))

def mult_3(x):
    return x * 3

a = map(mult_3, t)

b = map(mult_3, a)

print(list(b))