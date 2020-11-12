# Standard library imports
from typing import Union, Any

# Organization imports
from CheckingExceptions import BalanceError, OutOfChecksError

class CheckingAccount(object):
    '''

    '''
    __balance: Union[float, int]
    __check_count: int

    def __init__(self, starting_balance: Union[float, int] = 0,
                       num_checks: Union[float, int] = 0) -> None:
        '''

        '''
        self.balance = starting_balance
        self.__check_count = num_checks
    
    @property
    def balance(self) -> Union[float, int]:
        '''

        '''
        return self.__balance
    
    @balance.setter
    def balance(self, amount: Union[float, int]) -> None:
        '''

        '''
        try:
            if amount > 0:
                if isinstance(amount, type(int(1))) or isinstance(amount, type(float(1))):
                    self.__balance += amount
                else:
                    raise ValueError
            else:
                raise ValueError
        except ValueError:
            print(
                f"Invalid Deposit Amount",
                f"--------------------------",
                f"Amount: ${amount:.2f}",
                f"",
                f"Must be a positive number."
            )

    def deposit(self, amount: Union[float, int]) -> None:
        '''
        
        '''
        try:
            if amount > 0:
                self.__balance += amount
            else:
                raise ValueError
        except ValueError:
            print(
                f"Invalid Deposit Amount",
                f"--------------------------",
                f"Amount: ${amount:.2f}",
                f"",
                f"Cannot deposit a negative or null amount."
            )

    def write_check(self, amount: Union[float, int]) -> None:
        '''

        '''
        try:
            if self.__balance > amount:
                if amount > 0:
                    self.__balance -= amount
                else:
                    raise ValueError
            else:
                raise BalanceError
            if self.__check_count != 0:
                self.__check_count -= 1
            else:
                raise OutOfChecksError
        except BalanceError:
            print(
                f"Insufficient Funds",
                f"------------------",
                f"Balance: ${self.__balance:.2f}",
                f"Withdraw Amount: ${amount:.2f}",
                f"------------------",
                f"Overdraft Amount: ${(self.__balance - amount):.2f}",
                sep="\n"
            )
        except OutOfChecksError:
            print(
                f"Error: Insufficient Checks",
                f"---------------------------",
                f"You are currently out of checks.",
                sep="\n"
            )
            if self.__balance >= 5:
                user_input: str = str(input('Would you like to commission 25 checks for $5.00? (y/n): '))
                if user_input.lower() == 'y' or user_input.lower() == 'yes':
                    self.__balance -= 5
                    self.__check_count += 25
                    print(
                        f"25 have been commissioned for $5.00.",
                        sep="\n"    
                    )
                    self.display()
            else:
                print(f"Please commission more checks and try again.")
        except ValueError:
            print(
                f"Invalid Withdrawal Amount",
                f"--------------------------",
                f"Amount: ${amount:.2f}",
                f"",
                f"Cannot withdraw a negative or null amount."
            )

    def display(self) -> None:
        '''

        '''
        print(
            f"Account Information",
            f"-------------------",
            f"Balance: ${self.__balance:.2f}",
            f"Checks: {self.__check_count}",
            sep="\n"
        )

    def apply_for_credit(self, amount: Union[float, int]) -> None:
        '''

        '''
        message: str = (
            f"This method is not yet available."
        )
        raise NotImplementedError(message)