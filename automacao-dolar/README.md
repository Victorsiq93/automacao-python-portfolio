# 💱 Automação de Cotação do Dólar

Automação em Python que busca a cotação do dólar (USD → BRL),
salva os dados em um arquivo Excel e mantém um histórico diário.

## 🚀 Funcionalidades
- Consumo de API pública
- Registro automático de data
- Histórico incremental em Excel
- Estrutura profissional de projeto

## 📁 Estrutura do Projeto
automacao-dolar/
│
├─ dados/
│   └─ historico_dolar.xlsx
│
├─ scripts/
│   └─ automacao_dolar.py
│
└─ README.md

## 🛠 Tecnologias Utilizadas
- Python
- Requests
- Pandas
- OpenPyXL

## ▶️ Como Executar
1. Instale as dependências:
```bash
pip install requests pandas openpyxl

python scripts/automacao_dolar.py
