# Função para verificar se um número é primo
def verificar_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Solicitar número ao usuário
numero = int(input("Digite um número para verificar se é primo: "))

# Verificar se o número é primo e exibir resultado
if verificar_primo(numero):
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")
