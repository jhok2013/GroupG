# Import standard library
from typing import Union, List, Dict, Any, Optional, cast

class Time(object):
    '''

    '''

    __period: str = 'AM'
    __hours_simple: int = 0
    __total_seconds: int = 0
    __hours: int = 0
    __minutes: int = 0
    __seconds: int = 0

    def __init__(self) -> None:
        '''

        '''
        pass

    @property
    def hours(self) -> int:
        '''

        '''
        return self.__hours
    
    @hours.setter
    def hours(self, hours: int) -> None:
        '''

        '''
        # Validate hours to be between 0 & 23
        if hours > 23:
            hours = 23
        elif hours < 0:
            hours = 0
        else:
            hours = hours

        # Remove self.__hours in seconds from self.__total_seconds
        # and add hours in seconds
        self.__total_seconds -= pow(base=60, exp=2) * self.__hours
        self.__total_seconds += pow(base=60, exp=2) * hours
        self.__hours = hours