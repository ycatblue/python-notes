# The endswith() method returns True if the string ends with the specified value, otherwise False.
txt = "hello,welcome to my house."
x = txt.endswith(".")
y = txt.endswith("?")
print(x)
print(y)

# Syntax:string.endswith(value, start, end)
a = "Hello, welcome to my world."
b = txt.endswith("my world.", 5, 11)
print(b)
