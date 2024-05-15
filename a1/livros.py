def _init_(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.livros = []  # Lista para armazenar múltiplos livros

    def adicionar_livro(self, novo_livro):
        self.livros.append(novo_livro)  # Adiciona um novo livro à lista

    def listar_livros(self):
        for livro in self.livros:
            print(f"{livro.titulo}, {livro.autor}, {livro.ano}")

    def get_titulo(self):
        return self.titulo
    
    def get_autor(self):
        return self.autor
    
    def get_ano(self):
        return self.ano

# Uso das classes
meus_livros = Livro("1984", "George Orwell", 1949)  # Cria uma instância de Livro
meus_livros.adicionar_livro(Livro("A Revolução dos Bichos", "George Orwell", 1945))
meus_livros.listar_livros()