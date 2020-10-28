# Standard library imports
from abc import ABC
from abc import abstractmethod
from typing import Union

# 3rd Party imports (if any)

class Employee(ABC):
    '''
    Base abstact class to be derived by the HourlyEmployee and SalaryEmployee.

    Attributes
    ----------
    name: str\n
        Represents the name of the employee. Is left blank by default.
    
    Methods
    -------
    display: None\n
        Abstact method to be used by derived classes to display metadata.
    '''
    
    name: str

    def __init__(self) -> None:
        '''
        Initializes the classes. Sets name to ''.
        '''
        self.name = ''

    @abstractmethod    
    def display(self) -> None:
        '''
        Abstact method meant to dispaly class metadata in derived classes.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        pass

class HourlyEmployee(Employee):
    '''
    Represents an HourlyEmployee. Extends the Employee class.

    Attributes
    ----------
    hourly_wage: Union[float, int]\n
        Represents the hourly wage of the employee.

    Methods
    -------
    display: None\n
        Displays the object's metadata in <name> - $<wage>/hour form.
    '''

    hourly_wage: Union[float, int]

    def __init__(self) -> None:
        '''

        '''
        super().__init__()
        self.hourly_wage = 0.00
    
    def display(self):
        print(
            f"{self.name} - ${self.hourly_wage:.2f}/hour"
        )

class SalaryEmployee(Employee):
    '''
    Represents a salaried employee. Extends the Employee class.

    Attributes
    ----------
    salary: Union[float, int]\n
        Represents the salary of the employee in dollars per year.

    Methods
    -------
    display: None\n
        Displays the classes metadata in <name> - $<salary>/year format.
    '''

    salary: Union[float, int]

    def __init__(self) -> None:
        '''

        '''
        super().__init__()
        self.salary = 0.00
    
    def display(self) -> None:
        '''

        '''
        print(
            f"{self.name} - ${self.salary:.2f}/year"
        )