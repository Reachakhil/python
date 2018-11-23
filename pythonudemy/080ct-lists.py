# lst=[0,2,-3,4];
# # num1,num2=eval(input("enter two numbers"));
# # print(num1,num2);
# a=[3,4,3,5];
# b=[4,3,5,3,5];
# c=a+b;
# print(c);
# res=[]
# for i in range(0,10):
#     res.append(i);
# print(res);
#
# a=[1,2,3];
# b=a.copy();
# a[0]=5;
# print(a);
# print(b);
#
#
# #-------------
#
#
#
# result=[]
# def copy1( list1 ):
#     for i in list1:
#         result.append(i);
#     return result;
#
# a=[10,20,30];
# b=copy1(a);
# print(f"the copied is {b}");
# #----------------------------
# list=[10,20,30,40,50,60];
# print(list[-5:-3]);
# list[2:2]=['a','b','c'];
# print(list)
# print(list[2]);

#------------------------------------

from random import randrange
def random_list():
    result = []
    count = randrange(0, 10)
    for i in range(count):
        result += [randrange(-50, 50)]
    return result

def selection_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        small = i

        for j in range(i + 1, n):
            if lst[j] < lst[small]:
                small = j
        if i != small:
            lst[i], lst[small] = lst[small], lst[i]
def main():

    for n in range(10):
        col = random_list()
        print(col)
        selection_sort(col)
        print(col)
        print('==============================')
main()

#-------------------------------------------

def locate(lst,seek):
    for i in range(len(lst)):
        if(lst[i]==seek):
            return i;
    return None

def show(lst):

    for item in lst:
        print("%4d" % item, end='')
    print()



def display(lst, value):
    show(lst)
    position = locate(lst, value)
    if position!=None:
        print(f"the element is at {position+1} position")
    else:
        print("(", value, " not in list)", sep='')
    print()

def main():
    a = [100, 44, 2, 80, 5, 13, 11, 2, 110]
    display(a, 13)
    display(a, 2)
    display(a, 7)
    display(a, 100)
    display(a, 110)
main()

#---------------------------------------

def binarysearch(lst,seek):
    first = 0
    last = len(lst) - 1;
    while first <= last:
        mid = first + (last - first + 1) // 2;
        if lst[mid] == seek:
            return mid;
        elif lst[mid] > seek:
            last = mid - 1
        else:
            first = mid + 1;
    return None;
def show(lst):

    for item in lst:
        print("%4d" % item, end='')
    print()

def display(lst, value):
    show(lst)
    position = binarysearch(lst, value)
    if position != None:
        print(position+1);
    else:
        print("(", value, " not in list)", sep='')
    print()

def main():
    a=[2,5,9,19,43,55,88,101,202];
    display(a,22);
    display(a,43);
    display(a,101);
    display(a,55);
    display(a,2);

main()
#--------------------------
list=[13,4,2,4,2,4,2,44,2,4,2]
list=list[::-1];
print(list)

