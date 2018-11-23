def square(num):
    return num**2;
my_nums=[1,2,3,4];

for item in map(square,my_nums):
    print(item);
def even1(num):
    if num%2==0:
        return True;

x=list(filter(lambda num: num%2==0,my_nums))
print(x);

#--------------------------
square= lambda num: num**2

print(square(4));