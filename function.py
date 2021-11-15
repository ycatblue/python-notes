n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))


def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(5, 2))
