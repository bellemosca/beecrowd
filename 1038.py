valor_cod, qta = map(int, input().split())

codigo = [1, 2, 3, 4, 5]
preco = [4.0, 4.5, 5.0, 2.0, 1.5]

if valor_cod in codigo:
    total = preco[codigo.index(valor_cod)] * qta
    print(f"Total: R$ {total:.2f}")

else:
    print("Valores não cadastrados")
