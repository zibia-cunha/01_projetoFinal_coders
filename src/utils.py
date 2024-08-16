import json
from datetime import datetime
data_atual = datetime.now()
data_atual_formatada = data_atual.strftime('%d/%m/%Y')


def incluir_de_csv(path, **parametros):
    """
    inclui um registro manualmente

    Returns:
        tipo (str): tipo de movimentação
        valor (float): valor da movimentação
        data (str): data da movimentação
    """
    pass


def incluir_registros_base_dados(base_dados):
    """
    Inclui registros na base de dados com um identificador único.
    """
    arquivo = 'base_dados.json'
    try:
        with open(arquivo, 'r') as file:
            base_dados = json.load(file)
    except FileNotFoundError:
        base_dados = {}

    tipo_de_registros = {1: 'Receita', 2: 'Despesas', 3: 'Investimento'}

    while True:
        for chave, descricao in tipo_de_registros.items():
            print(f"{chave}. {descricao}")

        registro = input("\nQual o tipo de registro deseja inserir? ")

        if registro.isdigit() and int(registro) in tipo_de_registros:
            data_atual = datetime.today().strftime('%d/%m/%Y')
            valor = float(input(f"Digite o valor de {tipo_de_registros[int(registro)]} que deseja inserir:"))

            if tipo_de_registros[int(registro)] == 'Despesas':
                valor = -abs(valor)  

            
            id_registro = len(base_dados) + 1

            
            while str(id_registro) in base_dados:
                id_registro += 1

            
            base_dados[id_registro] = {
                'Data': data_atual,
                'Tipo': tipo_de_registros[int(registro)],
                'Valor': valor
            }

            print("*" * 60)
            print(f"Registro de {tipo_de_registros[int(registro)]}, no valor de {valor} cadastrado com sucesso")
            print("*" * 60)

            continuarCadastro = input("\nDeseja continuar cadastrando registros? S/N ")
            if continuarCadastro.upper() != "S":
                break
        else:
            print("Opção inválida")


    with open(arquivo, 'w') as file:
        json.dump(base_dados, file, indent=4)

    print(f"Dados salvos no arquivo '{arquivo}'.")

    return base_dados


def criar_registro_movimentacao(parametros: dict, database_path="database"):
    """
    Cria um registro de movimentação

    Parameters:
        parametros (dict): dicionário com os parâmetros da movimentação
        database_path (str): caminho do banco de dados

    """
    pass


def listar_movimentacoes(database_path="database"):
    """
    Lista as movimentações

    Parameters:
        database_path (str): caminho do banco de dados

    Returns:
        movimentacoes (list): lista de movimentações
    """
    pass


def calcular_rendimento(taxa: float = 0.003,
                        valor: float = 1580,
                        data_anterior=datetime(2005, 4, 6),
                        data_atual=datetime(2022, 1, 5)):
    """
    Cálculo do rendimento de investimento
    M = C * (1 + i)^t
    t = contar_dias_entre_datas(data_anterior, data_atual)

    Parameters:
        taxa (float): taxa de rendimento
        valor (float): valor investido
        data_anterior (datetime): data do investimento anterior
        data_atual (datetime): data atual

    Returns:
        rendimento (float): rendimento do investimento
    """
    
    # Calcula a diferença em dias entre as duas datas
    dias = (data_atual - data_anterior).days

    # Calcula o montante final M = C * (1 + i)^t
    montante = valor * (1 + taxa) ** dias

    # O rendimento é a diferença entre o montante final e o valor inicial
    rendimento = montante - valor

    return rendimento

# Chamando a função
rendimento = calcular_rendimento()
print(f"Rendimento do investimento: R${rendimento:.2f}")


def deletar_registro(indice: int, tipo: str,
                     database_path: str):
    """
    Determina o tipo de movimentação e deleta o registro correspondente ao indice

    Parameters:
        indice (int): indice do registro a ser deletado
        tipo (str): tipo de movimentação
        database_path (str): caminho do banco de dados
    """


def atualizar_registro(dicionario):
    identificador = input('insira o identificador')
    if identificador in dicionario:
        novo_tipo = input('Insira o novo tipo: ').capitalize()
        dicionario[identificador]['Tipo'] = novo_tipo
        novo_valor = float('Insira o novo valor: ')
        dicionario[identificador]['Valor'] = novo_valor
        
        dicionario[identificador]['Data'] = datetime.now().strftime('%d/%m/%Y')
        return f"Registro {identificador} atualizado com sucesso."
    else:
        return f"Registro {identificador} não encontrado."


def agrupar_movimentacoes(movimentacoes, agrupar_por):
    """
    agrupa movimentações por tipo

    """


def exportar_relatorio_json(movimentacoes, formato='json', nome_arquivo='relatorio'):
    """
    exporta relatório de movimentações para um arquivo json

    Parameters:
        movimentacoes (list): lista de movimentações
        formato (str): formato do arquivo
        nome_arquivo (str): nome do arquivo
    """


def exportar_relatorio_csv(movimentacoes, formato='csv', nome_arquivo='relatorio'):
    """
    exporta relatório de movimentações para um arquivo csv

    Parameters:
        movimentacoes (list): lista de movimentações
        formato (str): formato do arquivo
        nome_arquivo (str): nome do arquivo
    """
