class Bank:
    def __init__(self):
        self.amount = 0.0

    def deposit(self):
        deposit_amount = float(input("Enter amount to deposit: "))
        self.amount += deposit_amount
        print(f"Deposited: {deposit_amount}")

    def withdraw(self):
        withdraw_amount = float(input("Enter amount to withdraw: "))
        if withdraw_amount <= self.amount:
            self.amount -= withdraw_amount
            print(f"Withdraw: {withdraw_amount}")
        else:
            print("Insufficient balance")

    def display_balance(self):
        print(f"Current balance: {self.amount}")
b1 = Bank()
b1.deposit()
b1.withdraw()
b1.display_balance()
