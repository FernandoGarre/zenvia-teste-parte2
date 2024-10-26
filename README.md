
# Zenvia Teste - Parte 2: Serviços de Agregação de Dados com Entradas CSV

Este projeto computa a média de faturamento de cada conta (`account`) nos últimos três e seis meses, considerando entradas de dados no formato CSV.

## Estrutura do Projeto

- `data/invoices.csv`: Arquivo de entrada contendo os dados de faturamento.
- `src/process_data.py`: Script principal para processar o CSV e calcular as médias.
- `docs/EXECUTION.md`: Instruções detalhadas para execução do projeto.

## Executando o Projeto

1. Instale as dependências:
   ```bash
   pip install pandas
   ```

2. Execute o script:
   ```bash
   python src/process_data.py
   ```

O resultado será exibido no console, mostrando a média de faturamento de cada `account` nos últimos 3 e 6 meses, com valores `null` onde os dados são insuficientes.
