#args used

def add(*args):
    sum=0
    for i in args:
        sum+=i;
    return sum
x=add(2,4,3,2,8,4,3)
print(x);

#kargs used

def lists(**kargs):
    print("details are:")
    for k,v in kargs.items():
        print (f" {k}: {v}")
lists(firstname = "akhil",lastname="amber",age=21,phonenumber=99999)

