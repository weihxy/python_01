# 字符串方法演示

#1.字符串分割 ： join(seq)
astr = ' '
bstr = astr.join('world')
print(bstr)

#2.截取字符串 ： split(str = "")
cstr = "hello world"
dstr = cstr.split(" ")
print(dstr)

cstr = "hello world"
dstr = cstr.split("o")
print(dstr)

# 查找字符串 ：find(substr)，如果找到了返回的是最小索引，没有找到返回-1
print(cstr.find("l"))
print(cstr.index("l"))

# 查找以xxx结尾的字符串 ：endswith('xxx')
fstr = "测试报告.doc"
if fstr.endswith(".doc"):
    print(fstr)

# 替换字符串 ：
gstr = "hh"
hstr = gstr.replace("hh",'lala')
print(hstr)













