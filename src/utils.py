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
    Inclui registros na base de dados
    """
    tipo_de_registros = {1: 'Receita', 2: 'Despesas', 3: 'Investimento'}

    for chave, descricao in tipo_de_registros.items():
        print(f"{chave}. {descricao}")

    registro = input("\nQual o tipo de registro deseja inserir? ")

    if registro.isdigit() and int(registro) in tipo_de_registros:
        data_atual = datetime.today().strftime('%d/%m/%Y')
        valor = float(input(f"Digite o valor de {
                      tipo_de_registros[int(registro)]} que deseja inserir:"))

        if tipo_de_registros[int(registro)] == 'Despesas':
            valor = -abs(valor)  # Armazena como negativo

        if data_atual not in base_dados:
            base_dados[data_atual] = {'Registros': {
                'Receita': 0, 'Despesas': 0, 'Investimento': 0}}

        tipo_registro = tipo_de_registros[int(registro)]
        base_dados[data_atual]['Registros'][tipo_registro] += valor

        print("*" * 60)
        print(f"Registro de {tipo_registro}, no valor de {
              valor} cadastrado com sucesso")
        print("*" * 60)

        continuarCadastro = input(
            "\nDeseja continuar cadastrando registros? S/N ")
        if continuarCadastro.upper() == "S":
            incluir_registros_base_dados(base_dados)
    else:
        print("Opção inválida")

    # criar_registro_movimentacao(base_dados)

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
                        valor: float = 0,
                        data_anterior=None,
                        data_atual=None):
    """
    Cálculo do rendimento de investimento
    M = C * (1 + i)^t
    t = contar_dias_entre_datas(data_anterior,data_atual)

    Parameters:
        taxa (float): taxa de rendimento
        valor (float): valor investido
        data_anterior (datetime): data do investimento anterior
        data_atual (datetime): data atual

    Returns:
        rendimento (float): rendimento do investimento
    """


def deletar_registro(indice: int, tipo: str,
                     database_path: str):
    """
    Determina o tipo de movimentação e deleta o registro correspondente ao indice

    Parameters:
        indice (int): indice do registro a ser deletado
        tipo (str): tipo de movimentação
        database_path (str): caminho do banco de dados
    """


def atualizar_registro(indice: int,
                       tipo: str,
                       database_path: str,
                       data=datetime.today().strftime('%d/%m/%Y'),
                       **parametros):
    """
    atualiza o valor ou o tipo de uma movimentação com base na data de registro

    Parameters:
        dia (int): dia da movimentação
        mes (int): mês da movimentação
        ano (int): ano da movimentação
        valor (float): valor da movimentação
        tipo (str): tipo da movimentação
    Returns:
    """


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
