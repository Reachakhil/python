from random import shuffle
from random import randint
for num in range(2,10,2):
    print(num)

list1=[1,2,5,6,3,4];

print(shuffle(list1));
print(randint(3,56))
print(type(randint))
x=input('enter your name ')
print(x);

mystring='hello'
mylist=[]

mylist=[x for x in mystring];
print(mylist);

mylist1=[x for x in range(2,30) if x%2==0]
print(mylist1)

for x in range(1,100):
    if(x%3==0 and x%5==0):
        print("fizzbuzz");
        continue
    if(x%3==0):
        print("fizz")
    elif(x%5==0):
        print("buzz");
    else:
        print(x);
st = 'Print only the words that start with s in this sentence'
st=st.split();
for x in  st:
    if(x[0]=='s'):
        print(x);
list1 = list(range(0,10,2));
print(list1)

st = 'Print every word in this sentence that has an even number of letters'
st=st.split();  #split all the words in sentence
for x in st:
    if len(x)%2==0:
        print(x);