def rep(str):
    return str.replace('a','$');

x=rep('akhilaa');
print(x)

#--------------
def rem(str):

    str1=str[len(str)-1]
    return str1


x=rem('akhila$',);
print(x);

def repfirstlast(str):
    return str[-1]+str[1:-1]+str[0]
x=repfirstlast('akhil')
print(x)
#---------------------------
def vow(str):
    c=0;
    for i in str:
        if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
            c+=1;
    print(c)

vow('akhileeiffdf');

#---------------------------
    

