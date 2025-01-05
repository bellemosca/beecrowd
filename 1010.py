codigo_peca1, n_pecas1, valor_peca1 = map(
    lambda x: float(x) if "." in x else int(x), input().split()
)

codigo_peca2, n_pecas2, valor_peca2 = map(
    lambda x: float(x) if "." in x else int(x), input().split()
)

total = (n_pecas1 * valor_peca1) + (n_pecas2 * valor_peca2)

print(f"VALOR A PAGAR: R$ {total:.2f}")
