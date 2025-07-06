class example :
    # static variable or static method
    stat_variable = 1
    # public access
    def __init__(self):
        self.id = example.stat_variable
        example.stat_variable += 1
        self.public_var = 'I am Public'

    # protected access
        self._protected_var = "I am Protected"

    # private access
        self.__private_Var = "I am private"

    # getters
    def get(self):
        return self.__private_Var
    
    # setter
    def set(self,name):
        self.__private_Var = name

    # we can use getter and setter for static method also
    @staticmethod #decorator
    def get_static():
        return example.stat_variable

    @staticmethod
    def set_static(val):
        example.stat_variable = val
    
obj = example()
print(obj.public_var)
print(obj._protected_var)
# print(obj.__private_Var)
# private attribute can be accessed using following method
obj.set("I am Pratik")
print(obj.get())
obj1 = example()
obj2 = example()
print(obj1.id)
print(obj2.id)

obj3 = example()
obj3.set_static(123)
print(obj.get_static())