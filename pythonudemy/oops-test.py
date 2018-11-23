class Account():
    def __init__(self,owner,balance):
        self.owner=owner;
        self.balance=balance;
    def deposit(self,money):
        if(money==0):
            print("amount can not be zero");
        else:
            print('Amount Added Succesfully');
            self.balance+=money;

    def withdraw(self,money):
        if(money>self.balance):
            print("not enough balance");
        else:
            print("money withdraw succesfull");
            self.balance-=money;

    def __str__(self):
        return f"name is {self.owner} and balance is {self.balance}";

akhil=Account('akhil',5000);
print(akhil);
akhil.deposit(4000);
print(akhil);
akhil.withdraw(6000)
print(akhil);
akhil.withdraw(11000)
