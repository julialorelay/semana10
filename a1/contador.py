class Contador:
    def __init__(self, valor = 200):
        self.__valor = valor
   
    def incrementar(self, valor):
        self.__valor += valor


    def decrementar(self, valor):
        self.__valor = 50


    def get_valor(self):
        return self.__valor


contador = Contador()
print('After declaration:', contador.get_valor())  
contador.incrementar(100)
print('+100:', contador.get_valor())
contador.decrementar(50)