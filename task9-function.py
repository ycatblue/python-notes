# 定义一个打印自己名字的函数say_name(a_name)
def say_name(a_name):
    print("my name is " + a_name)


say_name("laney")


# 定义一个打招呼的函数，并且给招呼语设置一个默认参数(缺省值)。
def say_hello(b_name, say="hello"):
    return b_name + say


print(say_hello('jhon '))
print(say_hello('小花', '你好'))


# 定义一个计算数字相加的函数。由于不知道有多少数字进行相加，所以需要使用可变参数。
def add_num(*a_num):
    a_sum = 0
    for i in a_num:
        a_sum += i
    return a_sum


print(add_num(1, 32, 423, 54))
print(add_num())

a_list = [22, 43, 43, 433]
print(add_num(*a_list))


# 定义一棵数，可以确定的是树编号、栽种时间，当然还有一些不清楚的属性，对于这些不清楚的属性就可以使用关键字参数
def tree_info(tree_id, tree_date, **un):
    return 'id:', tree_id, 'date:', tree_date, 'others:', un


print(tree_info(1, '2021/12/13'))
print(tree_info(2, '2021/12/13', Area='guangdong', u='maya'))

