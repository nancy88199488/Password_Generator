# # import random
# from User import User
# def main():
#     while True:
#         print("Thank you and welcome to the password locker")
#         print('\n')
#         print("pick a code to navigate through:to create new user use 'nu':To login into your account 'lg' or 'ex' to exit")
#         short_code = input().lower()
#         print('\n')
#         if short_code == 'nu':
#             print('create username')
#             created_user_name = input()
#             print('create password')
#             created_user_password = input()
#             print('confirm password')
#             confirm_password = input()
#             while confirm_password != created_user_password:
#                 print('invalid password did not match!')
#                 print('enter your password')
#                 created_user_password = input()
#                 print('confirm your password')
#                 confirm_password = input()
#             else:
#                 print(f"congratulations{created_user_name}!account creation successful")
#                 print('\n')
#                 print("proceed to login")
#                 print("username")
#                 entered_username = input()
#                 print("your password")
#                 entered_password = input()
#             while entered_username != created_user_name or entered_password != created_user_password:
#                 print("you entered a wrong username or password")
#                 print("username")
#                 entered_username = input()
#                 print("your password")
#                 entered_password = input()
#             else:
#                 print(f"welcome: {entered_username} to your account")
#                 print("\n")
#         elif short_code == 'lg':
#             print("welcome")
#             print("Enter user name")
#             default_user_name = input()
#             print("Enter password")
#             default_user_password =input()
#             print('\n')
#             while default_user_name != 'testuser' or default_user_password != '09876':
#                 print("wrong userName or password.Username 'testuser' and password '09876'")
#                 print("Enter user name")
#                 default_user_name = input()
#                 print("Enter password")
#                 default_user_password = input()
#                 print("\n")
#             else:
#                 print("login success")
#                 print('\n')
#                 print('\n')
#         elif short_code == 'ex':
#             break
#         else:
#             print("Enter valid code to continue")
# if __name__ == '__main__':
#     main()
