def account_validation(user_acct_no):
    if user_acct_no:
        if len(str(user_acct_no)) == 10:
            try:
                int(user_acct_no)
                return True
            except ValueError:
                print("Invalid account number, Account number should be integer")
                return False
            except TypeError:
                print("Invalid account Type")
        else:
            print("Account number can not be less or more than 10 digits")

    else:
        print("Account number is a required field")
        return False

