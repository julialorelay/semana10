class Veiculo:
    def _init_(self, acelerar):
        self.acelerar = acelerar

    def get_acelerar(self):
        return self.acelerar

veiculo = Veiculo("Velocidade máxima")

class Carro(Veiculo):
    def acelerar(self):
        print("Carro acelerando.")

class Motocicleta(Veiculo):
    def acelerar(self):
        print("Motocicleta acelerando.")