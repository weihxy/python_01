try:
    f = open("b.txt",'r')
    contents = f.readlines()
    for x in contents:
        print(2/0)
except Exception as e:
    print(e)
finally:
    f.close()


