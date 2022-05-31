
# 序列的通用操作

#索引：seq[index]-以列表、元祖、字符串  index代表下标，默认从0开始

lst = ['red', 10, 12.3," "]
print("第一个元素:",lst[-1])

tuple = ('red', 10, 12.3," ")
print(tuple[0])

str = "jhdgdb"
print(str[-1])

#切片:lst[start:end:step] 不包括end的那个数
lst5 = ['red','green','blue','black','gold','orange']
print("获取第2-5个元素:",lst5[1:5])
print("获取第2,4,6个元素:",lst5[1:6:2])

tuple = ('red', 10, 12.3," ")
print("获取第2-5个元素:",tuple[1:3])

str = "jhdgdb"
print("获取第2-5个元素:",str[1:3])

print("获取第1,3,5个元素:",lst5[::2]) #lst5[0:6:2] 省略start和end
print("获取第3个及后面的元素:",lst5[2:])# lst5[2:6:1]
print("将列表翻转：",lst5[::-1]) #
print(lst5[:3:])
print("将列表翻转：",lst5[6:0:-1])#*******

# 列表中有10个元素，取出奇数个的元素
print(lst[::2])

# 序列的相加和相乘
a_list = ['abc']
b_list = ['xyz']
c_list = a_list + b_list
print("两个列表相加后产生的新列表:",c_list)
print("列表a_list乘3后产生的新列表:",a_list*3)


dlst = [None] * 3
print(dlst)

print("=="*20)


# 检查元素:in,针对列表、字符串、元祖

lst = ['red', 'yellow', 'cream', 'blue', 'gunmetal']

print('red'in lst)
print('gunmeta'in lst)

a =len(lst)
print(a)

#序列支持的方法：list()
print("="*20)
klst =list()
print(list())

cstr = "abc"
print(list(cstr))



#循环序列中的索引和值
for index,vls in enumerate(lst):
    print(index,vls)

print(max(lst))

#题 ：将后面的字符串转化为12345“[1,2,3,4,5]” ==> 12345

str = "[1,2,3,4,5]"
print(str)
print(str[1:10:2])

#列表推导式:[ 3.表达式 1.循环体 2.表达式 ]

#生成0~10的列表：
lst =[]
for x in range(1,11):
    lst.append(x)
print(lst)

lst1 = [x for x in range(1,11)]
print(lst1)

#生成0~10的列表，只打印奇数
lst2 = [x for x in range(1,11,2)]
print(lst2)

lst2 = [x for x in range(1,11,2) if x%2!=0]
print(lst2)

#生成0~10的列表，只打印奇数,生成的奇数加上10
lst2 = [x+10 for x in range(1,11,2)]
print(lst2)

print([y for y in range(1, 11) if y % 2])


