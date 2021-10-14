class Dog:
    attr1 = 'mamal'                #a simple class attribute
    attr2 = 'dog'

    def fun(self):                 # a sample method
        print('1 I am a ', self.attr1)
        print('2 I am a ', self.attr2)

Rodger = Dog()             # Driver code | object instantisation
print(Rodger.attr1)          # Accessing class attributes amd methods through objects
Rodger.fun()
