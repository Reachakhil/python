print("string-----------")
#index
#in
#join
#split
#replace
lista=["2","3","4","2"," is my number"];
x="".join(lista);
print(x)

str='my name is akhil';
lst=str.split();
print(lst);

str="hello kick"
str=str.replace("k","n")
print(str)
age=22
print(f"my age is :{age}")

print("functions----------")

def myfunction(a,b):

    '''
    (hello this function is used to add 2 numbers )
    '''
    return a+b

result=myfunction(4,5)
print(result)

print("lists-------------")
companies = ["hackerearth", "google", "facebook", ["tcs", "infosys"]]
print(companies[3][0])

companies1=[]
companies1.append("tcs");
print(companies1)
del companies1[0]
print(companies1)

print("dict-------------")

#dictmethods
#get (get with the keys name
#update
#del element
#.has_key (gives true or false

dict={1:'akhil',2:"amber"}
print(dict.get(1))
print(dict[1])
dict[3]="ashok"

dict1={4:'abdu'}
dict.pop(1)
dict.update(dict1);
for k,v in dict.items():
    print(f"key is {k} and value is {v}")

print("sets---------------")
#Sets are commonly used for membership testing,
#  removing duplicates entries,
# and also for operations such as intersection, union, and set difference.

#creating set
#add element to set using #add
#update
#remove
#copy of set
#set operations ( &,| , - )
x=set()
x="hellohello"
x=set(x)
x.add('y')
print(x)

y=x.copy()
print(y)
print("classes----------")
class Snake:
    name="python"
    def __init__(self,name):
        self.name=name;
    def changename(self,NewName):
        self.name=NewName


snake=Snake('cobra')

print(snake.name)
snake.changename('anaconda')
print(snake.name)
print("inheritennce----")

class Rocket:
    def __init__(self,name,distance):
        self.name=name
        self.distance=distance
    def launch(self):
        return f"{self.name} has reached at distance {self.distance}"

class MarsRover(Rocket):
    def __init__(self,name,distance,maker):
        Rocket.__init__(self,name,distance)
        self.maker=maker
    def makername(self):
        return f"{self.name} launched by {self.maker}"

x=Rocket('ISRO',2000)

print(x.launch())
y=MarsRover('isro',1000,'reliance')
print(y.makername())
import random

x=[7,8,9,33]
print(random.choice(x))











