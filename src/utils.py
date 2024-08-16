from datetime import datetime
import os
import csv

# data_atual = datetime.now()
# data_atual_formatada = data_atual.strftime('%d/%m/%Y')


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
    
    # arquivo = 'base_dados.json'
    # try:
    #     with open(arquivo, 'r') as file:
    #         base_dados = json.load(file)
    # except FileNotFoundError:
    #     base_dados = {}
    
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
        print(f"Registro de {tipo_de_registros}, no valor de {valor} cadastrado com sucesso")
        print("*" * 60)

        continuarCadastro = input("\nDeseja continuar cadastrando registros? S/N ")
        if continuarCadastro.upper() == "S":
            incluir_registros_base_dados(base_dados)

    else:
        print("Opção inválida")
    return base_dados

    # with open(arquivo, 'w') as file:
    #     json.dump(base_dados, file, indent=4)

    # print(f"Dados salvos no arquivo '{arquivo}'.")

    # return base_dados


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


def listar_movimentacoes(database_path="database", data=None, tipo=None):
    """
    Lista as movimentações

    Parameters:
        database_path (str): caminho do banco de dados

    Returns:
        movimentacoes (list): lista de movimentações
    """
    if data == None:
        data = input('Insira a data da movimentação (dd/mm/aaaa):')
    if tipo == None:
        tipo = input('Insira o tipo de movimentação (receita, despesa ou investimento):')
    
    investimentos = read_csv(f'{database_path}/investimentos.csv')
    print(investimentos)
    movimentacoes = read_csv(f'{database_path}/movimentacoes.csv')
    if data:
        if tipo.lower() in ['receita', 'despesa']:
            registros = []
            for movimentacao in movimentacoes:
                if movimentacao['Tipo'].lower() == tipo.lower() and movimentacao['Data'] == data:
                    registros.append(movimentacao)
            return registros
        else:
            registros = []
            for movimentacao in investimentos:
                if movimentacao['Data'] == data:
                    registros.append(movimentacao)
            return registros
    else:
        if tipo.lower() in ['receita', 'despesa']:
            registros = []
            for movimentacao in movimentacoes:
                if movimentacao['Tipo'].lower() == tipo.lower():
                    registros.append(movimentacao)
            return registros
        else:
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

            montante = float(ultimo_investimento["Montante"]) + float(investimento["Valor"]) + float(ultimo_investimento["Rendimento"]) 

            investimentos[indice]["Rendimento"] = rendimento
            investimentos[indice]["Montante"] = montante
    exportar_relatorio_csv(investimentos, tipo="investimento", path=database, nome_arquivo="investimentos.csv")


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

def deletar_registro(indice: int, tipo: str,
                     database_path: str):
    """
    Determina o tipo de movimentação e deleta o registro correspondente ao indice

    Parameters:
        indice (int): indice do registro a ser deletado
        tipo (str): tipo de movimentação
        database_path (str): caminho do banco de dados
    """
    if tipo.lower() in ['receita', 'despesa']:
        arquivo = "movimentacoes.csv"
        registros = read_csv(f'./{database_path}/{arquivo}')
    elif tipo.lower() == 'investimento':
        arquivo = "investimentos.csv"
        registros = read_csv(f'./{database_path}/{arquivo}')
    else:
        print('Tipo de movimentação inválida.',
              'Escolha entre: "receita", "despesa" ou "investimento"', sep='\n')
    
    for index, registro in enumerate(registros):
        if int(registro['id']) == indice:
            registros.pop(index)
            break
    # atualizar indices
    for index, registro in enumerate(registros):
        registro['id'] = f'{index+1:07d}'
    # exportar para csv

    exportar_relatorio_csv(registros, tipo, path=database_path, nome_arquivo=arquivo)
    return registros



def atualizar_registro(dicionario):
    ## TODO implementar a função de atualizar registro

    # Atualizar os registros de forma que o novo registro tenha a data do momento em 
    # a atualização é feita. a função deve ainda chamar a função "atualizacao_do_rendimento" caso
    # a atualização seja feita em investimentos.

    # identificador = input('insira o identificador')
    # if identificador in dicionario:
    #     novo_tipo = input('Insira o novo tipo: ').capitalize()
    #     dicionario[identificador]['Tipo'] = novo_tipo
    #     novo_valor = float('Insira o novo valor: ')
    #     dicionario[identificador]['Valor'] = novo_valor
        
    #     dicionario[identificador]['Data'] = datetime.now().strftime('%d/%m/%Y')
    #     return f"Registro {identificador} atualizado com sucesso."
    # else:
    #     return f"Registro {identificador} não encontrado."
    pass


#Crie pelo menos uma função de agrupamento, que seja capaz de 
# mostrar o total de valor baseado em alguma informação (mês, tipo...). 
# Esta função é de livre escolha do grupo. Pode ser, por exemplo, a média de 
# receitas/despesas em um determinado mês, o rendimento médio dos investimentos em um dado período etc.

def agrupar_movimentacoes(movimentacoes, agrupar_por):
    # TODO
    """
    agrupa movimentações por tipo

    """
    pass


def exportar_relatorio_json(movimentacoes, formato='json', nome_arquivo='relatorio'):
    """
    exporta relatório de movimentações para um arquivo json

    Parameters:
        movimentacoes (list): lista de movimentações
        formato (str): formato do arquivo
        nome_arquivo (str): nome do arquivo
    """


def exportar_relatorio_csv(movimentacoes,tipo,path='database', nome_arquivo='relatorio'):
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
