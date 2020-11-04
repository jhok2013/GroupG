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
        # Arrange
        expected_hours: int
        normal_hours: int = 22
        bad_small_hours: int = -1
        bad_big_hours: int = 24
        zero_hours: int = 0

        # Act
        ## Normal hours test
        expected_hours = 22
        self.time.hours = normal_hours
        self.assertEqual(expected_hours, self.time.hours, msg='Ran test 1 successfully.')

        ## Hours are too small test
        expected_hours = 0
        self.time.hours = bad_small_hours
        self.assertEqual(expected_hours, self.time.hours, msg='Ran test 1 successfully.')

        ## Hours are too big test
        expected_hours = 23
        self.time.hours = bad_big_hours
        self.assertEqual(expected_hours, self.time.hours, msg='Ran test 1 successfully.')

        ## Hours is 0
        expected_hours = 0
        self.time.hours = zero_hours
        self.assertEqual(expected_hours, self.time.hours)
    
    
    def test_minutes_normal(self) -> None:
        '''

        '''
        # Arrange
        expected_minutes: int = 45
        expected_hours: int = 10
        normal_minutes: int = 45
        normal_hours: int = 10

        # Act
        self.time.hours = normal_hours
        self.time.minutes = normal_minutes

        # Act
        self.assertEqual(
            first=expected_hours,
            second=self.time.hours
        )
        self.assertEqual(
            first=expected_minutes,
            second=self.time.minutes
        )

    
    def test_minutes_too_big(self) -> None:
        '''

        '''
        # Arrange
        expected_minutes: int = 59
        expected_hours: int = 10
        minutes: int = 60
        hours: int = 10

        # Act
        self.time.hours = hours
        self.time.minutes = minutes

        # Act
        self.assertEqual(
            first=expected_hours,
            second=self.time.hours
        )
        self.assertEqual(
            first=expected_minutes,
            second=self.time.minutes
        )

    
    def test_minutes_too_small(self) -> None:
        '''

        '''
        # Arrange
        expected_minutes: int = 0
        expected_hours: int = 10
        minutes: int = -1
        hours: int = 10

        # Act
        self.time.hours = hours
        self.time.minutes = minutes

        # Act
        self.assertEqual(
            first=expected_hours,
            second=self.time.hours
        )
        self.assertEqual(
            first=expected_minutes,
            second=self.time.minutes
        )

    
    def test_minutes_zero(self) -> None:
        '''

        '''
        # Arrange
        expected_minutes: int = 0
        expected_hours: int = 10
        minutes: int = 0
        hours: int = 10

        # Act
        self.time.hours = hours
        self.time.minutes = minutes

        # Act
        self.assertEqual(
            first=expected_hours,
            second=self.time.hours
        )
        self.assertEqual(
            first=expected_minutes,
            second=self.time.minutes
        )

    
    def test_minutes_normal_zero_hour(self) -> None:
        '''

        '''
        # Arrange
        expected_minutes: int = 45
        expected_hours: int = 0
        minutes: int = 45
        hours: int = 0

        # Act
        self.time.hours = hours
        self.time.minutes = minutes

        # Act
        self.assertEqual(
            first=expected_hours,
            second=self.time.hours
        )
        self.assertEqual(
            first=expected_minutes,
            second=self.time.minutes
        )

    
    def test_seconds_normal(self) -> None:
        '''

        '''
        # Arrange
        expected_seconds: int = 30
        expected_minutes: int = 45
        expected_hours: int = 1
        seconds: int = 30
        minutes: int = 45
        hours: int = 1

        # Act
        self.time.hours = hours
        self.time.minutes = minutes
        self.time.seconds = seconds

        # Act
        self.assertEqual(
            first=expected_hours,
            second=self.time.hours
        )
        self.assertEqual(
            first=expected_minutes,
            second=self.time.minutes
        )
        self.assertEqual(
            first=expected_seconds,
            second=self.time.seconds
        )

    
    def test_seconds_big_seconds(self) -> None:
        '''

        '''
        # Arrange
        expected_seconds: int = 59
        expected_minutes: int = 45
        expected_hours: int = 1
        seconds: int = 60
        minutes: int = 45
        hours: int = 1

        # Act
        self.time.hours = hours
        self.time.minutes = minutes
        self.time.seconds = seconds

        # Act
        self.assertEqual(
            first=expected_hours,
            second=self.time.hours
        )
        self.assertEqual(
            first=expected_minutes,
            second=self.time.minutes
        )
        self.assertEqual(
            first=expected_seconds,
            second=self.time.seconds
        )

    
    def test_seconds_small_seconds(self) -> None:
        '''

        '''
        # Arrange
        expected_seconds: int = 0
        expected_minutes: int = 45
        expected_hours: int = 1
        seconds: int = -1
        minutes: int = 45
        hours: int = 1

        # Act
        self.time.hours = hours
        self.time.minutes = minutes
        self.time.seconds = seconds

        # Act
        self.assertEqual(
            first=expected_hours,
            second=self.time.hours
        )
        self.assertEqual(
            first=expected_minutes,
            second=self.time.minutes
        )
        self.assertEqual(
            first=expected_seconds,
            second=self.time.seconds
        )
    
    def test_seconds_zero(self) -> None:
        '''

        '''
        # Arrange
        expected_seconds: int = 0
        expected_minutes: int = 45
        expected_hours: int = 1
        seconds: int = 0
        minutes: int = 45
        hours: int = 1

        # Act
        self.time.hours = hours
        self.time.minutes = minutes
        self.time.seconds = seconds

        # Act
        self.assertEqual(
            first=expected_hours,
            second=self.time.hours
        )
        self.assertEqual(
            first=expected_minutes,
            second=self.time.minutes
        )
        self.assertEqual(
            first=expected_seconds,
            second=self.time.seconds
        )

    def test_seconds_zero_minutes_zero_hours(self) -> None:
        '''

        '''
        # Arrange
        expected_seconds: int = 1
        expected_minutes: int = 0
        expected_hours: int = 0
        seconds: int = 1
        minutes: int = 0
        hours: int = 0

        # Act
        self.time.hours = hours
        self.time.minutes = minutes
        self.time.seconds = seconds

        # Act
        self.assertEqual(
            first=expected_hours,
            second=self.time.hours
        )
        self.assertEqual(
            first=expected_minutes,
            second=self.time.minutes
        )
        self.assertEqual(
            first=expected_seconds,
            second=self.time.seconds
        )

if __name__ == '__main__':
    unittest.main()
