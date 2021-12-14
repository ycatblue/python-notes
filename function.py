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

# 匿名函数:实现x与y的乘积。
lam = lambda x, y: x * y
print(lam(2, 4))


# 定义一个函数并且有一个参数，该参数的建议数据类型为int；然后调用两次该函数，分别传入int、str类型的参数。
def par_type(numb: int):
    print(type(numb))
    return


par_type(2)
par_type('sad')


# 定义一个函数并且返回值的建议数据类型为string；然后调用两次该函数，分别使返回值类型为string和int。
def re_type(a)-> str:
    return a


re_type(print(type('abc')))
re_type(print(type(4)))

