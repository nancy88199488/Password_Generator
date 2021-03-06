import unittest
from User import User

class TestUser(unittest.TestCase):
        '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
def setUp(self):
        '''
        Set up method to run before each test cases  to check if the class has been instantiated correctly

        '''
        self.new_user  = User("NewUser", "963258741")

def test_init(self):
            '''
            Test to ensure that the object is initialized properly
            '''
            self.assertEqual(self.new_user.user_name, "NewUser")
            self.assertEqual(self.new_user.password,  "963258741")

def test_save_user(self):
                '''
                  test_save_user test case to test if the user object is saved into the user list
                '''
                self.new_user.save_user()
                self.assertEqual(len(User.user_list),1)

if __name__  ==  '__main__':
                    unittest.main()



            
    
