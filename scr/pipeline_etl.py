import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# 1. Carregamento dos dados
df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

# 2. Renomeando colunas
df.rename(columns={
    'work_year': 'ano_trabalho',
    'experience_level': 'nivel_experiencia',
    'employment_type': 'tipo_emprego',
    'job_title': 'cargo',
    'salary': 'salario',
    'salary_currency': 'moeda',
    'salary_in_usd': 'usd',
    'employee_residence': 'residencia',
    'remote_ratio': 'remoto',
    'company_location': 'localizacao_empresa',
    'company_size': 'porte_empresa'
}, inplace=True)


# 3. Traduzindo valores categóricos

# Nível de experiência
senioridade_traduzida = {
    'EN': 'Junior',
    'MI': 'Pleno',
    'SE': 'Sênior',
    'EX': 'Executivo'
}
df["nivel_experiencia"] = df["nivel_experiencia"].map(senioridade_traduzida)

# Tipo de trabalho remoto
tipo_contrato_traduzido = {
    0: 'Presencial',
    50: 'Híbrido',
    100: 'Remoto'
}
df["remoto"] = df["remoto"].map(tipo_contrato_traduzido)


# 4. Tratamento de dados

# Preenchendo valores nulos na coluna ano_trabalho
df["ano_trabalho"] = df["ano_trabalho"].fillna(df["ano_trabalho"].mean()).round().astype(int)

# Cálculo da média salarial por categoria de experiência
df["media_categoria"] = df.groupby("nivel_experiencia")["usd"].transform("mean").round()

# Criando coluna com situação salarial (desvio percentual)
df["situacao_salario"] = ((df["usd"] - df["media_categoria"]) / df["media_categoria"] * 100).round(2)


# 5. Visualizações com Seaborn / Matplotlib

# Gráfico de barras por nível de experiência
sns.barplot(data=df, x="nivel_experiencia", y="usd")
plt.title("Salário por Nível de Experiência (Gráfico Simples)")
plt.show()

# Contagem por nível de experiência
df["nivel_experiencia"].value_counts().plot(kind="bar", title="Distribuição por Senioridade")
plt.xlabel("Nível de Experiência")
plt.ylabel("Quantidade")
plt.show()

# Salário por senioridade (ordenado)
ordem = df.groupby("nivel_experiencia")["usd"].mean().sort_values(ascending=False).index
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="nivel_experiencia", y="usd", order=ordem)
plt.xlabel("Senioridade")
plt.ylabel("Salário (USD)")
plt.title("Salário por Nível de Experiência")
plt.show()

# Histograma de salários
plt.figure(figsize=(8, 5))
sns.histplot(data=df["usd"], bins=100, kde=True)
plt.title("Distribuição de Salários em USD")
plt.xlabel("Salário (USD)")
plt.ylabel("Frequência")
plt.show()

