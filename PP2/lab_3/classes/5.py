class Account:
    def __init__(self, owner, balance):
        """
        Initialize a new Account instance.
        
        Parameters:
            owner (str): The name of the account owner.
            balance (float): The starting balance for the account.
        """
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """
        Deposits the given amount into the account.
        
        Parameters:
            amount (float): The amount to deposit.
        """
        if amount > 0:
            self.balance += amount
            print(f"Deposit accepted. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraws the given amount from the account if sufficient funds exist.
        
        Parameters:
            amount (float): The amount to withdraw.
        """
        if amount > self.balance:
            print("Insufficient funds! Withdrawal not allowed.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrawal accepted. New balance: {self.balance}")

# Example usage:
# Create an account with an initial balance
acc = Account("John Doe", 100)
print(f"Account owner: {acc.owner}")
print(f"Initial balance: {acc.balance}")

# Make several deposits and withdrawals.
acc.deposit(50)         # Should increase the balance to 150
acc.withdraw(75)        # Should decrease the balance to 75
acc.withdraw(150)       # Should print an error message (insufficient funds)
acc.deposit(20)         # Should increase the balance to 95

# Final account status
print(f"Final balance: {acc.balance}")
