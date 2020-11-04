# Import standard library
from typing import Union, List, Dict, Any, Optional, cast

class Time(object):
    '''

    '''

    __period: str = 'AM'
    __hours_simple: int = 0
    __total_seconds: int = 0

    def __init__(self) -> None:
        '''

        '''
        pass

    @property
    def hours(self) -> int:
        '''

        '''
        return int(self.__total_seconds/pow(base=60, exp=2))
    
    @hours.setter
    def hours(self, hours: int) -> None:
        '''

        '''
        # Validate input is type int
        if not isinstance(hours, type(1)):
            raise Exception('Error: Must enter an integer.')

        # Validate hours to be between 0 & 23
        if hours > 23:
            hours = 23
        elif hours < 0:
            hours = 0
        else:
            # Do nothing
            pass

        # Get hours in seconds
        self.__total_seconds -= pow(base=60, exp=2) * int(self.__total_seconds/pow(60,2)) \
            if self.__total_seconds > 3599 else 0
        self.__total_seconds += pow(base=60, exp=2) * hours
    
    @property
    def minutes(self) -> int:
        '''

        '''
        return int((self.__total_seconds - (self.hours * pow(60,2))) / 60)
    
    @minutes.setter
    def minutes(self, minutes: int) -> None:
        '''

        '''

        # Validate input is type int
        if not isinstance(minutes, type(1)):
            raise Exception('Error: Must enter an integer.')

        if minutes > 59:
            minutes = 59
        elif minutes < 0:
            minutes = 0
        else:
            # Do nothing
            pass

        # Remove minutes in seconds from self.__total_seconds and then
        # add minutes in seconds
        self.__total_seconds -= int((self.__total_seconds - (self.hours * pow(60,2))) / 60) * 60
        self.__total_seconds += minutes * 60
    
    @property
    def seconds(self) -> int:
        '''

        '''
        return (self.__total_seconds - (self.hours * pow(60,2))) % 60
    
    @seconds.setter
    def seconds(self, seconds: int) -> None:
        '''

        '''
        # Validate is type int
        if not isinstance(seconds, type(1)):
            raise Exception('Error: Must enter an integer.')

        if seconds > 59:
            seconds = 59
        elif seconds < 0:
            seconds = 0
        else:
            # Do nothing
            pass

        # Remove current seconds from self.__total_seconds and
        # add seconds to self.__total_seconds
        self.__total_seconds -= (self.__total_seconds - (self.hours * pow(60,2))) % 60
        self.__total_seconds += seconds