# 循环语句
"""for 循环
for 循环变量 in 序列
代码块
"""
# 需求： 循环字符串abcdef中的每个字符
for y in "abcdef":
    print(y)

# while 循环
"""
while 条件语句(condition):
daimakuai (statement)
"""
# 需求：打印1到5的数
a = 1
while a<=5:
    print(a)
    a += 1
# 需求：1-100内所有数的和
a = 1
b = 0
while a<= 100:
    b += a
    a += 1
print(b)

# range ()方法
"""
range (start,end,step)
"""
for x in range(0,10,3):
    print(x)
for x in range(0,20,5):
    print(x)

# 使用break语句
# 需求：循环1-10，到7时结束循环
a = 1
"""while a<=10:
    if x == 7:
        break
    print(a)
    a += 1
    """
for x in range(1,11,1):
    print(x)
    if x == 7:
        break
for x in range(1,11,1):
    if x == 7:
       continue
    print(x)