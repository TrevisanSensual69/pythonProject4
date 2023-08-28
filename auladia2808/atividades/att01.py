class Pessoa:
    def _init_(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")


pessoa1 = Pessoa("João", 25)
pessoa2 = Pessoa("Maria", 30)

pessoa1.saudacao()
pessoa2.saudacao()