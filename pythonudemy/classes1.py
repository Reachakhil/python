class Animal():
    def _init_(self):
        print("animal created");
    def who_ami(self):
        print('i am human being');

#inherited class
class Sample(Animal):
    country='india'
    def __init__(self,color,age,name):
        Animal._init_(self);
        self.color=color;
        self.age=age
        self.name=name;
    def tell(self,place):
        print(f'welcome to my profile,myself {self.name} at {place}')

    def __str__(self): #special methods ,
        return f"{self.name} of {self.age} lives in {self.country}"

    def __len__(self):
         return self.age;

    # def __del__(self):
    #     print('book object is deleted');
#-----------------------------------------
# object instance
my_sample=Sample('red',33,'akhil');
print(my_sample.color,my_sample.age,my_sample.name,my_sample.country);

my_sample.tell('india');

print(my_sample.who_ami());
print(my_sample);
print(len(my_sample))

#assingment------------------

class Cylinder():
    pi = 3.14;
    def __init__(self, height, radius):
        self.height=height;
        self.radius=radius;

    def volume(self):
        return self.height*self.pi*self.radius**2

    def surface_area(self):
        pass

c = Cylinder(2,3)
print(c.volume());
