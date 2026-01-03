import pandas as pd

# Ler a planilha
tabela = pd.read_excel("vendas.xlsx")

tabela['faturamento'] = tabela['Quantidade'] * tabela['Preço']
total = tabela['faturamento'].sum()
print('Faturamento total:', total)

tabela.to_excel('relatorio_vendas.xlsx', index=False)

print(tabela)
