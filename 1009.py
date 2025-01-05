vendedor = str(input()).upper()
salario = float(input())
vendas_efetuadas = float(input())

comissao = salario + (vendas_efetuadas * 0.15)

print(f"TOTAL = R$ {comissao:.2f}")
