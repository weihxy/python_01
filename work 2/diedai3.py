"""
## 需求-迭代3：用户新增功能:
1. 将默认用户数据放在文件中保存，以上迭代功能查询数据都要从文件查询 。
2. 需要对文件的读写进行异常捕获
3. 用户可以输入关键字add进行新增用户 ，新增的用户信息可以保存到文件中 。
4. 同时进行查询时，也能查询出该用户 。
5. 当用户添加成功时，在返回的结果中要创建时间。
"""


# 方法 ：从文件中读取数据，返回的是列表形式的数据
def from_file_get_data(file_name):
    f = None
    try:
        f = open(file_name, 'r')
        line = f.readline()
        user_data = eval(line)
        return user_data
    except Exception as e:
        print(e)
    finally:
        if not f:
            f.close()






# 方法 ：向文件中写入内容，用户添加的信息是在原来的基础上添加的。






#1.定义用户默认数据:[a1,a2]
#user_list = [{'role': 'admin', 'account': 'admin', 'password': '123456', 'dept': 'tester'}, {'role': 'user', 'account': 'dev', 'password': '123456', 'dept': 'dev'}]
user_list = []
user_list


#2.定义返回结果：
result = {"code":0,"message":""}


#3.定义登录功能
def login(username,password):
    #用户名或密码为空
    if username is None or username =="":
        result.update({"code":1,"message":"用户名不能为空"})
        return result
    if password is None or password == "":
        result.update({"code": 1, "message": "密码不能为空"})
        return result
    #登陆成功
    for user_info in user_list:
        if username == user_info.get('account') and password == user_info.get('password'):
            result.update({"message":"登陆成功","user_list":user_list})
            return result

    #用户名或密码不匹配或错误
    result.update({"code":1,"message":"请检查您的用户名或密码是否填写正确"})
    return result
#创建一个类：包括新增用户、修改用户、删除用例、查询用户
class User():


     # 添加用户的方法
     def add_user(self):

#定义用户查询功能
    def get_user(self,username):

    # 判断用户名是否登录，若登陆成功才能进行查询，否则返回权限不足
        if not result.get('code') :
            result.update({"code":11,"message":"用户未登录，无法查询"})
            return result

    #输入正确用户名进行查询，返回结果（支持模糊查询）
        result.update({"user_list":[]})
        lst = [] #存放查询到结果的数据
        for x in user_list:
            account = x.get('account')
            if username in account: #支持模糊查询
                x.pop('password')
                lst.append(x)
    #判断新列表里的数据，如果列表不为空，查询成功，返回对应结果
        if lst !=0:
             result.update({"massage":"查询用户成功！","user_list":lst})
             return result

    # 若用户名输入不正确，返回无查询结果
        result.update({"code":12,"message":"未查询到用户，请重新输入"})
        return result



if __name__ == '__main__':
    #1.进行循环，以便用户做各种操作
    flag = True

    while flag:

        #提供用户的各种选择，比如1代表登录操作，2代表查询操作，输入q：退出操作
        vls = input("操作请输入对应的编号："
              "\n 1:进行登录："
              "\n 2:查询用户，请输入用户名："
              "\n q:退出："
              "\n 其他字符：位置操作，请重新输入：")
        #当输入未知符号后，进行重新输入
        if vls not in ('1','2','q','quit'):
            print("="*30)
            continue
        #进行登录操作
        if vls == '1':
            username = input("请输入用户名：")
            password = input("请输入密码：")
            login_result = login(username,password)
            print(login_result)
            continue


        #进行查询用户的情况
        if vls == '2':
            name = input("请输入查询用户：")
            get_result = get_user(name)
            print(get_result)
            continue


        #是否退出
        if vls in ('q','quit'):
            flag = False
            print("退出成功！")

