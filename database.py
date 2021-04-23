import os
import validation
# """
# Making a folder directory to save all user details

# """
user_db_path = "Data/user_details/"

def create(user_acct_no, first_name, last_name, email, password):
    user_details = first_name + "," + last_name + "," + email + "," + password + "," + str(0)
    f = open(user_db_path + str(user_acct_no) + ".txt", "x")
    f.write(user_details);
    completion_state = True
    f.close();
    return completion_state
    
# """
#    This first Loop helps to know if random account generated comes up again to be the same with the new generated account
    
# """
    # if existing_account(user_acct_no):
    #     print("Account already exist")
    #     return False

# """
#     This first Loop helps to know if email comes up again to be the same with the new email provided
    
# """
    # if existing_email(email):
    #     print("email already exist")
    #     return False
    
# """
#     This will open directory to save the new account details for users
    
# """
    completion_state = False

    try:
        f = open(user_db_path + str(user_acct_no) + ".txt", "x")

    except FileExistsError:
        
        contain_file = read(user_db_path + str(user_acct_no) + ".txt", "x")
        if not contain_file:
            delete(user_acct_no)

# """
#     Checking or reading the content of file before delete operation(empty file)
# """
    else:
        f.write(str(user_datails));
        completion_state = True

    finally:
        f.close();
        return completion_state




def delete(user_acct_no):
    
    is_deleted = False

    if os.path.exists(user_db_path + str(user_acct_no) + ".txt"):

        try:
            os.remove(user_db_path + str(user_acct_no) + ".txt")
            is_deleted = True

        except FileNotFoundError:
            print("user not found")

        finally:
            return is_deleted




def read(user_acct_no):
    is_valid_account_number = validation.account_validation(user_acct_no)
    
    try:
        if is_valid_account_number:
            f = open(user_db_path + str(user_acct_no) + ".txt", "r")

        else:
            f = open(user_db_path + user_acct_no, "r")

    except FileNotFoundError:
        print("user not found")
    
    except TypeError:
        print("Invalid Account Number format")

    except FileExistsError:
        print("User does not exit!")

    else:
        return f.readline()

    return False


def existing_email(email):
    all_users = os.listdir(user_db_path)

    for user in all_users:
        user_list = str.split(read(user), ',')
        if email in user_list:
            return True
    return False


def existing_account(user_acct_no):
    all_users = os.listdir(user_db_path)
    for user in all_users:
        if user == str(user_acct_no) + ".txt":
            return True
    
    return False


def authenticated_user(account_number, password):
    if existing_account(account_number):
        # user_raw = read(account_number)
        user = str.split(read(account_number), ',')
        if password == user[3]:
            return user

    return False


# print(read(1234567890))
# print("\n")
# print(read(5644688465))
# print(existing_email('walebioye@gmail.com'))
# print(existing_account(5644688465))
# create(1234567890, ["wale", 'abioye', 'walebioye@gmail.com', 'password', '200'])
# delete(7531327048)






