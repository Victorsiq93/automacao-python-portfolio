import requests
import pandas as pd
from datetime import datetime
import os

# Buscar cotação
url = 'https://api.frankfurter.app/latest?from=USD&to=BRL'
dados = requests.get(url).json()
cotacao = dados['rates']['BRL']

# Criar Registro
data_hoje = datetime.now().strftime('%Y-%M-%D')

novo_registro = pd.DataFrame({
    'Data': [data_hoje],
    'Moeda': ['USD'],
    'Cotação': [cotacao]
})

# Caminho do arquivo
arquivo = "dados/historico_dolar.xlsx"

# Salvar ou atualizar
if os.path.exists(arquivo):
    historico = pd.read_excel(arquivo)
    historico = pd.concat([historico, novo_registro], ignore_index=True)
else:
    historico = novo_registro

historico.to_excel(arquivo, index=False)

print('Cotação registrada com sucesso!')