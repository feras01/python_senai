
# # numero1 = 10
# # numero2 = 10

# # # Operador maior
# # print(numero1 > numero2)
# # print(numero2 > numero1)

# # #operador menor
# # print (numero1 < numero2)
# # print (numero2 < numero1)

# # print(numero1 == numero2)

# # print(numero1 == numero2)
# # print(numero1 >= numero2)
# # print(numero1 <= numero2)
# # print(numero1 != numero1)

# #Variavéis = > <

# #int tipos inteiros
# #float
# # str
# #  


# # idade = int(input('Informe sua idade: \n'))

# # if (idade > 120):
# #     print('idade invalida')
# # elif(idade >= 18):
# #     print('maior de idade')
# #     elif (idade < 0):
# #         print('ainda não nasceu')
# # else:

# # Verdadeiro ou Falso, sim ou não


# # idade = int(input('Informe sua idade: \n'))

# # if (idade >= 18):
# #     print('Pode assitir o Filme')
# # elif(idade >= 16):
# #     acompanhado =input('Eta acompanhado de adulto SIM OU NÃO? \n')
# #     if (acompanhado == 'sim'):
# #       print('pode assistir')
# #     else:
# #         print('não pode assistir')
# # else:
# #     print('não pode assistir')


# # idade = int(input('Informe sua idade: \n'))

# # if(idade < 18):
# #    acompanhado =input('Eta acompanhado de adulto SIM OU NÃO? \n')
# #     if(acompanhado == 'sim'):
# #         print('pode assistir')
# #     else:
# #         print('pode assistir')
# #         else:
# #     print('não pode assistir')
# #     else:
# #         print('pode assitir')


# # usando variavel AND

# # alladin = input('Alladin apareceu? \n')
# # jasmine = input('jasmine apareceu? \n')

# # if (alladin == 'sim') and (jasmine =='sim'):
# #     print('Love a noite inteira')
# # else:
# #     print('não rolou encontro')


# # usando variavel or

# # alladin = input ('Alladin apareceu? \n')
# # jasmine = input ('jasmine apareceu? \n')

# # if (alladin) == 'sim' or (jasmine == 'não')
# # print ('sim tever encontro')



# alladin = input('Alladin apareceu? \n')
# jasmine = input('jasmine apareceu? \n')

# if (alladin == 'sim') or (jasmine =='sim'):
#      print('Love a noite inteira com outra')
# else:
#      print('não rolou encontro')



     



# Aula06

# candidato = int(input('informe o numero do candidato'))

# if candidato ==13:
#     print('voltou no lula')
# elif candidato == 22:
#      print('voltou no Bolsonaro')
# else
# print('Candidato invalido')


candidato = int(input('informe o numero do candidato \n'))

match candidato:
     case 13:
          print("voltou no Lula")
     case 22:
          print('voltou no Bolsonaro')
     case _:
          print('opção invalida')