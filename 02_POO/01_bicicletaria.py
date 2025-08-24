class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("pling plig")

    def parar(self):
        print("Parando bicicleta...")
        print("Biciclet parada!")

    def correr(self):
        print("Vrummmmmmmmmmmm")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{key}={value}' for key, value in self.__dict__.items()])}"

b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar()
print()
b1.correr()
print()
b1.parar()
print()

print(b1.cor, b1.modelo, b1.ano, b1.valor)


b2 = Bicicleta("verde", "monark", 200, 189)
b2.buzinar()  # Bicicleta.buzinar(b2)

print()
print(b2)