import locale
from datetime import datetime

locale.setlocale(locale.LC_ALL, 'pt_BR')

def retorna_data_extenso(data_string):
    try:
        datetime.strptime(data_string, '%d/%m/%Y')
    except ValueError:
        print("Formato de data inválido, deve ser DD/MM/AAAA")
        return None
    else:
        data_datetime = datetime.strptime(data_string,'%d/%m/%Y')
        return datetime.strftime(data_datetime, '%d de %B de %Y')

    #dia = datetime.strftime(data_datetime, '%d')
    #mes = datetime.strftime(data_datetime, '%B')
    #ano = datetime.strftime(data_datetime, '%Y')
    #return dia + " de " + mes[0].upper() + mes[1:] + " de " + ano
    #return dia + " de " + mes.capitalize() + " de " + ano

data = input("Digite uma data no formato DD/MM/AAAA:")
data_extenso = retorna_data_extenso(data)

if data_extenso is not None:
    print(data_extenso)

# Lista com os meses por extenso
meses = [
    "janeiro", "fevereiro", "março", "abril", "maio", "junho",
    "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
]

# Lista para armazenar as datas convertidas
datas_convertidas = []

def valida_data(data_str):
    """Função para validar se uma data está no formato DD/MM/AAAA."""
    try:
        dia, mes, ano = map(int, data_str.split('/'))
        if 1 <= dia <= 31 and 1 <= mes <= 12 and ano >= 0:
            return dia, mes, ano
    except ValueError:
        pass
    return None

def converte_data(dia, mes, ano):
    """Função para converter a data no formato DD/MM/AAAA para DD de mês por extenso de AAAA."""
    mes_extenso = meses[mes - 1]
    data_extenso = f"{dia} de {mes_extenso} de {ano}"
    datas_convertidas.append(data_extenso)
    return data_extenso

def pedir_data():
    """Função para pedir uma data válida ao usuário."""
    while True:
        data_str = input("Digite a data (DD/MM/AAAA): ")
        data = valida_data(data_str)
        if data:
            return data
        else:
            print("Data inválida. Por favor, digite novamente.")

def listar_datas():
    """Função para listar todas as datas convertidas por extenso."""
    if datas_convertidas:
        print("\nDatas convertidas:")
        for data in datas_convertidas:
            print(data)
    else:
        print("\nNenhuma data convertida.")

def gravar_datas_arquivo(nome_arquivo):
    """Função para gravar as datas convertidas em um arquivo."""
    try:
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            for data in datas_convertidas:
                arquivo.write(data + "\n")
        print(f"Datas gravadas no arquivo '{nome_arquivo}' com sucesso.")
    except Exception as e:
        print(f"Erro ao gravar o arquivo: {e}")

def menu():
    """Função para exibir o menu de opções e obter a escolha do usuário."""
    print("""
    1 - Converter Data
    2 - Listar Datas por extenso
    3 - Gravar Datas em Arquivo
    4 - Sair
    """)
    while True:
        try:
            opcao = int(input("Escolha uma opção: "))
            if 1 <= opcao <= 4:
                return opcao
        except ValueError:
            pass
        print("Opção inválida. Por favor, digite um número entre 1 e 4.")

def main():
    """Função principal do programa."""
    while True:
        opcao = menu()
        if opcao == 1:
            dia, mes, ano = pedir_data()
            data_extenso = converte_data(dia, mes, ano)
            print(f"Data por extenso: {data_extenso}")
        elif opcao == 2:
            listar_datas()
        elif opcao == 3:
            nome_arquivo = input("Digite o nome do arquivo para gravar as datas: ")
            gravar_datas_arquivo(nome_arquivo)
        elif opcao == 4:
            print("Saindo do programa...")
            break

if "_name_" == "_main_":
    main()









