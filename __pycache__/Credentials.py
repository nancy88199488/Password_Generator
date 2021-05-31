 class Credentials:
     '''
      Created class for the credentials
      '''
      credentials_list = []

     def  __init__(self, account_name,  account_password);
     self.account_name = account_name
     self.account_password = account_password

     def save_credentials(self):
         '''
         Method that saves the credentials object into the credentials_list
         '''
         self.credentials_list.append(self)

         def delete_credentials(self):
             '''
         Method that deletes  credentials specified  
             '''
             @classmethod
             def credentials_exists(cls, name):
                 '''Method  that checks if a credential exists from the credentials list
                 Args:
                 name: name of the account to search if it exists
                 boolean: ttrue or false depending if the credential exists
                 '''
                 for credential in cls.credentials_list:
                     if credential.account_name == name:
                         return True
                         return False
                         def find_by_name(cls, account_name):
                             ''' 
                             Method that finds a credential and returns the credential that matches
                             Args: 
                             name: account_name that has a password
                             return:the account_name and it's corresponding password
                             '''
                             for credential in cls.credentials_list:
                                 if credential.account_name ==account_name:
                                     return credential
                                     @classmethod
                                     def display_credentials(cls):
                                         '''Method that displays the current credentials
                                         '''
                                         return cls.credentials_list


