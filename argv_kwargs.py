#  variable length arguments

def myFun1(*argv):
    for arg in argv:
        print(arg, end=" ")

def myFun2(**kwargs):
 for key, value in kwargs.items():
     print("%s : %s"%(key,value))

myFun1("Hello", 'Welcome', 'to', 'Pyrack')
print()

myFun2(first = 'Py', mid = 'rack', last = 'Pune')

