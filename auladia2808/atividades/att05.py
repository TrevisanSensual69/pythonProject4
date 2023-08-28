class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_media(self):
        return (self.nota1 + self.nota2) / 2

aluno1 = Aluno("Carlos", 8.5, 7.2)
media_aluno1 = aluno1.calcular_media()
print(f"A média do aluno {aluno1.nome} é: {media_aluno1:.2f}")
