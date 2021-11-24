"""
 输入一个年龄，如果年龄小于等于0则输出“您还未出生”；如果年龄大于0且小于等于20则输出“您可以点点点了”；
 如果年龄大于20且小于60则输出“您是测试工程师”，否则输出“您已退休“。
 """

age = input("please input your age:")
age = int(age)

if age <= 0:
    print("您还未出生")

elif age <= 20:
    print("您可以点点点了")

elif age <= 60:
    print("您是测试工程师")
else:
    print("您已退休")

