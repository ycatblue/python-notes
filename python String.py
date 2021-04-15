# Strings in python are surrounded by either single quotation marks, or double quotation marks
print('hello')
print("hello")

# Multiline Strings
a = '''
    My name is laney,I'm form China,Guangdong
    I have a sister,she like singing
'''
print(a)

# Strings are Arrays
b = "university classmate"
print(b[2])

# Looping Through a String
for i in "laney":
    print(i)

# String length
c = "laney"
print(len(c))

# Check string
d = "You are so beautiful"
print("!" in d)

if "!" in d:
    print("yes,I think so")

else:
    print("No,I don't think so")

# Check if NOT
e = "Is he your brother?"
if "sister" not in e:
    print("No, he isn't")
else:
    print("Yes,she is")