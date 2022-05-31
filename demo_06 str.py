# 字符串的格式化
my_str = "my name is %s"% ('李四')
print(my_str)

my_str = "张三 今年 %d 岁"%(22)
print(my_str)

my_str = "一斤苹果%f元"%(11)
print(my_str)

#辅助指令 ： m.n
my_str = "一斤苹果%5.2f元"%(11)
print(my_str)

#显示左对齐 ：-
my_str = "一斤苹果%-7.2f元"%(11)
print(my_str)

#+ ：在正数前面显示加号(+)
my_str = "一斤苹果%+7.2f元"%(11)
print(my_str)

#0 ： 显示的数字前面填充0而不是默认的空格

my_str = "一斤苹果%07.2f元"%(11)
print(my_str)


#使用format()方法进行字符串格式化：: “{}”.format("传入的字符串")
my_str = "张三 今年 {}岁".format(23)
print(my_str)

#format格式化两个参数
print("今天星期{}，张三买了{}斤苹果".format('二',3))

#format位置参数
print("我是位置参数：{0} {1}".format('hello','python'))
print("我是位置参数：{0} {2} {1}".format('hello','python','2'))

#format:是关键字参数
print("我是关键字参数：{y} {x}".format(x='hello',y='0'))

#结合使用：位置参数和关键字参数可以结合起来使用，当它们结合起来使用时，位置参数必须放在关键字前面
print("今天星期{0}，张三买了{x}斤苹果".format('二',x='3'))









