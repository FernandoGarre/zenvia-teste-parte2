
# Execução do Projeto Zenvia Teste - Parte 2

## Requisitos

- Python 3.x
- Biblioteca `pandas`

Para instalar `pandas`, execute:
```bash
pip install pandas
```

## Arquivo de Entrada

Coloque o arquivo `invoices.csv` na pasta `data/`. Esse arquivo deve conter dados de faturamento com colunas `customer`, `account`, `invoice_date`, e `invoice_value`.

## Executando o Script

Navegue até a pasta do projeto e execute o script:

```bash
python src/process_data.py
```

O script processará o CSV e exibirá as médias de faturamento para cada conta.
