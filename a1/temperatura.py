class termômetro:
    def init(self):
        self.__temperatura_celsius = 0
   
    def definir_temperatura_celsius(self, temperatura):
        self.__temperatura_celsius = temperatura
   
    def definir_temperatura_fahrenheit(self, temperatura):
        # Converter Fahrenheit para Celsius
        self.__temperatura_celsius = (temperatura - 32) * 5/9
   
    def obter_temperatura_celsius(self):
        return self.__temperatura_celsius
   
    def obter_temperatura_fahrenheit(self):
        # Converter Celsius para Fahrenheit
        return (self.__temperatura_celsius * 9/5) + 32


# Uso da classe
termometro = termômetro()
termometro.definir_temperatura_celsius(25)
print("Temperatura em Celsius:", termometro.obter_temperatura_celsius())
print("Temperatura em Fahrenheit:", termometro.obter_temperatura_fahrenheit())


termometro.definir_temperatura_fahrenheit(77)
print("Temperatura em Celsius:", termometro.obter_temperatura_celsius())
print("Temperatura em Fahrenheit:", termometro.obter_temperatura_fahrenheit())