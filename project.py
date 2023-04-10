class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance


def main():
    account = BankAccount()

    while True:
        print("1. Check balance")
        print("2. Make a deposit")
        print("3. Make a withdrawal")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Current balance: ", account.get_balance())
        elif choice == 2:
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
            print("Deposit successful")
        elif choice == 3:
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
            print("Withdrawal successful")
        elif choice == 4:
            break
        else:
            print("Invalid choice")


if __name__ == '__main__':
    main()
