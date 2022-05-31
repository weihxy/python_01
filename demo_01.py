
# 定义变量
a = 88
b = 21
c = True
d = -555

print(a)
print (b)
print(c)
print(d)

# 定义变量的其他方式
e,f =2,8
g=b + d
print (g)
# print 方法
print("hello world")
print("hello python")
print (1*2)

# type方法
print (type(111))
type(print("hello python"))

# 算数运算符
print(a + b )
print(a - b)
print(a * b)
print(a / b,type(a /b))
print(a//b,type(a//b))
print(a%b,type(a%b))
print(a**b)
print(a>b,type(a>b))
print(a>=b,type(a>=b))
print(a<b,type(a<b))
print(a<=b,type(a<=b))
print(a==b,type(a==b))
print(a!=b,type(a!=b))
print(a is b,type(a is b))
print(a is not b,type(a is not b))

# 赋值运算符
a+=b
print(a)
a-=b
print(a)
a*=b
print(a)
a/=b
print(a)
a%=b
print(a)
a**=b
print(a)
a//=b
print(a)
# 逻辑运算符
x = True # a>2
y = False# b<0
print(x and y)
print(x or y)
print(not x)
print(not y)

# 条件语句
"""
格式：
if 条件语句:
   执行代码块
"""

if 13<12:
    print("13是小于12的数")
else:
    print("13是大于12的数")


"""多条件判断格式：
if 条件判断1：
代码1
elif 条件判断2：
代码2
elif 条件判断3：
代码3
else：
代码4
"""
score = 76
if score >90:
    print("优秀")
elif score > 80:
    print("良")
elif score >60:
    print("及格")
else:
    print("不及格")

if score > 75 and score < 90:
    print("良")

if 0:
    print("T")
if 0.22:
    print("T")
if -33:
    print("T")
if "":
    print("T")
if "hhh":
    print("T")
if None:
    print("T")