


class Employee:
    def __init__(self, name, salary, position):
        self.name = name
        self.salary = int(salary)
        self.position = position

    @classmethod
    def from_file(cls, filepath):
        """Creates and returns a list of Employee instances from a file."""
        employees = []
        with open(filepath, 'r') as f:
            for line in f:
                # Skip empty lines
                line = line.strip()
                if not line:
                    continue
                
                # Parse data and instantiate object
                name, salary, position = line.split(',')
                employees.append(cls(name.strip(), salary.strip(), position.strip()))
        
        return employees


employees = Employee.from_file('info.txt')

for emp in employees:
    print(f'The Employee {emp.name} he works as {emp.position} and he makes {emp.salary} per month')

"""
Transform this example into generators instead of appending to a list
"""

