import unittest
from User import user

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
        self.new_user  = user("NewUser", "963258741")
        def test_init(self):
            '''
            Test to ensure that the object is initialized properly
            '''
            
            
    
