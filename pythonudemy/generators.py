def create_cubes(n):
    result=[]
    for i in range(n):
        yield(i**3)
for x in create_cubes(4):
    print (x)

print('---------------fibonnacii')

def fib(n):
    a=1
    b=1
    for i in range(n):
        yield a
        a,b=b,a+b
for i in fib(4):
    print(i);

def myfunc():
    for x in range(3):
        yield x

x=myfunc()
print(next(x))
print(next(x))
print(next(x))
print(next(x))


# #swap
#
# def swap(a,b):
#     a,b=b,a
#     return a,b
#
#
# print(swap(5,4))

