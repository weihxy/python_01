'''
## 需求-迭代1：登录功能
1. 定义两条用户数据 ，要求用户数据的属性包括用户角色，用户账号，密码，部门
2. 要求返回的格式是字典形式 ，包含两个字段，code和message ,code为0代表成功，为1代表失败 ；message给出相应的提示 ，格式如 ：{'code':0,'message':'登录成功'}
3. 用户通过控制台输入用户名和密码，判断用户名和密码是否和定义数据中的用户名密码相匹配，若匹配返回成功登录消息体，并把用户列表也追加到返回结果中,{'code':0,'message':'登录成功',user_list:[]}
4. 若用户名输入为空或密码输入为空，都给出对应的提示，如用户名不能为空
5. 若用户名或密码不匹配，都给出登录失败，请检查您的用户名或密码是否填写正确。
'''

#1.定义用户默认数据:[a1,a2]
user_list = [{'role': 'admin', 'account': 'admin', 'password': '123456', 'dept': 'tester'}, {'role': 'user', 'account': 'dev', 'password': '123456', 'dept': 'dev'}]

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





if __name__ == '__main__':
    username = input("请输入用户名：")
    password = input("请输入密码：")


    print(login(username,password))







"""
def login
class login():
    user1_dct = {'role': 'admin', 'account': 'admin', 'password': '123456', 'dept': 'tester'}
    user2_dct = {'role': 'user', 'account': 'dev', 'password': '123456', 'dept': 'dev'}
    def input(self,role,account,password,dept):
        self.role=role
        self.account =account
        self.password = password
        self.dept=dept

    def log1(self,account,password):
        if account == self.account and password==self.password:
            print({'code':0,'message':'登录成功'})
        else:
            print({'code':1,'message':'登录失败'})
    def log2(self,account,password):
        if account == self.account and password == self.password:
            print({'code': 0, 'message': '登录成功',user_list:{role:self.role,account:self.account,password:self.password ,dept:self.dept}})
        elif account ==" ":
            print("用户名不能为空")
        elif password == " ":
            print("密码不能为空")
        else:
            print({'code': 1, 'message': '登录失败'},"请检查用户名或密码是否正确")

l = login()
user_account = input("请输入用户名：")
user_password = input("请输入密码：")
l.log1()

"""



