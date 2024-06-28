class BankAccount :
    def __init__(self,balance) :
        self.balance=balance

    def  withdraw(self,money):
        message=""
        if self.balance>0 and self.balance>= money:
            self.balance-=money
            message=f"you withdrew {money} succesfully \nyor balance is {self.balance}"

            
        else :
            message=f"you dont have enough money "
        return message  

    def add(self,money):
        message=""
        if money>0:
            self.balance+=money
            message=f"you added {money} succesfully\nyor balance is {self.balance} "
            
        else :
            message=f"invalid amount "
        return message 

 