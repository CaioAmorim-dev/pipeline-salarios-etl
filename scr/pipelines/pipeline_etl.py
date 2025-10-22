import pandas as pd
import numpy as np
import plotly.express as px

def carregar_dados_tratados(base_dados):

    # 1. Carregamento dos dados
    df = pd.read_csv(base_dados)

    # 2. Renomeando colunas
    df.rename(columns={
        'work_year': 'ano',
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
    if "nivel_experiencia" in df.columns:
        df["nivel_experiencia"] = df["nivel_experiencia"].map(senioridade_traduzida)
    else:
        # Se a coluna não existir, cria como valor padrão ou copia de outra coluna
        df["nivel_experiencia"] = "Desconhecido"

    # Tipo de trabalho remoto
    tipo_contrato_traduzido = {
        0: 'Presencial',
        50: 'Híbrido',
        100: 'Remoto'
    }
    df["remoto"] = df["remoto"].map(tipo_contrato_traduzido)


    # 4. Tratamento de dados
    # Preenchendo valores nulos na coluna ano_trabalho
    df["ano"] = df["ano"].fillna(df["ano"].mean()).round().astype(int)

    # Cálculo da média salarial por categoria de experiência
    df["media_categoria"] = df.groupby("nivel_experiencia")["usd"].transform("mean").round()

    # Criando coluna com situação salarial (desvio percentual)
    df["situacao_salario"] = ((df["usd"] - df["media_categoria"]) / df["media_categoria"] * 100).round(2)

    df.to_csv("dados_tratados.csv", index=False)

    return df