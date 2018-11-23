mylist=[1,2,3,4,5,6,7,8,9,10]
for x in mylist:
    if(x%2==0):
        print(x)
    else:
        #print('this is odd:',x)
        print(f'this is odd{x}')
sum=0;
for x in mylist:
    sum+=x;
print("and",sum,"the sum is:",sum);

for x in 'hello world':
    print(x)
list=(1,2,3,4,5)
for x in list:
    print(x)
mylist=[(1,2),(3,4),(5,6),(7,8)]

for (x,y) in mylist:
    print(x)
    print(y)

l={'k1':'akhil','k2':'tony'}
for (a,b) in l.items():
    print(b )
    #------------------
x=0;
while x<10:
    print("x values are ",x);
    x=x+1;
list='akhil bhardwaj'

for x in list:
    if x== 'a':
        continue
    print(x);