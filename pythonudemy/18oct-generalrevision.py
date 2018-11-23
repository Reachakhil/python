a=0
b=1
c=a+b
for i in range(3,19):
    c=a+b
    a=b
    b=c
    print(c)

def fact(n):
    sum=1;
    for i in range(n):
        sum*=n;
    print(sum);
fact(3);
print("------")

def numtobinary(n):
    l= []
    while n>0:
        x=n%2;
        l.append(x)
        n=n//2
        reversed(l)
    return l
x=numtobinary(3);
for i in x:

    print(i,end=" ")

print("---------------");









