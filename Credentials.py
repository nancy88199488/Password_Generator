class Credentials:
    '''
    Created class for credentials
    '''

    def __init__(self, account_name, account_password):
        self.account_name = account_name
        self.account_password = account_password

    credentials_list = []

    def save_credentials(self):
        '''
        Method that saves credentials objects into credentials_list
        '''
        self.credentials_list.append(self)

    def delete_credential(self):
        '''
        Method that deletes a particular credential
        '''
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_by_name(cls, account_name):
        '''
        Method that takes in a name and returns a credential that matches that particular name
        Args:
            name: account_name that has a password
        Return:
            the account_name and it's corresponding Password
        '''

        for credential in cls.credentials_list:
            if credential.account_name == account_name:
                return credential

    @classmethod
    def credential_exists(cls, name):
        '''
        Method to check if the credential exists
        Args:
        name: name of account to search if it exists
        boolean: True or False depending if the contatc exists
        '''

        for credential in cls.credentials_list:
            if credential.account_name == name:
                return True
        return False

    @classmethod
    def display_credentials(cls):
        '''
        Method which displays the current credentials
        '''
        return cls.credentials_list