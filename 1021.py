valor = float(input())
valor = round(valor * 100)

notas = [10000, 5000, 2000, 1000, 500, 200]
moedas = [100, 50, 25, 10, 5, 1]

print("NOTAS:")
for nota in notas:
    quantidade = valor // nota
    if quantidade >= 0:
        print(f"{quantidade:.0f} nota(s) de R$ {nota/100:.2f}")
    valor %= nota


print("MOEDAS:")
for moeda in moedas:
    quantidade = valor // moeda
    if quantidade >= 0:
        print(f"{quantidade:.0f} moeda(s) de R$ {moeda/100:.2f}")
    valor %= moeda
