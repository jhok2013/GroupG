# Add standard library imports
import cmd
from typing import Union, List, cast

# Add third party imports
from Employees import Employee, HourlyEmployee, SalaryEmployee

class EmployeeSystem(cmd.Cmd):

    intro: str = 'Welcome to the Employee System. Type help or ? to list commands.\n'
    prompt: str = '(ES) '
    employee_list: List[Employee] = []

    # Basic commands
    def do_s(self, arg) -> None:
        '''
        Adds a salaried employee. Prompts the user for name and salary.
        '''
        salary_employee: SalaryEmployee = SalaryEmployee()
        salary_employee.name = str(input("Name: "))
        salary_employee.salary = cast(Union[float, int], float(input("Salary: ")))
        self.employee_list.append(salary_employee)

    def do_h(self, arg) -> None:
        '''
        Adds an hourly employee. Prompts the user for name, hours, and wage.
        '''
        hourly_employee: HourlyEmployee = HourlyEmployee()
        hourly_employee.name = str(input("Name: "))
        hourly_employee.hours = cast(Union[float, int], float(input('Hours: ')))
        hourly_employee.hourly_wage = cast(Union[float, int], float(input('Hourly wage: ')))
        self.employee_list.append(hourly_employee)

    def do_q(self, arg) -> None:
        '''
        Displays all employee information. Exits the program.
        '''
        for employee in self.employee_list:
            employee.display()
        quit()
    
    def do_d(self, arg) -> None:
        '''
        Displays an employee's information.
        Example: d 'James Hough'
        '''
        if arg:
            emp_list: List[Employee] = [emp for emp in self.employee_list if emp.name == arg]
            if emp_list:
                for emp in emp_list:
                    emp.display()
            else:
                print(f'{self.prompt}Employee not found.')
        else:
            print(f'{self.prompt}No name provided. Please provide employee name.')
    