
# 面向对象
#1.定义一个电梯的类：class 类名()
class Elevator():
    #2.在类的里面申明车的属性（数据）和方法（函数）
    button = "未激活"
    max_people_nums = 15
    floor = 8
    #打开、关闭、运行电梯
    def open(self):
        print("开门")

    def close(self):
        print("关门")

    def run(self):
        print("电梯启动运行")
# 3.定义一个具体的对象，叫初始化对象，==>初始化对象：对象名=类名()
el = Elevator()
# 4.使用对象调用方法或属性 ： 对象名.属性||  对象名.方法
el.open()
el.close()
el.run()

# 类的定义
#实例: 创建学生类，要求有属性：姓名和年级 ; 方法有：学习的方法，打印学生的上课情况

class Students():
    name = ""
    grade = 0
    def study(self):
        print("学生{},目前{}年级".format(self.name,self.grade))
        return
s = Students()
s.name = "张三"
s.grade = 5
print(s.study())











