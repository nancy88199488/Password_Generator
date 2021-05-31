import random
from User import User
from Credentials import Credentials

 # Functions to add credentials

def create_new_credential(account_name, account_password):
    """
    Function to create a new account and its credentials
    """
    new_credential = Credentials(account_name, account_password)
    return new_credential


def save_new_credential(credentials):
    """
    Function to save the created account and password
    """
    credentials.save_credentials()


def find_credential(account_name):
    """
    Function that finds credentials based on account_name given
    """
    return Credentials.find_by_name(account_name)


def check_existing_credentials(name):
    """
    Method that checks if a particular account and its credentials exists based on entered account_name
    """
    return Credentials.find_by_name(name)


def display_credentials():
    """ 
    Function which displays the saved credentials
    """
    return Credentials.display_credentials()


def delete_credential(credentials):
    """
    Method that deletes credentials
    """
    return Credentials.delete_credential(credentials)

def main():
    while True:
        print("Hello! Welcome to the password locker")
        print('\n')
        print("Use these short codes to select an option: Create new user use 'cu': Login to your account use 'lg' or 'ex' to exit password locker")
        short_code = input().lower()
        print('\n')
        if short_code == 'cu':
            print('create username')
            created_user_name = input()
            print('create password')
            created_user_password = input()
            print('confirm password')
            confirm_password = input()
            while confirm_password != created_user_password:
                print('Wrong password did not match!')
                print('Enter your password')
                created_user_password = input()
                print('Confirm your password')
                confirm_password = input()
            else:
                print(f"congratulations {created_user_name}! account created  successfully")
                print('\n')
                print("Proceed to login")
                print("username")
                entered_username = input()
                print("Your password")
                entered_password = input()
            while entered_username != created_user_name or entered_password != created_user_password:
                print("You entered a wrong username or password")
                print("username")
                entered_username = input()
                print("Your password")
                entered_password = input()
            else:
                print(f"welcome: {entered_username} to your account")
                print("\n")

                while True:
                    print("1: View Your saved credentials")
                    print("2: Add new credentials")
                    print("3: Remove credentials")
                    print("4: Search credentials")
                    print("5: Log Out")
                    option = input()

                    if option == '2':
                        while True:
                            print("Continue to add? y/n")

                            choice = input().lower()
                            if choice == 'y':
                                print("Saved the account name")
                                account_name = input()
                                print("Enter a password")
                                print(
                                    "To generate random password enter keyword 'gp' or 'n' to create your own password")
                                keyword = input().lower()
                                if keyword == 'gp':
                                    account_password = random.randint(111111, 1111111)
                                    print(f"Account: {account_name}")
                                    print(f"Password: {account_password}")
                                    print('\n')
                                elif keyword == 'n':
                                    print("Create your password")
                                    account_password = input()
                                    print(f"Account: {account_name}")
                                    print(f"Password: {account_password}")
                                    print('\n')

                                else:
                                    print("Please enter a valid Code")

                                save_new_credential(create_new_credential(
                                    account_name, account_password))
                            elif choice == 'n':
                                break
                            else:
                                print("Please use 'y' for yes or 'n' for no!")
                    elif option == '1':
                        while True:
                            print("Below is a list of all your credentials")
                            if display_credentials():

                                for credential in display_credentials():
                                    print(f"Account name:{credential.account_name}")
                                    print(f"Password:{credential.account_password}")

                            else:
                                print('\n')
                                print("You don't seem to have any credentials yet")
                                print('\n')

                            print("Back to Menu? y/n")

                            back = input().lower()
                            if back == 'y':
                                break
                            elif back == 'n':
                                continue
                            else:
                                print("Please Enter a valid code")
                                continue

                    elif option == '5':
                        print("Warning! You will loose all your credentials if you log out. Are you sure? y/n")
                        logout = input().lower()

                        if logout == 'y':
                            print("You have Successfully logged out")
                            break
                        elif logout == 'n':
                            continue
                    elif option == '3':
                        while True:
                            print("Search for credential to delete")

                            search_name = input()

                            if check_existing_credentials(search_name):
                                search_credential = find_credential(search_name)
                                print(f"Account name: {search_credential.account_name} \n Password: {search_credential.account_password}")
                                print("Delete? y/n")
                                sure = input().lower()
                                if sure == 'y':
                                    delete_credential(search_credential)
                                    print("Account deleted successfully")
                                    break
                                elif sure == 'n':
                                    continue

                            else:
                                print("That credential does not exist")
                                break

                    elif option == '4':
                        while True:
                            print("Continue? y/n")
                            option2 = input().lower()
                            if option2 == 'y':
                                print("Enter an account name to find credentials")

                                search_name = input()

                                if check_existing_credentials(search_name):
                                    search_credential = find_credential(search_name)
                                    print(f"Account name: {search_credential.account_name} \n password: {search_credential.account_password}")
                                else:
                                    print("That credential does not exist")
                            elif option2 == 'n':
                                break
                            else:
                                print("Please enter a valid code")
                        continue
        elif short_code == 'lg':
            print("Welcome")
            print("Enter user name")
            default_user_name = input()
            print("Enter password")
            default_user_password =input()
            print('\n')
            while default_user_name != 'testuser' or default_user_password != '3698word':
                print("Wrong username or password.Username 'testuser' and password '3698word")
                print("Enter user name")
                default_user_name = input()
                print("Enter password")
                default_user_password = input()
                print("\n")
            else:
                print("login success")
                print('\n')
                print('\n')
        elif short_code == 'ex':
            break
        else:
            print("Enter valid code to continue")
if __name__ == '__main__':
    main()
