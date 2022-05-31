#可变化参数：这里的可变化参数指的参数的数量可以发送变化
def add(a,b,*args):
    print(args)
    z =a + b + sum(args)
    return z


print(add(3,5,7,5,88))


#传入列表，注意，列表前需要加*
print(add(3,4,*[4,5,-1]))


#可变参数可接收字典中的元素 。在函数中是以双星**表示
def show_info(**kwargs):
    print(kwargs)
show_info() #可变参数也可以不传入任何参数
show_info(key1="python") #传入一个参数
show_info(key1="python",key2='java') #传入多个参数
show_info(**{'key1':'python','key2':'java'}) #传入字典，注意，列表前需加*


#同样的位置参数和可变参数结合起来使用。
def fun_name(*args,**kwargs): #此函数可以接收任何长度，任何位置，任何关键字的参数

