# 列表

# 格式： 变量名 = []
alst = []
blst = [11,23,'hds',None]
print(alst)
print(blst)


#列表循环：
for x in blst:
    print("列表中的值:",x)


# 列表的方法：
clst = ['red','green','blue']

#在列表中添加新的元素： list.append(obj)
clst.append('black')
print(clst)

# 向列表中追加一个其他列表内的元素 ：list.count(seq)

clst.extend(blst)
print(clst)

#列表翻转 ： list.reverse()
clst.reverse()
print(clst)

# 列表排序：list.sort(),里面的元素必须是同类型的
# clst.sort()
# print(clst)


#统计在列表中出现的次数：list.count(obj)
print(clst.count('black'))

# 从列表中找出具体的某个元素的位置：list.index(obj)
print(clst.index(23))

#向列表中的某个位置插入元素 ： list.insert(index,obj)
clst.insert(1,'hello')
print(clst)

# 打印1-10的数
for x in [1,2,3,4,5,6,7,8,9,10]:
    print(x)

#打印1-10的偶数
for x in [1,2,3,4,5,6,7,8,9,10]:
    if x / 2 = 0:
        print(x)
