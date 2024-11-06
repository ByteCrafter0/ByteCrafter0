class Account:
    #At first initialize the initial amount
    def __init__(self, initial_amount=100):
        self.Amount = initial_amount
    
    #We create the function which helps to the deposite related function
    def deposit(self, amount):
        self.Amount += amount
        print(f"Amount Rs. {amount} has been credited to your account.")
        print(f"Now the total Balance is Rs {self.Amount}")
    #In this funtion help to to do Withdraw related function
    def withdraw(self, amount_to_debit):
        if amount_to_debit > self.Amount:
            print("Insufficient balance.")
        else:
            self.Amount -= amount_to_debit
            print(f"Amount Rs. {amount_to_debit} has been debited from your account.")
            print(f"Remaining Balance is Rs {self.Amount}")

# chaking it work or not
account = Account()
account.deposit(100)
account.withdraw(90)