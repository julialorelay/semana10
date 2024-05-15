class Lamp:
    def _init_(self, state=False):
        self.state = state


    def alterar_state(self):
        self.state = True


lamp = Lamp()


print(lamp.state)
lamp.alterar_state()
print(lamp.state)