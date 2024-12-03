# Função para calcular a média
def calcular_media(a, b, c):
    return (a + b + c) / 3

# Solicitar números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Calcular e mostrar a média
media = calcular_media(num1, num2, num3)
print(f"A média dos três números é: {media}")
