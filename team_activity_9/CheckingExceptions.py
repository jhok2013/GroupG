from typing import Union

class BalanceError(Exception):
    '''

    '''
    def __init__(self, overage_amount: Union[float, int]) -> None:
        '''

        '''
        self.__message: str = (
            f"Insufficient Funds\n"
            f"------------------\n"
            f"Overage Amount: ${overage_amount:.2f}"
        )
        super().__init__(self.__message)

class OutOfChecksError(Exception):
    '''

    '''
    __message: str = 'Insufficient checks.'
    def __init__(self) -> None:
        '''

        '''
        super().__init__(self.__message)