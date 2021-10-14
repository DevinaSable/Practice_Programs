class Employee:
    def __init__(self):                          #initializing
        print('Employee created')

    def __del__(self):                        # Deleting (calling destructor)
        print('Destructor is called, Employee deleted')

obj = Employee()
del obj