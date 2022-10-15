class Category:
    
    def __init__(self,category):
        self.category=category
        self.l=[]
    
    def __str__(self):
        s = self.category.center(50, "*") + "\n"
        for item in self.l:
            temp = f"{item['description'][:40]:40}{item['amount']:7.2f}"
            s += temp + "\n"
        s += "Total: " + str(self.get_balance())
        return s
    
    def deposit(self,amount,description=""):
        t={}
        t['amount']=amount
        t['description']=description
        self.l.append(t)
        
    def withdraw(self,amount,description=""):
        if (self.check_funds(amount)):
            t={}
            t['amount']=0-amount
            t['description']=description
            self.l.append(t)
            return True
        return False    
        
    def get_balance(self):
        balance=0 
        for i in self.l:
            balance=balance+i['amount']
        return balance    
    
    def transfer(self,amount,cate):
        if(self.check_funds(amount)):
            self.withdraw(amount,"Transfer to "+cate.category)
            cate.deposit(amount,"Transferred from "+self.category)
            return True
        return False    
        
    def check_funds(self,amount):
        if amount>self.get_balance():
            return False
        return True    
        
if __name__=="__main__":
    food = Category("Food")
    food.deposit(1000, "Initial deposit")
    food.withdraw(10.15, "Groceries")
    food.withdraw(15.89, "Restaurant and more food for dessert")
    
    clothing = Category("Clothing")
    food.transfer(50, clothing)
    clothing.withdraw(25.55)
    clothing.withdraw(100)
    vehicle = Category("Car")
    vehicle.deposit(1000, "Initial deposit")
    vehicle.withdraw(110,"Diesel")
    vehicle.withdraw(250, "Traffic challan")
    print(food)
    print()
    print(clothing)
    print()
    print(vehicle)
    print()
    print("********************Balance********************")
    print('Food balance:',food.get_balance())
    print('Clothing balance:',clothing.get_balance())
    print('Car balance:',vehicle.get_balance())
