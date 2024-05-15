class People:
    def _init_(self, name=None, age=None):
        if name is not None:
            self.__name = name
        if age is not None:
            self.__age = age


    def get_name(self):
        return self.__name
   
    def get_age(self):
        return self.__age


# Uso da classe
people = People("Ana", 30)
print(people.get_name())
print(people.get_age())