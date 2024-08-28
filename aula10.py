# # funcoes python
# numeros = [1, 5, 8, 10, 3, 78, 100, 51]
# print(max(numeros))
# print(min(numeros))
# print(len(numeros))
# print(sum(numeros))

# juntando funcoes: media dos numeros
## media = sum(numeros) / len(numeros)
## print(media)

# # criando minha propria funcao:

# def media (numeros):
#     resultado = sum(numeros) / len(numeros)
#     return resultado
# resposta = media(numeros)
# print(resposta)

# def soma (numero1, numero2):
#     soma = numero1 + numero2
#     return soma
# print(soma(15, 35))

# # funcao sem retorno:
# def saudacao(nome):
#     print(f'Olá {nome}')
# saudacao('Luana')

# # funcao com parametro opcional
# def ola(nome, mensagem = 'Olá'):
#     print(mensagem, nome)
# ola('Luana')
# ola('Luana', 'oi')

# funcao com multiplo retorno
# def dividir (numero1, numero2):
#     resposta = numero1 // numero2
#     resto = numero1 % numero2
#     return resposta, resto

# divisao, resto_divisao = dividir(9,2)
# print(divisao)
# print(resto_divisao)

# numeros = (1, 5, 8, 10, 3, 78, 100, 51)
# print(type(numeros))

# # funcao lambda
# def soma (numero1, numero2):
#     soma = numero1 + numero2
#     return soma

# somar = lambda numero1, numero2: numero1 + numero2
# print(somar(10,5))

# # parametro posicional
# def exibir_informacoes(*args):
#     print('Argumentos posicionais: ', args)
# exibir_informacoes(1,4,'Luana', 'Teste')


# def exibir_informacoes2(**args):
#     print('Argumentos nomeados: ', args)
# exibir_informacoes2(nome = 'luana', idade = 18, curso = 'python')

# key : value

pessoas =[{
    'nome': 'Luana',
    'idade': 18,
    'estado_civil': 'solteiro',
    'escolaridade': 'medio'
},
{
    'nome': 'Daniel',
    'idade': 19,
    'estado_civil': 'solteiro',
    'escolaridade': 'medio'
}]

print(pessoas[1])