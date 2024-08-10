

def incluir_de_csv(path, **parametros):
    """
    inclui um registro manualmente

    Returns:
        tipo (str): tipo de movimentação
        valor (float): valor da movimentação
        data (str): data da movimentação
    """ 
    pass

def incluir_registros_base_dados(**parametros):
    """
    inclui registros na base de dados
    """ 
    pass

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

def calcular_rendimento(taxa: float=0.003, 
                        valor: float=0, 
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
                       data=datetime.datetime.today(),
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