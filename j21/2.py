class BankAccount:
    def __init__(self, account_number, account_owner, password, balance=0):
        self.account_number = account_number
        self.account_owner = account_owner
        self.password = password
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """
        Withdraw money from the account.

        Args:
            amount (int): The amount to withdraw.

        Returns:
            int: The new balance after withdrawal, or "Insufficient funds" if the
            account balance is not enough.
        """
        if type(amount) in [int, float]:
            if amount > 0:
                if self.balance >= amount:
                    self.balance -= amount
                    return f"withdraw successfully new balance : {self.balance}"
                else:
                    return "Insufficient funds"
            else:
                return "amount must be higher than 0"
        else:
            return "invalid amount type"

    def get_balance(self):
        return f"new balance : {self.balance}"
    
    def info(self):
        return f"""
owner : {self.account_owner}
account number : {self.account_number}
balance : {self.balance}
"""


a1 = BankAccount("0987654321", "ali rezaee", 1234)
print(a1.info())
a1.deposit(700)
print(a1.withdraw(500))
print(a1.withdraw(0))
a1.deposit(200)
print(a1.get_balance())
