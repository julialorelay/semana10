class Contador:
    def __init__(self, valor = 200):
        self.__valor = valor
   
    def incrementar(self, valor):
        self.__valor = 300


    def decrementar(self, valor):
        self.__valor = 50


    def get_valor(self):
        return self.__valor


contador = Contador()
contador.incrementar(300)
contador.incrementar(300)
print(contador.get_valor())  
contador.decrementar(50)