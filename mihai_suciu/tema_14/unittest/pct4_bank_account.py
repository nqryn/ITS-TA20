class BankAccount:

    delta_amount = 0
    withdrawal_amount = 0

    def __init__(self, account_holder, account_code, account_balance, account_credit):
        self.account_holder = account_holder
        self.account_code = account_code
        self.account_balance = account_balance
        self.account_credit = account_credit

    def print_account_balance(self):
        print(f"Holder: {self.account_holder}\n"
              f"Account: {self.account_code}\n"
              f"Amount: {self.account_balance} Euros\n"
              f"Credit: {self.account_credit} Euros")
        print("-"*80)

    def make_a_withdrawal(self):
        answer = input("\nDo you want to make a withdrawal? (Y/N)\t")
        while True:
            if answer.upper() == 'Y':
                self.withdrawal_amount = int(input("Please enter the sum:\t"))
                if self.withdrawal_amount <= self.account_balance:
                    self.account_balance -= self.withdrawal_amount
                    print(f"You have withdrawn {self.withdrawal_amount} Euros\n")
                    print("Thank you for using our services! Bye!")
                else:
                    answer = input("\nYou don't have enough money in your account!\n"
                                   "\nDo you want to make a credit? (Y/N)\t")
                    if answer.upper() == 'Y':
                        self.account_credit = abs(self.account_balance - self.withdrawal_amount)
                        print(f"You need a credit of {self.account_credit} Euros")
                        self.make_credit()
                    else:
                        print("\nThank you for using our services! Bye!")
                        break
            else:
                print("\nThank you for using our services! Bye!")
            break

    def make_credit(self):
        print(f"You made a credit of {self.account_credit} Euros")
        self.account_balance += abs(self.account_credit)
        if self.withdrawal_amount <= self.account_balance:
            self.account_balance -= self.withdrawal_amount
            print(f"You have withdrawn {self.withdrawal_amount} Euros\n")
        print("Thank you for using our services! Bye!")
        print("-" * 80)

    def make_a_deposit(self):
        answer = input("\nDo you want to make a deposit? (Y/N)?\t")
        if answer.upper() == 'Y':
            deposit_amount = int(input(f"Enter the sum:\t"))
            self.account_balance += deposit_amount
            print("\nThank you for using our services! Bye!")
            print("-" * 80)
        else:
            print("\nThank you for using our services! Bye!")
            print("-" * 80)
