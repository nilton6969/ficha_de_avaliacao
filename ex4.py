print("--------------------------")
print("-----------Menu-----------")
print("--------------------------")
print(" Opção 1 - Viagem a Paris ")
print(" Opção 2 - Viagem a Paris/Alojamento ")
print(" Opção 3 - Viagem a Paris/Alojamento/Alimentação ")
print(" Opção 4 - Viagem a Paris/Alojamento/Museus ")


viagens = int(input("Escolha uma das opções meu caro cliente :"))

alimentaçao = 150
alojamneto = 250
viagem = 800
museus = 50
preco_total = 0

match viagens :
    case 1:
     preco_total = viagem
    case 2:
     preco_total = viagem + alojamneto
    case 3:
     preco_total = viagem + alojamneto + alimentaçao
    case 4:
     preco_total = viagem + alojamneto + museus


print("Você gastou {}€" .format(preco_total))
