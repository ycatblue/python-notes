n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))


def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(5, 2))


# 定义函数时参数组合传入的顺序是：位置参数(必须参数)、缺省参数、可变参数、关键字参数
def tree_info(tree_id, date='2021/12/13', *local, **un):
    print('id:', tree_id, 'date:', date, 'local:', local, 'un:', un)


print(tree_info(1))
print(tree_info(2, '2021/12/12'))
print(tree_info(2, '2021/12/12', 'SZ'))
print(tree_info(3, '2021/12/12', 'SZ', u1='u1', u2='u2'))
