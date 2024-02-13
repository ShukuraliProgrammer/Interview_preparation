class Employee:
    _emp_name = None
    __emp_age = None

    def __int__(self, emp_age, emp_name):
        self.__emp_age = emp_age
        self._emp_name = emp_name

    def display(self):
        print(f"Name: {self._emp_name} - Age: {self.__emp_age}")


obj1 = Employee(19, "sli")
obj1.display()
