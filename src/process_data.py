
import pandas as pd
from datetime import datetime, timedelta

# Carregar o arquivo CSV
df = pd.read_csv('data/invoices.csv')

# Converter a coluna de data para formato datetime
df['invoice_date'] = pd.to_datetime(df['invoice_date'])

# Definir o ponto de referência (último mês a ser considerado)
end_date = datetime(2020, 1, 31)

# Filtrar os últimos 3 e 6 meses
three_months = end_date - timedelta(days=90)
six_months = end_date - timedelta(days=180)

# Função para calcular a média de faturamento
def calculate_averages(df, period_start, period_end):
    filtered = df[(df['invoice_date'] >= period_start) & (df['invoice_date'] <= period_end)]
    if filtered.empty:
        return None
    return filtered['invoice_value'].mean()

# Preparar o DataFrame para o resultado
result = []

for customer, group in df.groupby(['customer', 'account']):
    avg_3_months = calculate_averages(group, three_months, end_date)
    avg_6_months = calculate_averages(group, six_months, end_date)
    result.append({
        'customer': customer[0],
        'account': customer[1],
        'avg_invoices_last_3_months': avg_3_months,
        'avg_invoices_last_6_months': avg_6_months
    })

# Transformar o resultado em DataFrame e exibir
result_df = pd.DataFrame(result)
print(result_df)
