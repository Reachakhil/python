#largest from the list

def largest(lst):
    maximum=0
    for i in lst:
        if i>maximum:
            maximum=i
        else:
            continue
    return maximum

x=largest([22,3,2,4,5,6,5,6,0.33,22.9])
print(x)

#empty
def empty(lst):
    l=[]
    if not lst:
        print ("empty string")
    else:
        print("not empty");

empty([23,3])

#copying list:
def copyit(lst):
    list1=list(lst)
    return list1
x=copyit([2,34,4,2,2]);
print(x);

#characters with length not greater than n.

def charit(lst,n):
    list1=[]
    for i in lst:
        if len(i)<n:
            list1.append(i)
    return list1
x=charit(['akhil','amberrr','abbyy','assssssbhass',],6)
print(x);

#compare two lists

def comp(lst1,lst2):
    for i in lst1:
        if i in lst2:
            return True
        else:
            return False
x=comp([2,3,4,4,5],[6,8,9])
print(x)

#remove 2nd third fourth

def remove(lst):
    return lst[0:2]+lst[5:]
x=remove(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'])
print(x)

#second largest num in list:

def seclargest(lst):
    lst.sort()
    return lst[-2]

x=seclargest([2,3,4,3,45,553,33,44,55,66])
print(x)

#unique value in list

def unique(lst):
    x=[]
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j]:
                break
            else:
                x.append(lst[i])
    return x
y=unique([4,4,5,6,6])
print(y)

#concatinate

def con(lst,n):
    x=[]
    for j in range(len(lst)):
        for i in range(1,n+1):
            x.append(lst[j]+str(i))
    return x
y=con(['q','p'],5);
print(y)

#common between two lists.

def common(lst1,lst2):
    lst1=set(lst1)
    lst2=set(lst2)
    x=[]
    for i in lst1:
        if i in lst2:
            x.append(i)
    return x
x=common([2,3,4,5,6,3,2],[4,5,8,4,9,5,2,8])
print(x)

#print element at the start of the sublists:

# def addit(lst,n):
#     for i in lst:
#         if i is list:
#             list[i][0]=n
#     return lst
# x=addit([[2,3][3,4],99])
# print(x)









