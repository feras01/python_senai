# from xml.dom.minidom import Element


# cavaleiros = ['seya', 'Aldebaran', 'shum', 'shiryu', 'yoga',]

# print(cavaleiros)
# # adiciona um novo elemento ao final da lista
# cavaleiros.append('Ikki')

# print(cavaleiros)

# # externdendo a lista com outra lista
# cavaleiros.extend(['shina', 'Mary'])
# print(cavaleiros)


# # inserir na lista em uma posição especifica

# cavaleiros.insert(0,'Athena')
# print(cavaleiros)

# # remove, exclui um elemento pelo valor.

# cavaleiros.remove('shina')
# print(cavaleiros)

# #pop - exclui o ultimo elemento da lista ou o indice informado
# elemento = cavaleiros.pop()
# cavaleiros.pop(0)
# print(cavaleiros)
# print(elemento)

# # metado de# indice - retona o indice da primeira ocorrencia de um valor procurado
# print(cavaleiros.index('yoga'))
# cavaleiros.pop(cavaleiros.index('yoga'))
# print(cavaleiros)

# # Alterando o valor de um elemento da lista 
# cavaleiros[cavaleiros.index('Ikki')] = 'Ikki de Fenix'
# print(cavaleiros)

# # contabilizando quantidade de elementos repetidos

# print(cavaleiros.count('Aldebaran'))

#  sort ordena a lista de forma crescente

from os import ftruncate


frutas = ['morango', 'maça', 'banana', 'abacaxi', 'amora', 'umbu', 'laranja']

numero = [9, 5, 81, 100, 33, 21, 2]

frutas.sort()
numero.sort()

print(frutas)
print(numero)

frutas.reverse()
numero.reverse()
print(frutas)
print(numero)

del frutas[-1]
print(frutas)

frutas.clear()
print(frutas)