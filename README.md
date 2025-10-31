# 📊 Dashboard de Análise Salarial — Área de Dados

Este projeto tem como objetivo analisar e visualizar salários na área de dados ao redor do mundo, com base em dados públicos de 2020 a 2025.
O **pipeline** realiza a **extração, tratamento e carga (ETL)** dos dados, e o dashboard interativo em Streamlit permite explorar insights de forma intuitiva.

# 🚀 Funcionalidades

Extração automática de dados online (com fallback para cache local)

Pipeline de tratamento e padronização de dados (Pandas + PyCountry)

Dashboard interativo com filtros dinâmicos

Gráficos criados com Plotly Express:

Top 10 cargos por média salarial

Distribuição de salários

Evolução salarial por ano

Salário por nível de experiência

Mapa global de salários de Data Scientists

# 🧠 Tecnologias Utilizadas

Python 3.10+

Pandas — manipulação de dados

Plotly Express — visualização interativa

Streamlit — criação do dashboard

PyCountry — padronização de códigos de países


## ⚙️ Como Rodar o Projeto
**1️⃣ Clonar o repositório**

```
git clone https://github.com/seuusuario/Imersao_dados.git

cd Imersao_dados
```

**2️⃣ Criar e ativar o ambiente virtual**

No Windows:

```
python -m venv .venv
.venv\Scripts\activate
```
 



No Mac/Linux:
```
python3 -m venv .venv
source .venv/bin/activate
```

**3️⃣ Instalar as dependências**
```
pip install -r requirements.txt
```

**4️⃣ Rodar o dashboard**
```
streamlit run src/dashboards/dashboard.py
```

**5️⃣ Acessar no navegador**

Após rodar o comando, o Streamlit abrirá automaticamente o dashboard (ou acesse manualmente):
```
http://localhost:8501
```