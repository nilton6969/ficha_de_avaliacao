numero = int(input("Digite um número : "))

if numero == 1 :
   print ("O nº digitado foi 1")
elif numero == 2 :
   print ("Eu sei o número digitado,")
   print ("o dígito foi 2 ")
elif numero in [3,4]:
   print ("O nº digitado foi 3 ou 4 ")
elif numero in [5,6,7,8,9,10]:
   print ("O nº digitado está entre 5 e 10 ")
else:
   print ("O nº digitado não está entre 1 e 10 ")
