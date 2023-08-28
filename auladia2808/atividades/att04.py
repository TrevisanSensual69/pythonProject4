class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

meu_retangulo = Retangulo(5, 8)
area = meu_retangulo.calcular_area()
print(f"A área do retângulo é: {area}")
