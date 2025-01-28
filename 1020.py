idade_pessoa_dias = int(input())

anos = idade_pessoa_dias // 365
resto_dias = idade_pessoa_dias % 365
meses = resto_dias // 30
dias = resto_dias % 30

print(f"{anos} anos(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")
