# # Desenvolva um algoritmo que pergunte ao usuário o estado civil (solteiro, casado, divorciado, viúvo) e exiba uma mensagem correspondente.

# def exibir_mensagem_estado_civel():
#     estado_civil = input('Digite seu estado civil (solteiro, casado, divorciado, viúvo): ').strip().lower()

#     if estado_civil == 'solteiro':
#         mensagem = 'você esta solteiro'
#     elif estado_civil == 'casado':
#         mensagem = 'você esta casa'
#     elif estado_civil == 'divorciado':
#             mensagem = 'você esta divorciado'
#     elif estado_civil == 'viuvo':
#         mensagem = 'você esta viuvo'

#     else:  
#         mensagem = 'Estado civil inválido: Por favor, insira um dos seguintes: solteiro, casado, divorciado, viúvo.'

# print('mensagem')
#  exibir_mensagem_estado_civil()























def exibir_mensagem_estado_civil():
    # Solicita ao usuário que insira seu estado civil
    estado_civil = input("Digite seu estado civil (solteiro, casado, divorciado, viúvo): ").strip().lower()

    # Determina a mensagem correspondente ao estado civil
    if estado_civil == "solteiro":
        mensagem = "Você está solteiro."
    elif estado_civil == "casado":
        mensagem = "Você está casado."
    elif estado_civil == "divorciado":
        mensagem = "Você está divorciado."
    elif estado_civil == "viúvo":
        mensagem = "Você está viúvo."
    else:
        mensagem = "Estado civil inválido. Por favor, insira um dos seguintes: solteiro, casado, divorciado, viúvo."

    # Exibe a mensagem correspondente
    print(mensagem)

# Chama a função para executar o programa
exibir_mensagem_estado_civil()
