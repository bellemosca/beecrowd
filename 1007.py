a = int(input())
b = int(input())
c = int(input())
d = int(input())

diferenca = (a * b) - (c * d)

print(f"DIFERENCA = {diferenca}")

# outra resolução melhorada para o problema

""" def ler_inteiro(mensagem):
    while True:
        try:
            # Tenta converter a entrada para um número inteiro
            return int(input(mensagem))
        except ValueError:
            # Exibe uma mensagem de erro e repete a solicitação
            print("Entrada inválida. Por favor, digite um número inteiro.")

# Solicita os valores
a = ler_inteiro("Digite o valor de A: ")
b = ler_inteiro("Digite o valor de B: ")
c = ler_inteiro("Digite o valor de C: ")
d = ler_inteiro("Digite o valor de D: ")

# Exibe os valores
print("Os valores digitados foram:")
print(a, b, c, d)
 """
