# global variable

a = 1
b = 2
c = 3
def myFunction():
    # local variable
    a = 5
    print(a)

    # global variable
    global b
    b = 'global variable changed'
    print(b)

    # accessing global variable
    print(c)

    d = 'this will be deleted'
    del d
    # print(d)

myFunction()
print(a)
print(b)

