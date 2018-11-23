# x=[1,2,3,4];
# print(2 in x);
#
# x=[0,1,[2]];
# x[2][0]=3;
# x[2].append(4);
# print(x);
# #----------------------

# def sums(lst):
#     result=[];
#     for i in lst:
#         result.append(i);
#     x="".join(result);
#     return x;
# x=sums(['akhil','bhardwaj']);
# print(x);
#------------------------------
# def factorial(n):
#     res=1;
#     for i in range(1,n+1):
#         res*=i;
#     return res;
#
# x=factorial(6);
# print(x);
#-------------------------------

# def reverse(lst):
#     rev=[]
#     k=1
#     list=lst[::-1];
#     for i in list:
#         rev.append(i)
#     return rev;
# x=reverse([3,4,5,6,7]);
# print(x);

#-----------------------

# def unique(lst):
#     new=[]
#     for i in lst:
#         if i in new:
#             continue;
#         else:
#             new.append(i);
#     return new;
# x=unique([2,2,3,4,2,4,5,4,5,6,9]);
# print(x);
#------------------------------
def unique(lst):
    new=[]
    for i in lst:
        if i not in (new):
            new.append(i);
    return new;
x=unique([2,2,3,4,2,4,5,4,5,6,9]);
print(x);

#---------------------------------

def lensort(lst):
    new=[];
    for i in lst:
        new.append(len(i));
    return new;
x=lensort(['sddsd','dsddddsd','d']);
y=sorted(x);
print(y);





