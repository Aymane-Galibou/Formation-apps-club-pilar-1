import pandas 


class Employee:
    MIN_SALAIRE = 3000


    def __init__(self,name,salary,job):
        self.name = name 
        self.job = job

        if salary > Employee.MIN_SALAIRE :
            self.salary = salary
        else :
            self.salary = Employee.MIN_SALAIRE

    def display_info(self):
        print(f'Le salarie {self.name} , et son salaire est : {self.salary}')


    @classmethod
    def create_from_file(cls,file):
        with open(file) as f :

            for line in f :
                line = line.strip()

                if not line :
                    continue
                
                info_employee = line.strip().split(',')

                name , salary , job = info_employee[0].strip() , int(info_employee[1].strip()), info_employee[2].strip()
                
                if name == 'lionel messi':
                    emp1 = cls(name,salary,job)
                    return emp1


emp1 = Employee.create_from_file('info.txt')

emp1.display_info()
    





