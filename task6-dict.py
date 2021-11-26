# 创建字典dict={'py':'python', 'sel':'selenium', 'at':'auto'}
a_dict = {'py': 'python', 'sel': 'selenium', 'at': 'auto'}
print(a_dict)

# 获取字典{'py':'python', 'sel':'selenium', 'at':'auto'}中key为py的值，然后获取一个不存在的key
print(a_dict['py'])
# print(a_dict['hi'])

# （1）将键为py的值修改为['py','python']。
# （2）添加新的元素，新元素为'w': 'web'。
a_dict['py'] = '[py,python]'
a_dict['w'] = 'web'
print(a_dict)

# 删除key为py的元素，然后清空字典中元素。
del a_dict['py']
print(a_dict)
# a_dict.clear()


