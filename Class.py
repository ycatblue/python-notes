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
        # self.__name = 'persion' 私有变量
        self.name = 'persion'

    def __eat(self):
        print('私有方法')

    def food(self):
        print("火锅")

    def fruit(self):
        print("火龙果")


# xiao_ming = Persion()
# xiao_ming.__name


# 创建一个Persion类，然后创建一个Student类并继承Persion类。
class Student(Persion):
    pass


xiao_ming = Student()
xiao_ming.food()


# Student1类同时继承Persion1类和Persion2类
class Persion1(object):
    def __init__(self):
        pass

    def breakfast(self):
        print("牛奶")


class Persion2(object):
    def dinner(self):
        print("牛肉")


class Student1(Persion1, Persion2):
    pass


xiao_hong = Student1()
xiao_hong.breakfast()
xiao_hong.dinner()


# 定义三个类Persion类、Youth类和Student类，Persion类继承Object类，Youth类继承Student类，Student类继承Persion
class Youth(Student):
    pass


xiao_dong = Youth()
xiao_dong.fruit()


# 定义Pesion类，有一个name属性和一个eat( )方法，定义一个Student2类继承Persion类，并对继承的name属性和eat( )方法进行重写
class Student2(Persion):
    def __init__(self):
        # super() 用于继承父类中的属性
        super(Student2, self).__init__()
        print(self.name)

        # name的属性重写
        self.name = "student"
        print(self.name)

    # eat方法的重写
    def eat(self):
        print("吃有营养的食物")


xiao_xi = Student2()
xiao_xi.eat()
