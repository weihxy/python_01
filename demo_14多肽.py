#多肽

"""
如果满足如下两个条件，就是类的多态：
1. 继承：多态一定是发生在子类和父类之间；
2. 重写：子类重写了父类的方法。
"""

class People():
    def eat(self,ids):
        print("{}吃饭".format(ids))
class Students(People):
    def eat(self,grade):
        super().eat(grade)
        print(grade,"年级的学生在吃饭")

class Teacher(People):
    def eat(self,subject):
        print(subject,"老师在吃饭")
s =Students()
s.eat("二")

t = Teacher()
t.eat("语文")









