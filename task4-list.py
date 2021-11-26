# 获取列表中的第三个元素，再获取列表中的最后一个元素。
a_list = ["Monday", "Tuesday", "Wednesday"]
print(a_list[1])
print(a_list[-1])


# （1）使用append( )方法在list最末尾添加元素selenium。
# （2）使用extend( )方法在list最末尾添加['auto', 'test']。
# （3）使用insert( )方法在list第5个元素位置添加元素insert。

a_list.append("selenium")
a_list.extend(["Friday", "Sunday"])
a_list.insert(4, "insert")

print(a_list)


# （1）使用remove(name)方法移除list中的“python”元素。
# （2）使用del list[index]方法移除索引为2的元素。
# （3）使用pop( )方法移除list的最后一个元素，并且将最后一个元素赋值给temp。

b_list = ["python", "php", "java", "C#"]
b_list.remove("python")
del b_list[2]
temp = b_list.pop()

print(temp)
print(b_list)

# （1）获取列表['hello', 'python', 321, "您好"]中索引为1和2的元素并且组成一个新的列表。
# （2）获取列表['hello', 'python', 321, "您好"]中索引为1、包含1之后的所有元素并且组成一个新的列表。
# （3）获取列表['hello', 'python', 321, "您好"]中索引为3、不包含3之前的所有元素并且组成一个新的列表。

c_list = ['hello', 'python', '321', '您好']
d_list = c_list[1:3]
e_list = c_list[1:]
f_list = c_list[:3]
print(d_list)
print(e_list)
print(f_list)


