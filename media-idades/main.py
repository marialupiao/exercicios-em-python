idade: int
nPessoas: int
soma: float
media: float

print("Digite as idades: ")
idade = int(input())

if idade < 0:
    print("IMPOSSIVEL CALCULAR")
else:
    soma = 0
    nPessoas = 0
    while idade >= 0:
        soma = soma + idade
        nPessoas = nPessoas + 1
        idade = int(input())

    media = soma / nPessoas

    print(f"MEDIA = {media:.2f}")