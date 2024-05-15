def _init_(self, nome, senha):
        self.__nome = nome
        self.__senha = senha
        
    def alterar_senha(self, nova_senha):
        self.__senha = nova_senha
    	
    def get_senha(self):
    	return self.__senha


usuario = Usuario("joao123", "senha123")
usuario.alterar_senha("novaSenha123")