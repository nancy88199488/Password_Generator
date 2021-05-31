class User:
    '''
    class that generates new instance of user
    '''
    user_list =[]
    def __init__(self, use_name, password):
        self.use_name = use_name
        self.password = password
    def save_user(self):