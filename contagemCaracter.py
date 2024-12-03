# Função para contar caracteres
def contar_caracteres(s):
    contador = {}
    for char in s:
        if char in contador:
            contador[char] += 1
        else:
            contador[char] = 1
    return contador

# Solicitar string ao usuário
texto = input("Digite um texto: ")

# Contar caracteres e exibir resultado
resultado = contar_caracteres(texto)
print("Contagem de caracteres:")
for char, count in resultado.items():
    print(f"{char}: {count}")
