class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age =  age
        self.gender = gender

    def show_Details(self):
        print('User details \n\n Name : {} \n Age : {} \n Gender : {}'.
        format(self.name,self.age,self.gender))


class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance = 0

    def deposit(self,amount):
        self.balance = self.balance + amount
        print('Deposited \nUpdated balance : ',self.balance)
    def withdraw(self,amount):
        if amount > self.balance:
            print('Insufficiant funds \nAvailable balance :',self.balance)
        else:
            self.balance = self.balance - amount
            print('Withdrawn \nUpdated balance :',self.balance)
    def show_balance(self):
        print('Available balance :',self.balance)
        




harshith = Bank('Harshith', 23,'Male')
harshith.show_Details()
harshith.deposit(500)
harshith.show_balance()
harshith.withdraw(600)
harshith.withdraw(400)
harshith.show_balance()


