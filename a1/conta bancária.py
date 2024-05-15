class ContaBancaria:
    def _init_(self, saldo_inicial):
        self._saldo = saldo_inicial  # Atributo protegido


    def depositar(self, valor):
        self._saldo += valor




    def get_saldo(self):
        return self._saldo
   
   


# Uso da classe
contabancaria = ContaBancaria(1000)
contabancaria.depositar(500)
print(contabancaria.get_saldo())