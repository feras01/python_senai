# Aula06

# candidato = int(input('informe o numero do candidato'))

# if candidato ==13:
#     print('voltou no lula')
# elif candidato == 22:
#      print('voltou no Bolsonaro')
# else
# print('Candidato invalido')

# match case uma estrutara condicional, alternatica ao if
# abaixo verifica o 


# candidato = int(input('informe o numero do candidato \n'))

# match candidato:
#      case 13:
#           print("voltou no Lula")
#      case 22:
#           print('voltou no Bolsonaro')
#      case _:
#           print('opção invalida')



# atribuição de valores a uma variavel

# numero = 10
# numero += 10
# print(numero)

# #numero = numero + 10
# print(numero)

# #numero = numero - 10
# numero -= 10
# print(numero)

# #numero = numero * 10
# numero *= 10
# print(numero)

# #numero = numero / 10
# numero /= 10
# print(numero)


# Verificando se o numero é par ou impar

# numero = int(input('informe o numero\n'))

# if numero % 2 == 0:
#      print('numero e par')
# else:
#      print('numero e impar'





# laços de repetição em portugues 'para'

# for i in range(5):
#      print(i)


# nomes = ['Flavio', 'Andriana', 'Janaina']
# print(nomes)

# for  nome in nomes:
#      print(nome)


# frutas = ['maça, morango, laranja, limão, manga']

# for indice, fruta in enumerate(frutas):
#     print(f'Suas frutas são {indice}: {fruta} ')


# nomes = []
# for i in range(5):
#      nome = input('Informe seu nome: /n')
#      nomes.append(nome)

# for nome in nomes:
#      print(nome)


# nome = 'Flavio'

# for i in nome:
#      print(i)



 # While em português enqueto
# numero = None

# while numero != 0:
#      numero = int(input('informe o numero'))

# contador = 1
# numero = int(input('informe o numero: '))
# while contador < 10:
#      print(numero * 2)
#      contador +=1


# numero = 10
# while True:
#     numero *= 10
#     print(numero)



numero = 10
while True:
    numero *= 10
    print (numero)
    if numero > 100000:
          break