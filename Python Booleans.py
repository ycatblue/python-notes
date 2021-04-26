# When you compare two values, the expression is evaluated and Python returns the Boolean answer:
print(10 > 9)
print(10 == 9)
print(10 < 9)

# When you run a condition in an if statement, Python returns True or False:
a = 200
b = 3
if a > b:
    print("b is greatar than a")
else:
    print("b is not greater than a")

# The bool() function allows you to evaluate any value, and give you True or False in return
print(bool("hello"))
print(bool(15))

x = "hello"
y = 15
print(bool(x))
print(bool(y))

# Almost any value is evaluated to True if it has some sort of content
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

"""
In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", 
the number 0, and the value None. And of course the value False evaluates to False.
"""
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

"""
One more value, or object in this case, evaluates to False, and that is if you have an object that is made 
from a class with a __len__ function that returns 0 or False:
"""


class myclass():
    def __len__(self):
        return 0


myobj = myclass()
print(bool(myobj))


# Functions can Return a Boolean
def myFuntion():
    return True


if myFuntion():
    print("Yes")
else:
    print("NO")

#  isinstance() function, which can be used to determine if an object is of a certain data type:
x = 200
print(isinstance(x, int))
