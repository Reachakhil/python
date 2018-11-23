# about instance variables,encapsulation with private members and getter and setter things!
class Person:
    def __init__(self,fname,lname,email):
        self.fname=fname;
        self.lname=lname;
        self.__email=email; #private member
        self.fullname=fname+ ' '+lname
    def setname(self,fname,lname):
        self.fname=fname;
        self.lname=lname;
    def getname(self):
        return f"my name is {self.fname+' '+self.lname}";
    def showname(self):
        return self.fname;
    def email(self):
        return self.__email

    def update_email(self, new_email):
        self.__email = new_email #we are encapsulating the private email
        #instance variable as  it is private and cannot be accessed from outside

p1=Person('akhil','bh','email.com');
p2=Person('ashok','patel',"hbardwaj.gmail.com");
p1.setname('amit','dhanda');
p1.__email="gmail.com";
p1.update_email('gmail.com')
print(p1.email());
print(p1.fname);
print(p1.getname());
print(p1.showname());
print(p2.fname);
print(p2.getname());
print(p2.showname());


