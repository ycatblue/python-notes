"""
gen = (x for x in range(5))
a = type(gen)
print(a)
"""

# next(generator)
'''
b = next(gen)
b = next(gen)
b = next(gen)
b = next(gen)
b = next(gen)
print(b)
'''

'''for i in gen:
    print(i)'''


# send 方法
def sequence(numb):
    for i in range(numb):
        i = i * 3
        temp = yield i
        print(temp)


g = sequence(5)
print(next(g))
print(next(g))
print(g.send("sed发送参数"))
print(g.send(None))
