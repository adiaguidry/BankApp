from os import system
from random import *


# create a person class with firstname and lastname
class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname


# create a Customer(Person) account_number and balance
class Customer(Person):
    def __init__(self, firstname, lastname, account_number, balance):
        super().__init__(firstname, lastname)
        self.account_number = account_number
        self.balance = balance

    def client_info(self):
        print(f'name: {self.firstname} {self.lastname}\n'
              f'account number: {self.account_number}\n'
              f'account balance: {self.balance}')
    def __str__(self):
        return
# methods deposit() how much money to add / withdraw() how much to take out
    def deposit(self):
        amount = ' '
        while not amount.replace(',', '').replace('.', '').isdigit():
            amount = input('Enter amount you like to deposit (20.00): ')
        amount = float(amount.replace(',', ''))
        if isinstance(amount, float):
            self.balance += round(amount, 2)
        print(f'Your new balance is ${"{:,.2f}".format(self.balance)}\n'
              f'${"{:,.2f}".format(amount)} was deposited')

    def withdraw(self):
        amount = ' '
        while not amount.replace(',', '').replace('.', '').isdigit():
            amount = input('Enter amount you like to withdraw (20.00): ')
        amount = float(amount.replace(',', ''))
        if isinstance(amount, float):
            if round(amount, 2) > self.balance:
                print('Sorry that withdraw will put you in the negative!!\n'
                      f'your balance is ${"{:,.2f}".format(self.balance)}')
            else:
                self.balance -= round(amount, 2)
                print(f'Your new balance is ${"{:,.2f}".format(self.balance)}\n'
                      f'${"{:,.2f}".format(amount)} was withdrawn')


def create_customer():
    firstname = input('Enter your first name: ')
    lastname = input('Enter your last name: ')
    account_number = randint(1000, 5000)
    balance = float(input('Enter your balance: ').replace(',', ''))
    customer = Customer(firstname, lastname, account_number, balance)
    return customer


def start():
    customer = create_customer()
    service = '0'
    while service != '4' and service.isdigit():
        service = (input('Welcome please select from the following:'
                         """
                         [1] Deposit
                         [2] Withdraw
                         [3] Account
                         [4] Exit
                         """ + '\n:'))

        system('clear')

        match int(service):
            case 1:
                customer.deposit()
            case 2:
                customer.withdraw()
            case 3:
                customer.client_info()
            case 4:
                'break'
            case _:
                print('You need to make a selection [1,2, or 3]')


start()








#ask user to choose: Deposit, Withdraw or Exit.. customer can never withdraw more
#than they have