def ran_check(num,low,high):
    if(num in range(low,high+1)):
        return True;
    else:
        return False;
x=ran_check(4,3,10);
print(x);
#-----------------------
def up_low(s):
    up=0;
    low=0;
    for i in s:
        if i.isupper():
            up+=1;
        elif i.islower():
            low+=1;
    print(low,up);

up_low('hello Theere MY')
#--------------------------
def unique_list(list):
    newlist=[];
    for i in list:
        print(i);
        if i in newlist:
            continue;
        else:
            newlist.append(i)
    return newlist;
x=unique_list([2,3,4,3,2,3,3,2,2,3]);
print(x);

#---------------------------------
def multiply(numbers):
    res=1;
    for i in numbers:
        res*=i;
    return res;
x=multiply([1,2,3,1]);
print(x);
#-----------------------
def palindrome(s):
    srev=s[::-1];
    if srev==s:
        return True;
    else:
        return False;

x=palindrome('hellehohh');
print(x);
#----------------
num =6;
r=1;
for i in range(1,num+1):
    r*=i;
print(r);

