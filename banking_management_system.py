# Banking Management System

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.balance = 0
        self.loan = 0
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append('Deposit amount: {} tk.'.format(amount))
        print('Deposit successful. Current balance: {} tk.'.format(self.balance))

    def withdrawal(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append('Withdrawal amount: {} tk.'.format(amount))
            print('Withdrawal successful. Current balance: {} tk.'.format(self.balance))
        else:
            print('Insufficient Balance! Withdrawal is not possible.')

    def transfer(self, amount, another_account):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append('Transfer amount: {} tk. to Mr. {}'.format(amount, another_account.name))
            another_account.balance += amount
            another_account.transactions.append('Transfer amount: {} tk. from Mr. {}'.format(amount, self.name))
            print('Transfer successful. Current balance: {} tk.'.format(self.balance))
        else:
            print('Insufficient funds. Transfer is not possible.')

    def check_balance(self):
        print('Current balance: {} tk.'.format(self.balance))

    def view_transactions(self):
        print('\n ==== Transaction history ====')
        for transaction in self.transactions:
            print(transaction)

    def take_loan(self):
        if self.balance > 0 and self.loan == 0:
            loan_amount = self.balance * 2
            self.balance += loan_amount
            self.loan = loan_amount
            self.transactions.append('Loan amount: {} tk.'.format(loan_amount))
            print(f'loan amount is {loan_amount} tk.')
            print('Loan received. Current balance: {} tk.'.format(self.balance))
        
        else:
            print('you are not eligible to get loan untill you repay the current loan')

    def repayment_loan(self):
        if self.loan > 0:
            print('Current Loan Amount: {} tk.'.format(self.loan))
            repayment_amount = int(input('Enter the repayment amount: '))
            if repayment_amount <= self.balance:
                self.balance -= repayment_amount
                self.loan -= repayment_amount
                self.transactions.append('Loan repayment amount: {} tk.'.format(repayment_amount))
                print(f'repayment amount is {repayment_amount} tk.')
                print('Loan repayment successful. Current balance: {} tk.'.format(self.balance))
                if self.loan == 0:
                    print('Loan fully repaid.')
            else:
                print('Insufficient balance. Repayment is not possible.')
        else:
            print('You have no loan to repay.')


class Admin(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.loan_feature_enabled = True

    def check_total_balance(self, clients):
        total_balance = sum(client.balance for client in clients)
        print('Total available balance in the bank: {} tk.'.format(total_balance))


    def check_total_loan_amount(self, clients):
        total_loans = sum(client.loan for client in clients)
        print('Total loan amount in the bank: {} tk.'.format(total_loans))


    def loan_feature(self):
        self.loan_feature_enabled = not self.loan_feature_enabled
        if self.loan_feature_enabled:
            print('Loan feature is available now-a-days.')
        else:
            print('Loan feature is not available now-a-days.')


if __name__ == '__main__':
    # Create client accounts
    number_of_clients = int(input('Enter the number of clients: '))
    clients = []

    for i in range(number_of_clients):
        name = input('Enter the name of client {}: '.format(i+1))
        email = input('Enter the email of client {}: '.format(i+1))
        password = input('Enter the password of client {}: '.format(i+1))
        client = User(name, email, password)
        clients.append(client)

    # Create admin account
    admin_name = input('Enter the name of admin: ')
    admin_email = input('Enter the email of admin: ')
    admin_password = input('Enter the password of admin: ')
    admin = Admin(admin_name, admin_email, admin_password)

    # options
    while True:
        print('\n ==== Bank Menu ====')
        print('1 => Client Login')
        print('2 => Admin Login')
        print('3 => Exit')
        choice = input('Enter your choice (1-3): ')

        if choice == '1':
            # Client Login Part:
            email = input('Enter your email: ')
            password = input('Enter your password: ')
            client_log_in = None
            for client in clients:
                if client.email == email and client.password == password:
                    client_log_in = client
                    break

            if client_log_in is not None:
                print('\n ==== Welcome, {}! ===='.format(client_log_in.name))
                while True:
                    print('\n ==== Client Menu ====')
                    print('1 => Deposit Amount')
                    print('2 => Withdrawal Amount')
                    print('3 => Transfer to Another Account')
                    print('4 => Check Available Balance')
                    print('5 => View Transactions History')
                    print('6 => Take Loan')
                    print('7 => Repayment Loan')
                    print('8 => Logout')
                    client_choice = input('Enter your choice (1-8): ')

                    if client_choice == '1':
                        amount = int(input('Enter the deposit amount: '))
                        client_log_in.deposit(amount)
                    elif client_choice == '2':
                        amount = int(input('Enter the withdrawal amount: '))
                        client_log_in.withdrawal(amount)
                    elif client_choice == '3':
                        another_account_email = input('Enter the another_account\'s email: ')
                        amount = int(input('Enter the transfer amount: '))
                        another_account = None
                        for client in clients:
                            if client.email == another_account_email:
                                another_account = client
                                break
                        if another_account is not None:
                            client_log_in.transfer(amount, another_account)
                        else:
                            print('Provided email is not found in our server.')
                    elif client_choice == '4':
                        client_log_in.check_balance()
                    elif client_choice == '5':
                        client_log_in.view_transactions()
                    elif client_choice == '6':
                        client_log_in.take_loan()
                    elif client_choice == '7':
                        client_log_in.repayment_loan()
                    elif client_choice == '8':
                        print('Log out')
                        break
                    else:
                        print('Invalid choice. You must put a number in between 1-8.')

            else:
                print('Invalid email or password. Please try again.')

        elif choice == '2':
            # Admin Login Part
            email = input('Enter your email: ')
            password = input('Enter your password: ')

            if admin.email == email and admin.password == password:
                print('\n ==== Welcome, {}! ===='.format(admin.name))
                while True:
                    print('\n ==== Admin Menu ====')
                    print('1 => Check Total Available Balance')
                    print('2 => Check Total Loan Amount')
                    print('3 => Loan Feature')
                    print('4 => Logout')
                    admin_choice = input('Enter your choice (1-4): ')

                    if admin_choice == '1':
                        admin.check_total_balance(clients)
                    elif admin_choice == '2':
                        admin.check_total_loan_amount(clients)
                    elif admin_choice == '3':
                        admin.loan_feature()
                    elif admin_choice == '4':
                        print('Log out')
                        break
                    else:
                        print('Invalid choice. You must put a number in between 1-4.')

            else:
                print('Invalid email or password. Please try again.')

        elif choice == '3':
            print('Exit')
            break

        else:
            print('Invalid choice. You must put a number in between 1-3.')
