import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

# Carrega os dados diretamente
df = pd.read_csv("https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv")

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

# 6. Visualizações com Plotly

# Média salarial por senioridade (Plotly)
senioridade_media_salario = df.groupby("nivel_experiencia")["usd"].mean().sort_values(ascending=False).reset_index()
fig = px.bar(
    senioridade_media_salario,
    x="nivel_experiencia",
    y="usd",
    title="Média Salarial por Senioridade",
    labels={"nivel_experiencia": "Nível de experiência", "usd": "Média Salarial Anual (USD)"}
)
fig.show()

# Proporção dos tipos de trabalho remoto (Pie Chart)
remoto_contagem = df["remoto"].value_counts().reset_index()
remoto_contagem.columns = ["remoto", "quantidade"]

fig = px.pie(
    remoto_contagem,
    names="remoto",
    values="quantidade",
    title="Proporção dos Tipos de Trabalho",
    hole=0.6
)
fig.show()
