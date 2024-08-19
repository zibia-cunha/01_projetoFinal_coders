#%%
from src.utils import *

PATH = "./database"
#%%

def main():
    """
    Função principal do programa
    """
    print("SISTEMA DE CONTROLE FINANCEIRO\n")
    dicionario_nomes = {
        1: "Incluir Registros",
        2: "Incluir Registros de CSV",
        3: "Listar Movimentações",
        4: "Calcular Rendimento",
        5: "Deletar Registro",
        6: "Atualizar Registro",
        7: "Agrupar Movimentações",
        8: "Exportar Reltório CSV",
        0: "Sair"
    }
    acoes = {
        '1': incluir_registros_base_dados,
        '2': incluir_registros_de_arquivo_csv,
        '3': listar_movimentacoes,
        '4': atualizacao_do_rendimento,
        '5': deletar_registro,
        '6': atualizar_registro,
        '7': agrupar_movimentacoes,
        '8': exportar_relatorio_csv
    }

    base_dados = {}
    while True:
        for chave, descricao in dicionario_nomes.items():
            print(f"{chave}. {descricao}")
        escolha = input("Escolha sua opção: ")
        if escolha == '0':
            print("Saindo do sistema...")
            if len(base_dados) > 0:
                print(base_dados)
            break
        elif escolha in acoes:
            if escolha == '1':
                print(f"\nExecutando ação: {dicionario_nomes[int(escolha)]}")
                base_dados = acoes[escolha](base_dados)
                criar_registro_movimentacao(base_dados, database_path="database")
            elif escolha == '2':
                print(f"\nExecutando ação: {dicionario_nomes[int(escolha)]}")
                path = input("Insira o caminho do arquivo csv: ")
                base_dados = acoes[escolha](path)
                criar_registro_movimentacao(base_dados, database_path="database")
            else:
                acoes[escolha]("./database")
        else:
            print("Ação inválida. Por favor, escolha uma ação válida.")
#%%

main()

# %%
