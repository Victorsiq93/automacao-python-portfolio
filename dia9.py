import pandas as pd
import os

pasta = 'planilhas'
tabelas = []

for arquivo in os.listdir(pasta):
    if arquivo.endswith('.xlsx'):
        caminho = os.path.join(pasta, arquivo)
        print('Lendo:', caminho)
        tabela = pd.read_excel(caminho)
        tabelas.append(tabela)

if len(tabelas) == 0:
    print('Nenhuma tabela encontrada')
else:
    consolidado = pd.concat(tabelas, ignore_index=True)

    consolidado['faturamento'] = consolidado['quantidade'] * consolidado['preco']

    total = consolidado['faturamento'].sum()

    print(consolidado)
    print('Faturamento total:', total)

    consolidado.to_excel('relatorio_consolidado.xlsx', index=False)