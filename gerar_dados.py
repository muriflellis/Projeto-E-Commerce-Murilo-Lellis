import pandas as pd
import numpy as np
import os

# Garantir que a pasta data existe
os.makedirs('data', exist_ok=True)

# Gerando um amostragem baseada no comportamento do dataset real da Olist (E-commerce Brasileiro)
np.random.seed(42)
n_linhas = 250

categorias = ['utilidades_domesticas', 'informatica_acessorios', 'beleza_saude', 'esporte_lazer', 'moveis_decoracao']
cidades = ['sao paulo', 'rio de janeiro', 'belo horizonte', 'curitiba', 'porto alegre', 'salvador', None]

dados_reais = {
    'id_pedido': [f'req_{np.random.randint(100000, 999999)}' for _ in range(n_linhas)],
    'data_compra': pd.date_range(start='2025-01-01', periods=n_linhas, freq='h').strftime('%Y-%m-%d %H:%M:%S'),
    'produto_categoria': np.random.choice(categorias, n_linhas, p=[0.3, 0.2, 0.2, 0.15, 0.15]),
    'preco': np.round(np.random.exponential(scale=120, size=n_linhas) + 15, 2),
    'frete': np.round(np.random.uniform(10, 45, size=n_linhas), 2),
    'cliente_cidade': np.random.choice(cidades, n_linhas, p=[0.4, 0.2, 0.1, 0.1, 0.05, 0.05, 0.1]), # 10% de nulos na cidade
    'avaliacao_score': np.random.choice([1, 2, 3, 4, 5], n_linhas, p=[0.08, 0.05, 0.12, 0.35, 0.40])
}

df_olist = pd.DataFrame(dados_reais)

# Introduzindo valores nulos de propósito em categorias e preços para simular a "bagunça" real
df_olist.loc[df_olist.sample(frac=0.05).index, 'produto_categoria'] = None
df_olist.loc[df_olist.sample(frac=0.04).index, 'preco'] = None

# Salvando a tabela real tratada no Excel
with pd.ExcelWriter('data/dados_ecommerce.xlsx', engine='openpyxl') as writer:
    df_olist.to_excel(writer, sheet_name='vendas_olist', index=False)

print("✅ Base real Olist (simulada com nulos) gerada com sucesso em 'data/dados_ecommerce.xlsx'!")

