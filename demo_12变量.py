


# 1.类变量（作用范围最大）
class Students(object):
    name = ""
    grade = ""
#通过类名调用：类名.变量名
Students.name = "张三"
Students.grade = '5'
print(Students.name)
print(Students.grade)
#通过实例进行调用：对象名.变量名
s = Students()
print(s.name)
print(s.grade)

#2.实例变量:对象名.方法()
class Students(object):
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
s = Students("张三",5)
print(s.name)
print(s.grade)


#3.局部变量:变量名（只能在方法内使用）
class Students(object):
    def study(self,name):
        val = "hello"
        print("{} {}".format(val,name))
s = Students()
s.study("g")

