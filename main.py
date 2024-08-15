from src.utils import *

PATH = "./database"


def main():
    """
    Função principal do programa
    """
    print("SISTEMA DE CONTROLE FINANCEIRO\n")
    dicionario_nomes = {
        1: "Incluir Registros",
        2: "Incluir Registros de CSV",
        3: "Criar Regstro de Movimentação",
        4: "Listar Movimentações",
        5: "Calcular Rendimento",
        6: "Deletar Registro",
        7: "Atualizar Registro",
        8: "Agrupar Movimentações",
        9: "Exportar Relatório JSON",
        10: "Exportar Reltório CSV",
        0: "Sair"
    }
    acoes = {
        '1': incluir_registros_base_dados,
        '2': incluir_de_csv,
        '3': criar_registro_movimentacao,
        '4': listar_movimentacoes,
        '5': calcular_rendimento,
        '6': deletar_registro,
        '7': atualizar_registro,
        '8': agrupar_movimentacoes,
        '9': exportar_relatorio_json,
        '10': exportar_relatorio_csv
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
            elif escolha == '7':
                print(f"\nExecutando ação: {dicionario_nomes[int(escolha)]}")
                base_dados = acoes[escolha](base_dados)
            else:
                acoes[escolha](base_dados)
        else:
            print("Ação inválida. Por favor, escolha uma ação válida.")


main()
