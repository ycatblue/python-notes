# （1）创建一个元组：tup=('hello', 'python', 321, "您好")。
# （2）创建一个空元组：tup =( )。

a_tup = ('hello', 'python', '321', '您好')
b_tup = ()
print(type(a_tup))
print(type(b_tup))

# 获取元组中第三个元素
print(a_tup[2])

# 将tup1 = ('hello', 'python')和tup2 = ('web', 'selenium')进行拼接，构成一个新的元组tup3
tup1 = ('hello', 'python')
tup2 = ('web', 'selenium')
tup3 = tup1 + tup2
print(tup3)

# 删除元组tup = ('hello', 'python', 321, "您好")
tup = ('hello', 'python', '321', '您好')
del tup



