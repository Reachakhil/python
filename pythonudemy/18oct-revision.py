
from  random import *
def largest(lst):
    lst1=[]
    lst.sort()
    l=len(lst1);
    return lst[l-1];

x=largest([35,33,22,44])
print(x)
#-----------------------
def evenodd(lst):
    evn=[]
    odd=[]
    for i in lst:
        if i%2==0:
            evn.append(i);
        else:
            odd.append(i);
    return (evn,odd)
x=evenodd([3,4,2,5,38,4,5,3,99])
print(x);
#----------------------------------

def mergelist(lst1,lst2):
    return lst1+lst2
x=mergelist([12,3,2,3],[23,3,2,4,5]);
print(x);

#-----------------------------------
def bubblesort(lst):
    for i in range(0,len(lst)-1):
        for x in range(0,len(lst)-i-1):
            if lst[x] > lst[x+1]:
                lst[x],lst[x+1]=lst[x+1],lst[x]
    return lst
x=bubblesort([3,4,5,32,4,2,11])
print(x)
#------------------
def intersection(lst1,lst2):
    lst3=[];
    c=0;
    for i in set(lst1):
        for x in set(lst2):
            if i == x:
                lst3.append(i)
                continue;
    return lst3
x=intersection([2,3,4,5,5],[3,423,4,5,3,2,4]);
print(x);
#-------------------------------
print("-------------")
def tup(n):
    l1=[]
    l2=[]
    for i in range(n):
        l1.append(i)
        l2.append(i*i)

    return (l1,l2)
x=tup(4);
print(x)

#-----------------

def ra(n):
    l=[]
    for i in range(n):
        l.append(randint(1, 20));
    return l
x=ra(7);
print(x)
#-----------------------------
def wordlen(lst):
    max1=len(lst[0])
    for i in lst:
        if len(i)>max1:
            maximum=i
    return maximum



x=wordlen(['aakss','dsdsd','dsdsds','sdddddddd']);

print(x)
#-------------------------





