#datetime模块

import datetime
print(datetime.datetime.now())
df='2020-08-09 11:28:25'
##import _strptime
#print(datetime.strptime(df,"%Y-%m-%d %H:%M:%S"))

#sys

import sys

print(sys.path)

#读取文件：

# 1.打开文件：open(filename,mode)  #filename:文件名 mode：读写模式
file = open('b.txt','r')
# 2. 读取
text = file.read()
print(text)


# 3. 关闭
file.close()

# 1.打开文件：open(filename,mode)  #filename:文件名 mode：读写模式
file = open('b.txt','w')
#4.写内容
file.write("hello")
file.write("world")

# 打开⽂件
file = open('b.txt')
while True:
    line = file.readline()
    if not line:
        break
# 每读取⼀⾏的末尾已经有了⼀个 \n
print(line, end="")
# 关闭⽂件
file.close()
file = open('b.txt')
# 读取所有的行
for x in file.readlines():
    print(x)


# 错误与异常

def div(x,y):
    z =x / y
    return z

print(div(3,1))

#try ... except语句
"""语法格式：
try:
可能出现异常的代码块
except Exception as e:
print(e)
"""
def div1(x,y):
    try:
        z =x / y
        return z
    except Exception as e:
        print("除法不能敲零")
        print(e)



print(div1(3,0))

#try...except...finally语句
"""语法格式：
try:
可能出现异常的代码块
except Exception as e:
print(e)
finally:
必须要执行的语句
"""





