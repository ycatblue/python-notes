# String Format
age = 26
# txt = "I am " + age  cannot combine strings and numbers

# combine strings and numbers by using the format() method
txt = "My name is John, and I am {}"
print(txt.format(age))

'''
The format() method takes unlimited number of arguments
and are placed into the respective placeholders:
'''
math = 80
english = 100
chinese = 98
physics = 80
biology = 88
txt = "Your final grades are out. Math:{},Chinese:{},Physics:{},Biology:{},English:{}"
print(txt.format(math, chinese, physics, biology, english))

# use index numbers {0} to be sure the arguments are placed in the correct placeholders:
txt = "Your final grades are out. Math:{0},Chinese:{2},Physics:{3},Biology:{4},English:{1}"
print(txt.format(math, english, chinese, physics, biology))

