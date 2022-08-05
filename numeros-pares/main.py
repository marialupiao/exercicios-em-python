n: int
qtd: int

n = int(input("Quantos numeros voce vai digitar? "))

vet = [0 for x in range(n)]

for i in range(n):
    vet[i] = int(input("Digite um numero: "))


print(f"\nNUMEROS PARES: ")

qtd = 0

for i in range(n):
    if vet[i] % 2 == 0:
        print(f"{vet[i]}  ", end="")
        qtd = qtd + 1

print(f"\n\nQUANTIDADE DE PARES = {qtd}")