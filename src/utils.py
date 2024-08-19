#%%
from datetime import *
import os
import csv
import random

#%%

def incluir_registros_base_dados(base_dados):
    """
    Inclui registros na base de dados com um identificador único (ID).

    """
    
    tipo_de_registros = {1: 'Receita', 2: 'Despesa', 3: 'Investimento'}

    for chave, descricao in tipo_de_registros.items():
        print(f"{chave}. {descricao}")

    registro = input("\nQual o tipo de registro deseja inserir? ")

    if registro.isdigit() and int(registro) in tipo_de_registros:
        data_atual = datetime.now()
        data_atual_formatada = data_atual.strftime('%d/%m/%Y')
        valor = float(input(f"Digite o valor de {tipo_de_registros[int(registro)]} que deseja inserir:"))

        if tipo_de_registros[int(registro)] in ['Receita', 'Despesa']:
            if tipo_de_registros[int(registro)] == 'Despesa':
                valor = -abs(valor)  

            # identificador único para cada registro
            id_registro = id_registro = len(base_dados) + 1

            # registro
            base_dados[id_registro] = {
                'Data': data_atual_formatada,
                'Tipo': tipo_de_registros[int(registro)],
                'Valor': valor,
                'Ano': data_atual.year,
                'Mes': data_atual.month,
                'Dia': data_atual.day
            }
        elif tipo_de_registros[int(registro)] == 'Investimento':
            taxa = float(input("Digite a taxa de rendimento do investimento: "))
            valor = abs(valor)
            id_registro = len(base_dados) + 1
            base_dados[id_registro] = {
                'Data': data_atual_formatada,
                'Tipo': tipo_de_registros[int(registro)],
                'Valor': valor,
                'Ano': data_atual.year,
                'Mes': data_atual.month,
                'Dia': data_atual.day,
                'Taxa': taxa}

        print("*" * 60)
        print(f"Registro de {tipo_de_registros[int(registro)]}, no valor de {valor} cadastrado com sucesso")
        print("*" * 60)

        continuarCadastro = input("\nDeseja continuar cadastrando registros? S/N ")
        if continuarCadastro.upper() == "S":
            incluir_registros_base_dados(base_dados)

    else:
        print("Opção inválida")
    return base_dados

def incluir_registros_de_arquivo_csv(path):
    """
    Lê um arquivo csv para manipulação dos dados

    """
    
    data = read_csv(path)
    regsitros = {}
    for nn, registro in enumerate(data):
        tipo = registro['Tipo de Transação']
        if tipo in ["Receita", "Despesa"]:
            valor = registro['Valor']
            data = registro['Data']
            regsitros[nn] = {'Data': data, 'Tipo': tipo, 'Valor': valor, "Ano": int(data.split('/')[0]), "Mes": int(data.split('/')[1]), "Dia": int(data.split('/')[2])}
        else:
            valor = registro['Valor']
            data = registro['Data']
            taxa = 0.003
            regsitros[nn] = {'Data': data, 'Tipo': tipo, 'Valor': valor, "Ano": int(data.split('/')[0]), "Mes": int(data.split('/')[1]), "Dia": int(data.split('/')[2]), "Taxa": taxa}

    return regsitros


def criar_registro_movimentacao(parametros: dict, database_path="database"):
    """
    Cria um registro de movimentação

    Parameters:
        parametros (dict): dicionário com os parâmetros da movimentação
        database_path (str): caminho do banco de dados

    """

    # # Validando se o valor é numérico e positivo
    # try:
    #     if valor < 0:
    #         raise ValueError(f'Valor {valor} inválido.')
    # except (TypeError, ValueError) as e:
    #     print(f'Valor {valor} inválido.',
    #           'O valor deve ser numérico e maior ou igual a 0.', sep='\n')

    # Parâmetros validados. Inserindo movimentação de acordo com o tipo.
    
    for registros in parametros:
        entrada = parametros[registros]
        tipo = entrada['Tipo'].lower()
        
        if tipo in ['receita', 'despesa']:
            identificador = int(retornar_ultimo_id(tipo=tipo, path=database_path)) + 1
            conteudo = [[f'{identificador:07d}', entrada['Data'], entrada['Tipo'],
                        entrada['Valor'], entrada['Ano'], entrada['Mes'], 
                        entrada['Dia']]]
            with open(f"{database_path}/movimentacoes.csv", 'a+', newline='') as file:
                writer = csv.writer(file, delimiter=',')

                writer.writerows(conteudo)
            print(f"Registro {conteudo} inserido com sucesso no arquivo {database_path}/movimentacoes.csv")
        elif tipo == 'investimento':
            if "Taxa" not in entrada:
                raise ValueError("Tipo de movimentacao investimento requer parametro taxa.")
            else:
                taxa = entrada["Taxa"]

            identificador = int(retornar_ultimo_id(tipo=tipo, path=database_path)) + 1
        
            # Nesse momento só insere no banco de dados, não calcula o rendimento. 
            # O rendimento é calculado no segundo passo, para todo o banco de dados.
            montante = 0
            rendimento = 0
            conteudo = [[f'{identificador:07d}', entrada['Data'], entrada['Tipo'],taxa,
                        entrada['Valor'], entrada['Ano'], entrada['Mes'], 
                        entrada['Dia'], montante, rendimento]]
            with open(f"{database_path}/investimentos.csv", 'a+', newline='') as file:
                writer = csv.writer(file, delimiter=',', lineterminator='\n')
                writer.writerows(conteudo)
            print(f"Registro {conteudo} inserido com sucesso no arquivo {database_path}/investimentos.csv")
        else:
            print('Tipo de movimentação inválida.',
                'Escolha entre: "receita", "despesa" ou "investimento"', sep='\n')


def listar_movimentacoes(database_path="./database"):
    """
    Lista as movimentações

    Parameters:
        database_path (str): caminho do banco de dados

    Returns:
        movimentacoes (list): lista de movimentações
    """

    tipo_de_registros = {1: 'Receita', 2: 'Despesa', 3: 'Investimento', 4: 'Geral'}

    for chave, descricao in tipo_de_registros.items():
        print(f"{chave}. {descricao}")
    tipo = input('Qual o tipo de registro que deseja listar? ')
    tipo_relatorio = tipo_de_registros[int(tipo)]

    if tipo_relatorio.lower() == 'geral':
        movimentacoes = read_csv(f'{database_path}/movimentacoes.csv')
        movimentacoes_com_taxa_e_redimento = []
        for reg in movimentacoes:
            novo_reg = {
               'id': reg['id'],
                'Data': reg['Data'],
                'Tipo': reg['Tipo'],
                'Taxa': 0,
                'Valor': reg['Valor'],
                'Ano': reg['Ano'],
                'Mes': reg['Mes'],
                'Dia': reg['dia'],
                'Montante': 0,
                'Rendimento': 0
            }

            movimentacoes_com_taxa_e_redimento.append(novo_reg)

        investimentos = read_csv(f'{database_path}/investimentos.csv')
        print_tabular_data(movimentacoes_com_taxa_e_redimento)
        print_tabular_data(investimentos)
        return movimentacoes_com_taxa_e_redimento + investimentos

    tipo_de_consulta = {1: 'Todos os Registos', 2: 'Data Específica'}
    for chave, descricao in tipo_de_consulta.items():
        print(f"{chave}. {descricao}")
    consulta = input("Quais registros deseja consultar? ")
    tipo_de_consulta = tipo_de_consulta[int(consulta)]

    if tipo_de_consulta == 'Todos os Registos':
        data = None
    elif tipo_de_consulta == 'Data Específica':
        data = input("Insira a data no formato dd/mm/aaaa: ")
    
    investimentos = read_csv(f'{database_path}/investimentos.csv')
    movimentacoes = read_csv(f'{database_path}/movimentacoes.csv')
    
    print(tipo_relatorio)
    print(movimentacoes)

    if data:
        if tipo_relatorio.lower() in ['receita', 'despesa']:
            registros = []
            for movimentacao in movimentacoes:
                if movimentacao['Tipo'].lower() == tipo_relatorio.lower() and movimentacao['Data'] == data:
                    registros.append(movimentacao)
            print_tabular_data(registros)
            return registros
        else:
            registros = []
            for movimentacao in investimentos:
                if movimentacao['Data'] == data:
                    registros.append(movimentacao)
            print_tabular_data(registros)
            return registros
    else:
        if tipo_relatorio.lower() in ['receita', 'despesa']:
            registros = []
            for movimentacao in movimentacoes:
                if movimentacao['Tipo'].lower() == tipo_relatorio.lower():
                    registros.append(movimentacao)
            print_tabular_data(registros)
            return registros
        else:
            print_tabular_data(investimentos)
            return investimentos


#%%
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


def atualizacao_do_rendimento(database="../database"):
    """
    Função que atualiza o rendimento dos investimentos. A função lê o arquivo 
    investimentos.csv, calcula o rendimento, e atualiza o arquivo.

    input:
        database (str): caminho do banco de dados
    """
    
    # retorna uma lista com os registros do arquivo investimentos.csv
    investimentos = read_csv(f'{database}/investimentos.csv')
    

    # loop para calcular o rendimento de cada investimento
    # e atualizar o montante
    # O for percorre os dados de inventimentos. O primeiro registro de investimento tera um rendimento igual
    # a 0, e o montante é igual ao valor investido.
    # A partir do segundo, o montante é a soma do montatne anteior com o novo valor investido e o rendimento
    # obtido no intervalo de tempo entre os dois registros.
    for indice, investimento in enumerate(investimentos):
        if indice == 0:
            investimentos[indice]["Rendimento"] = 0
            investimentos[indice]["Montante"] = investimentos[indice]["Valor"]
        else:
            ultimo_investimento = investimentos[indice-1]
            dia_anterior = datetime.strptime(ultimo_investimento["Data"], "%d/%m/%Y")
            dia_atual = datetime.strptime(investimento["Data"], "%d/%m/%Y")

            # calcula o rendimento com base no montante do registro anterior
            rendimento = calcular_rendimento(taxa=float(investimento["Taxa"]), 
                                             valor=float(ultimo_investimento["Montante"]),
                                            data_anterior=dia_anterior, data_atual=dia_atual)

            montante = round(float(ultimo_investimento["Montante"]) + float(investimento["Valor"]) + float(ultimo_investimento["Rendimento"]), 2)

            investimentos[indice]["Rendimento"] = round(rendimento, 2)
            investimentos[indice]["Montante"] = montante
    

    atualizar_base_csv(investimentos, tipo="investimento", path=database, nome_arquivo="investimentos.csv")
    
    print("Rendimento dos investimentos atualizado com sucesso.")

def deletar_registro(database_path):
    """
    Determina o tipo de movimentação e deleta o registro correspondente ao indice

    Parameters:
        indice (int): indice do registro a ser deletado
        tipo (str): tipo de movimentação
        database_path (str): caminho do banco de dados
    """
    indice = int(input('Insira o índice do registro a ser deletado: '))
    tipo = input('Insira o tipo de movimentação (receita, despesa ou investimento): ')

    if tipo.lower() in ['receita', 'despesa']:
        arquivo = "movimentacoes.csv"
        registros = read_csv(f'./{database_path}/{arquivo}')
    elif tipo.lower() == 'investimento':
        arquivo = "investimentos.csv"
        registros = read_csv(f'./{database_path}/{arquivo}')
    else:
        print('Tipo de movimentação inválida.',
              'Escolha entre: "receita", "despesa" ou "investimento"', sep='\n')
    
    indices = [int(i['id']) for i in registros]
    if indice in indices:
        for index, registro in enumerate(registros):
            if int(registro['id']) == indice:
                registros.pop(index)
                print(f"{tipo} {registro} deletado com sucesso.")
                break
    else:
        print(f"\nRegistro {indice} não encontrado.\n")
        
    # atualizar indices
    # for index, registro in enumerate(registros):
    #     registro['id'] = f'{index+1:07d}'
    # # exportar para csv

    

    atualizar_base_csv(registros, tipo, path=database_path, nome_arquivo=arquivo)
    return registros



def atualizar_registro(database_path):

    
    novo_tipo = input('Insira o novo tipo de movimentação (receita, despesa ou investimento): ')
    
    id_registro = int(input('Insira o id do registro a ser atualizado: '))
    
    
    

    data_atual_formatada = datetime.now().strftime('%d/%m/%Y')

    if novo_tipo.lower() in ['receita', 'despesa']:
        arquivo = "movimentacoes.csv"
        registros = read_csv(f'./{database_path}/{arquivo}')
    elif novo_tipo.lower() == 'investimento':
        arquivo = "investimentos.csv"
        registros = read_csv(f'./{database_path}/{arquivo}')
    else:
        print('Tipo de movimentação inválida.',
              'Escolha entre: "receita", "despesa" ou "investimento"', sep='\n')

    print (f'registros: {registros[id_registro-1]}')
    valor = float(input('Insira o novo valor da movimentação: '))

    if novo_tipo.lower() == 'despesa':
        valor = -abs(valor)
    for index, registro in enumerate(registros):
        if int(registro['id']) == id_registro:
            registro['Valor'] = valor
            registro['Data'] = data_atual_formatada 
            registro['Tipo'] = novo_tipo

    registros = atualizar_base_csv(registros, novo_tipo, path=database_path, nome_arquivo=arquivo)
    
    print(f"Registro {id_registro} atualizado com sucesso.")
    if novo_tipo.lower() == 'investimento':
        atualizacao_do_rendimento(database_path)

#Crie pelo menos uma função de agrupamento, que seja capaz de 
# mostrar o total de valor baseado em alguma informação (mês, tipo...). 
# Esta função é de livre escolha do grupo. Pode ser, por exemplo, a média de 
# receitas/despesas em um determinado mês, o rendimento médio dos investimentos em um dado período etc.

def agrupar_movimentacoes(database_path):
    tipo_de_registros = {1: 'Receita', 2: 'Despesa', 3: 'Investimento'}

    # Exibir opções para o usuário
    print("Tipos de registro disponíveis:")
    for chave, descricao in tipo_de_registros.items():
        print(f"{chave}. {descricao}")

    # Obter e validar a escolha do usuário
    try:
        tipo = int(input('Qual o tipo de registro que deseja agrupar? '))
        tipo_agrupamento = tipo_de_registros[tipo]
    except (ValueError, KeyError):
        print("Tipo de registro inválido.")
        return

    # Selecionar o arquivo e índices com base no tipo de registro
    if tipo_agrupamento in ['Receita', 'Despesa']:
        arquivo = "movimentacoes.csv"
        indice_valor = 'Valor'
        mostrar_montante = False
    elif tipo_agrupamento == 'Investimento':
        arquivo = "investimentos.csv"
        indice_valor = 'Valor'
        mostrar_montante = True
        indice_montante = 'Montante'
    else:
        print("Tipo de registro inválido.")
        return

    # Ler os registros do arquivo CSV
    try:
        with open(f'{database_path}/{arquivo}', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            registros = list(reader)
    except FileNotFoundError:
        print(f"Arquivo {arquivo} não encontrado no caminho especificado.")
        return
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")
        return

    # Inicializar variáveis de soma total
    soma_total = 0.0
    soma_montante = 0.0

    # Somar os valores para o tipo de agrupamento selecionado
    for entrada in registros:
        try:
            valor = float(entrada[indice_valor])
            tipo_movimentacao = entrada['Tipo']
            if mostrar_montante:
                montante = float(entrada[indice_montante])
            else:
                montante = 0.0  # Não usado para Receita e Despesa
        except (ValueError, KeyError) as e:
            print(f"Erro ao processar a entrada: {e}")
            continue

        # Somar o valor e o montante se o tipo de movimentação corresponder ao tipo de agrupamento
        if tipo_movimentacao == tipo_agrupamento:
            soma_total += valor
            if mostrar_montante:
                soma_montante += montante

    # Exibir o resultado
    if tipo_agrupamento == 'Investimento':
        print(f"Soma total de {tipo_agrupamento} - Valor investido: {soma_total}")
        print(f"Soma total de {tipo_agrupamento} - Montante total: {soma_montante}")
    else:
        print(f"Soma total de {tipo_agrupamento}: {soma_total}")


def exportar_relatorio_csv(database_path):

    # tipo_de_registros = {1: 'Receita', 2: 'Despesa', 3: 'Investimento'}

    # for chave, descricao in tipo_de_registros.items():
    #     print(f"{chave}. {descricao}")
    # tipo = input('Qual o tipo de registro que deseja exportar? ')
    # tipo_relatorio = tipo_de_registros[int(tipo)]
    relatorio = listar_movimentacoes(database_path="./database")
    
    nome_arquivo = input('Insira o nome do arquivo: ')

    keys = relatorio[0].keys()
    with open(f'{database_path}/{nome_arquivo}.csv', 'w', newline='') as file:
        dict_writer = csv.DictWriter(file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(relatorio)


def atualizar_base_csv(movimentacoes,tipo,path='database', nome_arquivo='relatorio'):
    """
    exporta relatório de movimentações para um arquivo csv

    Parameters:
        movimentacoes (list): lista de movimentações
        formato (str): formato do arquivo
        nome_arquivo (str): nome do arquivo
    """
    keys = movimentacoes[0].keys()

    if tipo.lower() in ['receita', 'despesa']:
        arquivo = "movimentacoes.csv"
    elif tipo.lower() == 'investimento':
        arquivo = "investimentos.csv"
    else:
        print('Tipo de movimentação inválida.',
              'Escolha entre: "receita", "despesa" ou "investimento"', sep='\n')
    with open(f'{path}/{nome_arquivo}', 'w', newline='') as file:
        dict_writer = csv.DictWriter(file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(movimentacoes)


def retornar_ultimo_id(tipo: str, path: str):
    """Verifica o último ID registrado no banco de dados.

                Parameters:
                    tipo (str): Tipo de movimentação (receita, despesa ou investimento)

                Returns:
                    ultimo_id (str): Ultimo id registrado no banco de dados escolhido.
    """
    try:
        if tipo.lower() not in ['receita', 'despesa', 'investimento']:
            raise ValueError("Tipo de movimentação inválido.") # criar classe de erro
    except (ValueError, AttributeError) as e:
        return tipo, e

    arquivo = "investimentos.csv" if tipo.lower() == 'investimento' else "movimentacoes.csv"

    try:
        with open(os.path.join(path, arquivo), 'r', newline='') as file:
            reader = csv.reader(file, delimiter=',')
            lista_id = [linha[0] for linha in reader if linha[0] != 'id']
            ultimo_id = f'{0:07d}' if len(lista_id) == 0 else max(lista_id)
        return ultimo_id
    except (FileNotFoundError, PermissionError) as e:
        print(f'Erro ao abrir o arquivo {arquivo}: {e}')
# %%

def print_tabular_data(data):
    if not data:
        print("No data available to display.")
        return

    # Get the headers from the first dictionary
    headers = list(data[0].keys())
    
    # Determine the column widths based on the longest data in each column
    column_widths = [max(len(str(row[key])) for row in data) for key in headers]
    column_widths = [max(width, len(header)) for width, header in zip(column_widths, headers)]

    # Create the header row
    header_row = "| " + " | ".join(f"{header:{width}}" for header, width in zip(headers, column_widths)) + " |"
    separator = "-" * len(header_row)

    # Print the table
    print(separator)
    print(header_row)
    print(separator)
    
    for entry in data:
        row = "| " + " | ".join(f"{str(entry[key]):{width}}" for key, width in zip(headers, column_widths)) + " |"
        print(row)
        print(separator)
# %%


def read_csv(path):
    """
    Lê um arquivo csv e retorna uma lista de dicionários

    Parameters:
        path (str): caminho do arquivo csv

    Returns:
        lista_de_dicionarios (list): lista de dicionários
    """
    try:
        lista_de_dicionarios = []
        with open(path, newline='') as f:
            leitor_csv = csv.DictReader(f)
            for linha in leitor_csv:
                lista_de_dicionarios.append(linha)
        return lista_de_dicionarios
    except FileNotFoundError:
        print(f'Arquivo {path} não encontrado.')
        return None
