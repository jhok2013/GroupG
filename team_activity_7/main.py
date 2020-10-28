'''
Authors: James Hough
Date: 10/27/2020
Version: 1.0.0
'''

# Import third party libraries

from EmployeeSystem import EmployeeSystem

def main():
    employee_system: EmployeeSystem = EmployeeSystem()
    employee_system.cmdloop()

if __name__ == '__main__':
    main()