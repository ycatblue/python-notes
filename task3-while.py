# 使用while语句循环打印1到5。
"""i = 0
while i < 5:
    i += 1
    print("当前循环的数字是：", int(i))

print("循环结束")"""

# 循环打印1到5之间的奇数，当循环变量i=2时跳过，循环变量i=4时结束，退出循环。
i = 0
while i < 5:
    i += 1
    if i == 2:
        continue
    if i == 4:
        break
    print(int(i))
