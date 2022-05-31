
#封装：如果类中的变量和方法想设置为私有的，可以通过在变量或方法前个单下划线(_)或双下划线(__)
#如果是以_下划线开头的方法和属性，则是无法导入的。
#如果是以__下划线开头的方法和数学，则是无法直接调用的。


class Students():
    name = "张三"
    __score = "76"


    def set_score(self,score):
        self.__score =score

    def get_score(self):
        return self.__score

print(Students.name)
s = Students
#print(s.get_score(self.__score))

#s.set_score()



#继承

#父类-人类
class People():
    def eat(self,ids):
        print("{}吃饭".format(ids))


class Students(People):
    def study(self):
        print("学习")

class Teacher(People):
    def teach(self):
        print("教书")

s = Students()
s.eat("学生")
t = Teacher()
t.teach()



