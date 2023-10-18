# Solicita ao usuário um número inteiro
numero_inserido = int(input("Digite um número inteiro: "))

# Verifica se o número é positivo
if numero_inserido <= 0:
    print("Por favor, insira um número inteiro positivo.")
else:
    print(f"Números ímpares de 1 até {numero_inserido}:")
    for numero in range(1, numero_inserido + 1, 2):
        print(numero)
