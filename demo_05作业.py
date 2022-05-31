#1. 输入a,b,c,d4个整数，计算a+b-c*d的结果
a =20
b=30
c = 0
d =3
e=a+b-c*d
print(e)
#2. 打印1~100内被3整除的所有数的和 。*******
sum = 0
for f in range(1,101,1):
    if f % 3 == 0:
        sum += f
print(sum)

#3. 使用range()输出1~10内的所有奇数 。
for x in range(1,11,2):
    print(x)
#4. 打印1~100所有偶数的和 减去 所有奇数的和 的值
sum1=0
sum2=0
for x in range(1,101):
    if x % 2==0:
        sum1 += x
    else:sum2+=x
    x+=1
print('4:',sum1-sum2)
#5. 求1+2+3+...+100的和
i =1
sum = 0
while i <=100:
    i+=1
    sum+=i
print(sum)
#6. 判断一个数n能同时被3和5整除

for x in range(1,101,1):
    if x % 3==0 and x%5==0:
        print('6:',x)
#7. 定义一个整数变量，判断该变量值是否是1-100内的某个数，如果是打印出来
i =input("请输入一个整数：")
if 0 < int(i) <=100:
    print(i)
#8. 输入三个整数x,y,z，请把这三个数由小到大输出。备注：输入方法：input()

"""x,y,z = input("请输入三个整数：")
if x>y:
    print(y)
    if x>z and z>y:
        print(y)
    else:
        print(z)
else:print(x)
"""
lst = []
x = input("请输入一个整数：")
y = input("请输入一个整数：")
z = input("请输入一个整数：")
lst.append(x)
lst.append(y)
lst.append(z)
lst.sort()
print(lst)
#9. 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。备注：需要使用input()方法
score = input("输入成绩：")
if int(score) >=90:
    print("A")
elif 60<=int(score)<=89:
    print("B")
else:
    print("C")















