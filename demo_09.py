

#所谓的函数，就是具有特定功能的代码块

#def 函数名(参数列表):函数体

#定义函数：两个数相加
def add(x,y):
    z = x+ y
    print(z)
    return z


#调用函数：
print(add(3,4))
 # 位置参数：参数位置要一一对应，不能颠倒
print(add(1,2)) #正确
print(add('hello','world')) #正确
#print(add(3)) #不正确，报TypeError异常
#print(add(1,2,3)) #不正确，报TypeError异常


# 关键字参数：关键字参数是指传值时要以key=value形式
def student_lesson(grade,subject):
    z = "{}年级上{}课".format(grade,subject)
    return z
print(student_lesson(3,'英语')) #位置参数
print(student_lesson(grade=4,subject='数学')) #关键字参数
print(student_lesson(subject='语文',grade=5)) #关键字参数可以调换位置
print(student_lesson(6,subject='体育')) #关键字参数和位置参数混合使用。位置参数必须在前，关键字参数在后，否则会报错。

#默认参数：如果设置默认参数，需放在位置参数后,即放在最后面
def study_language(name,language='python'):
    info = ("{}要学习{}语言".format(name,language))
    return info
# 调用函数时，给language传递值java
print(study_language("张三",'java'))
# 调用函数时，给language不传递任何值
print(study_language("张三","python"))










