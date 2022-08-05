n: int
homens: int
mulheres: int
menor: float
maior: float
media: float
total: float

n = int(input("Quantas pessoas serao digitadas? "))

altura = [0 for x in range(n)]
genero = [0 for x in range(n)]

for i in range(n):
    altura[i] = float(input(f"Altura da {i+1}a pessoa: "))
    genero[i] = str(input(f"Genero da {i+1}a pessoa: "))

menor = altura[0]
maior = altura[0]

for i in range(n):
    if altura[i] > maior:
        maior = altura[i]
    if altura[i] < menor:
        menor = altura[i]

homens = 0
mulheres = 0
total = 0

for i in range(n):
    if genero[i] == 'M':
        homens = homens + 1
    else:
        mulheres = mulheres + 1
        total = total + altura[i]

media = total / mulheres

print(f"Menor altura = {menor:.2f}")
print(f"Maior altura = {maior:.2f}")
print(f"Media das alturas das mulheres = {media:.2f}")
print(f"Quantidade de homens = {homens}")
