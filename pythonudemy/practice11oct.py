def sol(lst):
    return (lst[0],lst[-1]);
y=[]
y=sol([5,10,15,20,25]);
print(y);

#---------------------------

first=0
second=1
third=first+second;
for i in range(2,11):
    print(first);
    third=first+second;
    first=second;
    second=third;

def norepeat(lst):
    x=set(lst)
    return x;
x=norepeat([1,2,2,3,3,4,4,3,2,4,9,4,99]);
print(x);

#-----------------------------------
x="my name is akhil";
s=x.split();
print(s);
s=s[::-1];
print(s);
print(" ".join(s));

#--------------------------------------
def search(lst,x):
    flag=True;
    for i in range(len(lst)):
        if (lst[i] == x):
            flag=True;
            pos=i+1
            break;
        else:
            flag=False;
    return flag,pos
x=search([2,3,3,4,2,8,4,2,44],2)
print(x)


