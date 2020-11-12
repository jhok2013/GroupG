# Import standard library
from typing import Union, List, Dict, Any, Optional, cast

class Time(object):
    '''

    '''

    __total_seconds: int = 0

    def __init__(self) -> None:
        '''

        '''
        pass

    @property
    def hours_simple(self) -> int:
        '''

        '''
        return self.hours - 12 if self.period == 'PM' else self.hours
    
    @hours_simple.setter
    def hours_simple(self, hours_simple: int) -> None:
        '''

        '''
        # Validate input is type int
        if not isinstance(hours_simple, type(1)):
            raise Exception('Error: Must enter an integer.')

        # Validate that input is between 1 and 12
        if hours_simple > 12:
            hours_simple = 12
        elif hours_simple < 1:
            hours_simple = 1
        else:
            # Do nothing
            pass
        
        # Synchronize self.hours_simple and self.hours
        if self.hours != hours_simple and self.period == 'AM':
            self.hours = hours_simple
        elif self.hours != hours_simple and self.period == 'PM':
            self.hours = hours_simple + 12
        else:
            # Do nothing
            pass

    @property
    def period(self) -> str:
        '''

        '''
        return 'AM' if self.__total_seconds < 43200 else 'PM'
    
    @period.setter
    def period(self, period: str) -> None:
        '''

        '''
        # Validate is str type
        if not isinstance(period, type('str')):
            raise Exception('Error: Must enter a string.')

        # Validate that it is a valid variant of 'AM' or 'PM'
        if not period.lower() == 'am' and not period.lower() == 'pm':
            raise Exception('Error: Must bnot  or PM.')

        # Determine if in the AM hours. If in the am hours and
        # wanting to switch to PM, then add half of the total seconds
        # possible in the day. If the inverse then minus half of the
        # total seconds in the day. 
        am: bool = True if self.__total_seconds < 43200 else False
        if am and period.lower() == 'pm':
            self.__total_seconds += 43200
        elif not am and period.lower() == 'am':
            self.__total_seconds -= 43200

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