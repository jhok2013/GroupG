# Standard library imports
from pathlib import Path
from sys import path
from typing import Union, Any, List, Dict, cast, Any
import unittest

# Add project to path
path.insert(0, str(Path('C:\projects').resolve()))

# 3rd party imports
from GroupG.team_activity_8.timeObject.Time import Time #type: ignore

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
    
    def test_invalid_type(self) -> None:
        '''

        '''
        expected_hours: int = 0
        error_message: str = 'Error: Must enter an integer.'
        with self.assertRaises(Exception) as context:
            self.time.hours = 'Not an integer'
            self.assertTrue(error_message in context.exception) #type: ignore
        self.assertEqual(
            first=expected_hours,
            second=self.time.hours
        )
    
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
    
    def test_period_pm_am(self) -> None:
        '''

        '''
        # Arrange
        new_period: str = 'AM'
        normal_hours: int = 12
        normal_minutes: int = 1
        normal_seconds: int = 0
        expected_period: str = 'AM'
        expected_hours: int = 0
        expected_minutes: int = 1
        expected_seconds: int = 0

        # Act
        self.time.hours = normal_hours
        self.time.minutes = normal_minutes
        self.time.seconds = normal_seconds
        self.time.period = new_period

        # Assert
        self.assertEqual(
            first=[
                expected_hours,
                expected_minutes,
                expected_seconds,
                expected_period
            ],
            second=[
                self.time.hours,
                self.time.minutes,
                self.time.seconds,
                self.time.period
            ]
        )

    def test_period_am_am(self) -> None:
        '''

        '''
        # Arrange
        new_period: str = 'AM'
        normal_hours: int = 11
        normal_minutes: int = 59
        normal_seconds: int = 59
        expected_period: str = 'AM'
        expected_hours: int = 11
        expected_minutes: int = 59
        expected_seconds: int = 59

        # Act
        self.time.hours = normal_hours
        self.time.minutes = normal_minutes
        self.time.seconds = normal_seconds
        self.time.period = new_period

        # Assert
        self.assertEqual(
            first=[
                expected_hours,
                expected_minutes,
                expected_seconds,
                expected_period
            ],
            second=[
                self.time.hours,
                self.time.minutes,
                self.time.seconds,
                self.time.period
            ]
        )
    
    def test_period_am_pm(self) -> None:
        '''

        '''
        # Arrange
        new_period: str = 'PM'
        normal_hours: int = 11
        normal_minutes: int = 59
        normal_seconds: int = 59
        expected_period: str = 'PM'
        expected_hours: int = 23
        expected_minutes: int = 59
        expected_seconds: int = 59

        # Act
        self.time.hours = normal_hours
        self.time.minutes = normal_minutes
        self.time.seconds = normal_seconds
        self.time.period = new_period

        # Assert
        self.assertEqual(
            first=[
                expected_hours,
                expected_minutes,
                expected_seconds,
                expected_period
            ],
            second=[
                self.time.hours,
                self.time.minutes,
                self.time.seconds,
                self.time.period
            ]
        )
    
    def test_period_pm_pm(self) -> None:
        '''

        '''
        # Arrange
        new_period: str = 'PM'
        normal_hours: int = 23
        normal_minutes: int = 59
        normal_seconds: int = 59
        expected_period: str = 'PM'
        expected_hours: int = 23
        expected_minutes: int = 59
        expected_seconds: int = 59

        # Act
        self.time.hours = normal_hours
        self.time.minutes = normal_minutes
        self.time.seconds = normal_seconds
        self.time.period = new_period

        # Assert
        self.assertEqual(
            first=[
                expected_hours,
                expected_minutes,
                expected_seconds,
                expected_period
            ],
            second=[
                self.time.hours,
                self.time.minutes,
                self.time.seconds,
                self.time.period
            ]
        )

    def test_invalid_period_type(self) -> None:
        '''

        '''
        expected_hours: int = 23
        bad_period: int = 1
        error_message: str = 'Error: Must enter a string.'
        with self.assertRaises(Exception) as context:
            self.time.hours = expected_hours
            self.time.period = bad_period
            self.assertTrue(error_message in context.exception) #type: ignore
        self.assertEqual(
            first=expected_hours,
            second=self.time.hours
        )

    def test_invalid_period_string(self) -> None:
        '''

        '''
        expected_hours: int = 23
        bad_period: str = 'AMM'
        error_message: str = 'Error: Must enter a string.'
        with self.assertRaises(Exception) as context:
            self.time.hours = expected_hours
            self.time.period = bad_period
            self.assertTrue(error_message in context.exception) #type: ignore
        self.assertEqual(
            first=expected_hours,
            second=self.time.hours
        )

    def test_invalid_hour_simple_type(self) -> None:
        '''

        '''
        expected_simple_hours: int = 0
        bad_simple_hours: str = 'Not a number'
        error_message: str = 'Error: Must enter an integer.'
        with self.assertRaises(Exception) as context:
            self.time.hours_simple = expected_simple_hours
            self.assertTrue(error_message in context.exception) #type: ignore
        self.assertEqual(
            first=expected_simple_hours,
            second=self.time.hours_simple
        )
    
    def test_hours_simple_normal(self) -> None:
        '''

        '''
        # Arrange
        normal_period: str = 'PM'
        normal_hours: int = 23
        normal_minutes: int = 59
        normal_seconds: int = 59
        normal_hours_simple: int = 11
        expected_period: str = 'PM'
        expected_hours: int = 23
        expected_minutes: int = 59
        expected_seconds: int = 59
        expected_hours_simple: int = 11

        # Act
        self.time.hours = normal_hours
        self.time.minutes = normal_minutes
        self.time.seconds = normal_seconds
        self.time.period = normal_period
        self.time.hours_simple = normal_hours_simple

        # Assert
        self.assertEqual(
            first=[
                expected_hours,
                expected_minutes,
                expected_seconds,
                expected_period,
                expected_hours_simple
            ],
            second=[
                self.time.hours,
                self.time.minutes,
                self.time.seconds,
                self.time.period,
                self.time.hours_simple
            ]
        )

if __name__ == '__main__':
    unittest.main()
