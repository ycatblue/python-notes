# 定义一个动物类
class Animal:
    food = '香蕉'

    def __init__(self, name):
        self.name = name

    def eat(self):
        print("%s正在吃%s" % (self.name, Animal.food))


# 创建Animal类的一个对象cat。
monkey = Animal('小猴子')
monkey.eat()
# print(monkey.food)

# 创建一个cat实例对象，将其food属性修改为“猫粮”；然后添加一个属性do，值为“捉老鼠”；最后删除do属性。
cat = Animal('cat')
cat.food = '猫粮'
print(cat.food)
cat.do = '抓老鼠'
print(cat.do)
del cat.do  # 删除do属性
cat.eat()


# 定义一个Persion类，类中定义一个私有变量__name和一个私有方法__eat( )
class Persion(object):
    def __init__(self):
        self.__name = 'persion'

    def __eat(self):
        print('私有方法')


# xiao_ming = Persion()
# xiao_ming.__name

