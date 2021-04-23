import random
import database
import validation
import datetime
from getpass import getpass



now = datetime.datetime.now()

def init():
    valid_option = False
    print("Welcome to Halal-Bank")
    while valid_option == False:
        have_acct = int(input("Do you have an account with us? \n" "1. Yes \n" "2. No \n"))
        if have_acct == 1:
            valid_option = True
            login()
        elif have_acct == 2:
            valid_option = True
            sign_up()

        else:
            print("Invalid Option Selected")


def login():
    print("*********** Enter your Login Details ***********")
    user_acct_no = input("Enter your Account number:")
    valid_acct = validation.account_validation(user_acct_no)
    if valid_acct:
        password = getpass("Enter your password \n")
        user = database.authenticated_user(user_acct_no, password)
        if user:
            print("-*-*-*-*-*  Login Successful  -*-*-*-*-*")
            print("%s" %now)
            bank_operation(user)

        print('Invalid Account or password: Please Try Again!')
        login()
        
    else:
        print("Invalid Account, check if Account number is an integer up to 10 digit")
        init()

def sign_up():
    print("********** Sign Up **********")
    email = input("Enter your Email address \n")
    first_name = input("Enter your first name \n")
    last_name = input("Enter your last name \n")
    password = getpass("Create a passkey:")

    account_number = acct_generator()

    user_details = first_name + "," + last_name + "," + email + "," + password + "," + str(0)
    create_user = database.create(account_number, first_name, last_name, email, password)
    if create_user:
        print("Your Account has been Created")
        print("%s" %now)
        print("Your Account number is : %d" % account_number)
        print("======== proceed to login ========")
        login()
        try:
            account_number = acct_generator()
        except ValueError:
            print("Account generation failed due to internet connection")
            init()
    else:
        print("Something went wrong, please try again later")
        sign_up()


def bank_operation(user):
    print("Welcome to Halal Bank")
    select_an_option = int(input(
        "What would you like to do? \n" "1. Deposit \n" "2. Withdraw \n" "3. Logout \n" "4. Exit \n" "5. balance \n"))
    if select_an_option == 1:
        deposit()
    elif select_an_option == 2:
        withdraw()
    elif select_an_option == 3:
        logout()
    elif select_an_option == 4:
        exit()
    elif select_an_option == 5:
        current_balance(user_details)
    else:
        print("Invalid option selected please try again!")
        bank_operation(user_details)


def deposit(user_details):
    print("Maximum deposit is 1000000")
    Balance = user_details[4]
    deposit = float(input("How much would you like to deposit? \n"))
    print("You deposited %s to your food budget" % deposit)
    availableBalance = int(Balance) + int(deposit)
    print("******* Deposit Succesful *******")
    print("Your Balance is: %s" % availableBalance)
    init()


def withdraw():
    print("Minimum you can withdraw is 1000")
    Balance = 1000
    withdraw = float(input("How much would you like to withdraw from your food budget? \n"))
    print("You withdraw %s from your food budget" % withdraw)
    availableBalance = int(Balance) - int(withdraw)
    print("******* Withdrawal Succesful *******")
    print("Your Balance is: %s" % availableBalance)
    init()


def logout():
    print("********** Logout Successful **********")
    print("%s" %now)
    login()


def exit():
    print("%s" %now)
    init()


def current_balance(user_details):
    print("Your current balance is \n")
    print(user_details[4])
    bank_operation(user_details)




def acct_generator():
    print("======================================")
    return random.randrange(1111111111, 9999999999)


init()
