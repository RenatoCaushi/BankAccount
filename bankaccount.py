class BankAccount:

    def __init__(self,name, int_rate, balance): 
      self.name = name
      self.int_rate = int_rate
      self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self
        
    def withdraw(self, amount):
        if (self.balance>=amount):
            self.balance -= amount
        else:
            print("Insuficient funds, charging $5")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print(f"User:{self.name} has this balance:${self.balance} ")

    def yield_interest(self):
        self.balance=self.balance+self.balance*self.int_rate
        return self


Renato=BankAccount("Renato",0.02,0)
Renato.display_account_info()
Renato.deposit(10).deposit(30)
Renato.display_account_info()
Renato.withdraw(2)
Renato.display_account_info()
Renato.withdraw(12)
Renato.display_account_info()
Renato.yield_interest()
Renato.display_account_info()

print("///////////////////////////")

Klea=BankAccount("Klea",0.02,0)
Klea.display_account_info()
Klea.deposit(10)
Klea.display_account_info()
Klea.withdraw(2)
Klea.display_account_info()
Klea.withdraw(12)
Klea.display_account_info()
Klea.yield_interest()
Klea.display_account_info()



