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

