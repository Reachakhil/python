# lesser_of_two_evens(2,4) --> 2
# lesser_of_two_evens(2,5) --> 5

def lesser_of_two(a,b):
    if(a%2==0 and b%2==0):
        return min(a,b)
    else:
        return max(a,b)

x=lesser_of_two(9,7)
print(x);
#---------------------------
def animal_crackers(text):
    text=text.split();
    y=text[0][0]
    z=text[1][0]
    if y ==z:
        return True
    else:
        return False
x=animal_crackers('akhil ahardwaj');
print(x);
#-------------------------------

def makes_twenty(n1,n2):
    if(n1==20 or n2==20):
        return True
    elif(n1+n2 >=20):
        return True
    else:
        return False
x=makes_twenty(0,20)
print(x)

#----------------------------
def old_macdonald(name):

    x=name[0].upper();
    name=x+name[1:3]+name[3].upper()+name[4:];
    return name

z=old_macdonald('macdonalds');
print(z);
#-------------------------------------
def master_yoda(text):
    x=text.split();
    x=x[::-1]; #for reversing a list
    y= ' '.join(x);
    return y;

x=master_yoda('akhil is name my');
print(x);
#---------------------------------
def almost_there(n):
    if(n>190 and n<210):
        return True
    else:
        return False
x=almost_there(140);
print(x);
# #------------------------------------
def has_33(nums):
    for i in range(0,len(nums)-1):
        if(nums[i]==3 and nums[i+1]==3):
            print('true');
            break;
    else:
        print('false')
has_33([8,3,4,3,3])
# print("def has__33:",x);
#-----------------------------
def paper_doll(text):
    k='';
    for i in range(0,len(text)-1):
        k+=text[i]*3;
    print(k);

paper_doll('misissippi');
#------------------------------
def blackjack(a,b,c):
    if a >11 or a<1 or b>11 or b<1 or c>11 or c<1:
        print('give correct input');
    elif (a+b+c >21 and (a==11 or b==11 or c==11)):
        print((a+b+c)-10);
    elif (a+b+c <=21):
        print(a+b+c);
    else:
        print('BUST');
blackjack(8,9,5);
#-----------------------
def spy_game(nums):
    code=[0,0,7,1];
    for num in nums:
        if(num == code[0]):
            code.pop(0);
    if(len(code)==1):
        return True;
    else:
        return False;
x=spy_game([9,3,4,5,2,0,7,4]);
print(x);
#------------------
def count_primes(num):
    