def addtodict(k,v):
    dic1={};
    dic1.update({k:v});
    return dic1
x=addtodict(1,'akhil');
print(x);

print("---------------");
def concatenate(dict1,dict2):
    dict1.update(dict2);
    return dict1;

x=concatenate({1:'aki',2:'anil'},{3:'amit',4:'dsd'});
print(x);

print("---------------");

def keyss(dict,n):
    x=[]
    for key,value in dict.items():
        if key==n:
            flag=True;
        else:
            flag=False
    return flag


print(keyss({1:'aki',2:'anil'},2));

print("---------------");
def printsum(dict):
    sum=0;
    for i,x in dict.items():
        sum+=x;
    return sum;
print(printsum({1:4,2:55,4:33}));

print("----------------");

def removekey(dict,k):
    del dict[k];
    return dict;
print(removekey({1:4,2:55,3:33},3))
# using dictionry for counters
def frequency(str):
    dict1={'a':0,'k':0,'i':0}
    for i in str:
        if i == 'a':
            dict1['a']+=1
        elif i == 'k':
            dict1['k']+=1;
        elif i == 'i':
            dict1['i'] += 1;
    return dict1;
print(frequency("akkkkkiii"))
##SETS:


print("------------")
def vowels(str):
    c=0;
    s=set("aeiou");
    for i in str:
        if i in s:
            c+=1
    print(c)
vowels("ahilewefdewedfdf");
print("--------------");

def common(x,y):
    l1=[]
    l2=[]

    l1=(set(x) & set(y));  #for only common values in x and y;
    print (l1)
common('akhil','abhikhx');


#----------------------------









