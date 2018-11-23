list=[1,2,3,4];
list.insert(2,8)
print(list)
#-------------------------
def function_name(name):
    '''
    this is a function to tesr
    :return:
    '''
    return 'the name is' ,name;
x= function_name('akhil');
print(x);

def add1(a,b):
    return a+b;

result= add1(4,5);
print(result);

def check(string):
    if ' dog ' in string:
        return True
    else:
        return False
result=check('my  go  dog waddd');
print(result);

def pig(word):
    first=word[0];
    if(first in 'aeiou'):
        pigword=word+'ay';
        return pigword
    else:
        pigword=word[1:]+'ay';
        return pigword


x=pig('wdwdefe');
print(x);
def func(*args):
    for i in args:
        print(i)
    # return sum(args)
# x=func(4,6,3,2,4,6,3,3)
# print(x);
x=func(2,2,3,2,1,3,2,1)
print(x);

def func(*args,**kwargs):
    print(args)
    print(kwargs)
    print(f"i would like {args[3]} {kwargs['car']}")


func(10, 20, 0, 40, fruit="apple", food="maggi", car="benz")
