import math

def calcular_raizes(a, b, c):
    delta = b ** 2 - 4 * a * c

    if delta < 0:
        print("Esta equação não possui raízes reais")
    elif delta == 0:
        raiz_dupla = -b / (2 * a)
        print(f"A raiz desta equação é {raiz_dupla}")
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)

        if raiz1 < raiz2:
            print(f"As raízes da equação são: {raiz1} e {raiz2}")
        else:
            print(f"As raízes da equação são: {raiz2} e {raiz1}")

# Entrada dos parâmetros
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

# Chamada da função para calcular e imprimir as raízes
calcular_raizes(a, b, c)
