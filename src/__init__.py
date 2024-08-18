import csv
import os

print(os.getcwd())
os.makedirs('./database', exist_ok=True)

try:
    with open('./database/movimentacoes.csv', 'x', newline='') as file:
        cabecalho = [['id', 'Data', 'Tipo', 'Valor', 'Ano', 'Mes', 'dia']]
        escritor = csv.writer(file, delimiter=',')
        escritor.writerows(cabecalho)
except FileExistsError:
    pass

try:
    with open('./database/investimentos.csv', 'x', newline='') as file:
        cabecalho = [['id','Data', 'Tipo','Taxa', 'Valor', 'Ano', 'Mes', 'Dia', 'Montante', 'Rendimento']]
        escritor = csv.writer(file, delimiter=',')
        escritor.writerows(cabecalho)
except FileExistsError:
    pass