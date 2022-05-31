

# 元祖
# 1.定义 ： 变量=()

tp1 = ()
tp2 = (1,3,4,'hello')
print(tp1)
print(tp2)

# 2.循环
for x in tp2:
    print(x)

#字典的定义 d （变量名）= {key1:value1,key2:value2}
# 创建字典
dct1 = {} #空字典
dct2 = {'a': 1, 'b': 3,'c':4}
print(dct1)
print(dct2)


# 字典的获取：
print("获取字典dct2中键名为b的值：",dct2['b'])
#print("获取字典dct2中键名为d的值：",dct2['d']) # 键名不存在会报错
# print("获取字典dct2中键名为b的值：",dct2['b'])

# 字典的获取：dict.get(键名)
print("获取字典dct2中键名为b的值：",dct2.get('b'))
print("获取字典dct2中键名为d的值：",dct2.get('d'))



# 3.更新字典的某个值：dict['键名'] = 新值
dct2['b']=22
print(dct2)

# 更新字典里的值到另外一个字典： dict.update(dict1)
dct3 = {'e':55,'f':'hello'}
dct2.update(dct3)
print('更新后字典显示：',dct2)

# 判断键是否存在字典中 '键名' in dct
print('e'in dct2)
print('e'in dct1)

# 获取字典中所有的键名 ： dict.keys()
print('获取字典中所有的键名：',dct2.keys())

for x in dct2.keys():
    print(x)

#获取字典中所有的值：dict .values()
print('获取字典中所有的值：',dct2.values())

for x in dct2.values():
    print(x)

# 获取字典中所有键值对：dct2.items()
print('获取字典中所有键值对：',dct2.items())
for x,y in dct2.items():
    print(x,y)













