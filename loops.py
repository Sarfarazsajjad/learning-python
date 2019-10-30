class MyClass:
    pass

a = MyClass()
a.x = 1
a.y = 2

b = MyClass()
b.x = 3
b.y = 4

c = MyClass()
c.x = 5
c.y = 6

list = [a,b,c]

# iterate with elements
for item in list:
    print(item.x,item.y)

# iterate with elements and iteration index
for index,item in enumerate(list):
    print(index,item.x,item.y)