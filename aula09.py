import string


texto = 'Flavio Marques Rodrigues  '

texto2 = texto.capitalize()
# capitalize muda o primeiro caracter da string para maiusculo

print(texto.capitalize())
print(texto2)

# lower padroniza a string em minusculo 

nome = 'FlAviO MaRquEs RoDriGues'
nome2 = 'flavio marques rodrigues'
print(nome.lower())


if nome.lower() == nome2.lower():
    print('são iguais')
else:
    print('não são iguais')

# UPPER padroniza uma string em maiusculo

print(nome.upper())

#replace muda um padrão de caracteres de um string

silvano_sales = 'coração coração cabeção'

# silvano_sales2 = silvano_sales.replace('ç', 'c')
# silvano_sales2 = silvano_sales2.replace('ã', 'a')

print(silvano_sales.replace('cã', 'ca'))

# strip é uma forma de remove caracteres em branco no final e no inicio e uma string
# usando muito em banco de dados


jack_stripador ='        removendo espaços de uma string       '
print(jack_stripador)
print(jack_stripador.strip())

# split divide uma string em base de espaços == elementos de uma lista

string_espalhada = 'Flavio Marques Rodrigues'

print(string_espalhada)
print(string_espalhada.split())

# join transforma os elementos de uma lista de uma string
# concatena strings

nome_listas = ['flavio', 'marques', 'rodrigues']

print('-'.join(nome_listas))

dominio = 'aluno.senai.br'
print('flavio.marques'+(dominio))

# slice manipula string por indice

cidade = 'Ceilandia, cidade do povo sem futuro'

print(cidade[::-1])



# exer32 usando string por indice -- slice 


palindromo = 'Arara'

if palindromo.lower == palindromo[::-1].upper():
    print('e palindromo')
else:
    print('não é palindromo')