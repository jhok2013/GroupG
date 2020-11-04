# Standard library imports
from pathlib import Path
from sys import path
from typing import Union, Any, List, Dict, cast, Any
import unittest

# Add project to path
path.insert(0, str(Path('C:\projects').resolve()))

# 3rd party imports
from GroupG.team_activity_8.timeObject.Time import Time

class test_time(unittest.TestCase):
    '''

    '''

    def setUp(self):
        self.time = Time()
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()
    
    def test_hours_setter(self):
        '''

        '''
        hours: int = 22
        self.time.hours = hours
        self.assertEqual(hours, self.time.hours, msg='Ran test 1 successfully.')

if __name__ == '__main__':
    unittest.main()
