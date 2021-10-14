#creating a base class
class Base:
    def __init__(self):
        self.a = "GeekforFolks"
        self.__C = "GeekForFolks"

#Creating a derived class
class Derived(Base):
    def __init__(self):
        #calling a constructor of base class
        Base.__init__(self)
        print("Calling private number of base class:")
        print(self.__a)
#Derived code
obj = Derived()
