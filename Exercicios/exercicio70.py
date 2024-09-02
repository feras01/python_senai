import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    
    if response.status_code == 200:
        dados = response.json()
        if "erro" in dados:
            return None
        return dados
    else:
        return None

def gerar_relatorio(dados):
    relatorio = f"""
    Relatório de Endereço
    =====================
    CEP: {dados['cep']}
    Logradouro: {dados['logradouro']}
    Bairro: {dados['bairro']}
    Cidade: {dados['localidade']}
    Estado: {dados['uf']}
    =====================
    """
    return relatorio

def main():
    while True:
        cep = input("Digite o CEP para consulta (somente números): ").strip()

        if not cep.isdigit() or len(cep) != 8:
            print("CEP inválido! Tente novamente.")
            continue

        dados = consultar_cep(cep)

        if dados is None:
            print("CEP não encontrado ou inválido! Tente novamente.")
            continue

        relatorio = gerar_relatorio(dados)
        print(relatorio)

        nova_consulta = input("Deseja realizar outra consulta? (s/n): ").strip().lower()
        if nova_consulta != 's':
            print("Encerrando o sistema.")
            break

if __name__ == "__main__":
    main()