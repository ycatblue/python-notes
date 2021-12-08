# 将 'python' 以列表形式输出为单个字母
a_str = 'python'
print([i for i in a_str])

# 求出所有小于20的偶数
a_list = [i for i in range(20) if i % 2 == 0]
print(a_list)

# 互换字典中的key和value
a_dict = {'py': 'python', 'sel': 'selenium', 'at': 'autotest'}
dict_conversion = {v: k for k, v in a_dict.items()}
print(dict_conversion)

# 求出小于10的所有数的平方。
dict_k = {x ** 2 for x in range(1, 10)}
print(dict_k)
