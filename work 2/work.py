#10. 将一个列表的数据复制到另一个列表中。
alst = [1,2,3]
blst = [55," "]
#alst.append(blst)  [1, 2, 3, [55, ' ']]
alst.extend(blst)#[1, 2, 3, 55, ' ']
print(alst)

#11. 输出 9*9 乘法口诀表。*********
"""
1.有两个数 x，y
2.for


"""
for x in range(1,10):
    for y in range(1,x+1):
        print(y,' * ',x,' = ',x * y, end=' ') #end 为了不让他换行
    print()
#12. 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

astr = "bcuysvg bvue %%%bu81"
yw = 0
kg = 0
sz = 0
other = 0
for x in astr:
    if x.isalpha():
        yw +=1
    elif x.isspace():
        kg +=1
    elif x.isnumeric():
        sz +=1
    else:
        other+=1
print("英文字母：",yw)
print("空格：",kg)
print("数字：",sz)
print("其他字符：",other)

#13. 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
d = int(input ("请输入几位数："))
a= int(input("请输入a的值："))
s =0
aa = 0
for i in range(1,d+1,1):
    aa += a * 10**(i-1)
    s += aa
print(s)


#14. 题目：打印出如下图案（菱形）:"""

"""a = "*"
for x in range(1,9,2):
    print(a * x)
"""
str1 = '*'
b = input("请输入行数：")
x = 2*int(b)
y = 2*int(b) -1
print(x)
a = range(1,x,2)
for i in a:
    print((str1 * i).center(y))
for i in reversed(a):
    print((str1 * i).center(y))
