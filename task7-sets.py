# 创建集合{'python', 'selenium', 'auto'}和集合{'m', 'o', 'a', 'y', 'h', '-', 'i', 'e', 'l', 'n', 't', 'u', 'p', 's'}。
test = {'python', 'selenium', 'auto'}
b_test = {'m', 'o', 'a', 'y', 'h', '-', 'i', 'e', 'l', 'n', 't', 'u', 'p', 's'}
print(test, b_test)

# （1）使用add( )将'grid'添加到test集合中。
# （2）使用update( )将['web', 'UI']添加到test集合中。
test.add('grid')
test.update(['web', 'UI'])
print(test)

# 从test集合中移除元素'web'和'UI'，再随机移除一个元素，最后清空集合。
test.remove('web')
test.discard('UI')
test.pop()
test.clear()
print(test)

# 拷贝一个集合
test.copy()
print(test)

# 返回多个集合的差集，交集，并集
a_test = {'python', 'selenium', 'auto'}
b_test = {'php', 'auto'}
c_test = {'php', 'python', 'auto'}
d_test = a_test.difference(b_test, c_test)  # 差集
e_test = a_test.intersection(b_test, c_test)  # 交集
f_test = a_test.union(b_test, c_test)  # 并集
print(d_test, e_test, f_test)

test