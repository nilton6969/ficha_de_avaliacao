n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

print("---- Operações ----")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("---- Operações -----")

opcoes = int(input("Escolha a operação (1-4): "))

match opcoes:
    case 1:
        resultado = n1 + n2
        print(n1, "+", n2, "=", resultado)
    case 2:
        resultado = n1 - n2
        print(n1, "-", n2, "=", resultado)
    case 3:
        resultado = n1 * n2
        print(n1, "*", n2, "=", resultado)
    case _: 
        resultado = n1 / n2
        print(n1,"/", n2, "=",  resultado )
