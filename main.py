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
        8: "Exportar Relatório JSON",
        9: "Exportar Reltório CSV",
        0: "Sair"
    }
    acoes = {
        '1': incluir_registros_base_dados,
        '2': incluir_de_csv,
        '3': listar_movimentacoes,
        '4': atualizacao_do_rendimento,
        '5': deletar_registro,
        '6': atualizar_registro,
        '7': agrupar_movimentacoes,
        '8': exportar_relatorio_json,
        '9': exportar_relatorio_csv
    }

    base_dados = {}
    while True:
        for chave, descricao in dicionario_nomes.items():
            print(f"{chave}. {descricao}")
        escolha = input("Escolha sua opção: ")
        if escolha == '0':
            print("Saindo do sistema...")
            print(base_dados)
            break
        elif escolha in acoes:
            if escolha == '1':
                print(f"\nExecutando ação: {dicionario_nomes[int(escolha)]}")
                base_dados = acoes[escolha](base_dados)
                criar_registro_movimentacao(base_dados, database_path="database")
            elif escolha == '7':
                print(f"\nExecutando ação: {dicionario_nomes[int(escolha)]}")
                base_dados = acoes[escolha](base_dados)
            else:
                acoes[escolha](base_dados)
        else:
            print("Ação inválida. Por favor, escolha uma ação válida.")
#%%

main()

# %%
