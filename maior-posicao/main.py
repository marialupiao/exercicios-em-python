n: int
posMaior: int
maior: float

n = int(input("Quantos numeros voce vai digitar? "))

vet = [0 for x in range(n)]

for i in range(n):
    vet[i] = float(input("Digite um numero: "))

maior = vet[0]
posMaior = 0

for i in range(n):
    if vet[i] > maior:
        maior = vet[i]
        posMaior = i

print(f"\nMAIOR VALOR = {maior:.1f}")
print(f"POSICAO DO MAIOR VALOR = {posMaior}")