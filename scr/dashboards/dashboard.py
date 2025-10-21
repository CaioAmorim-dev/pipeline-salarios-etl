import streamlit as st
import pandas as pd
import plotly.express as px
import scr.pipelines.pipeline_etl as pipeline_etl


st.set_page_config(
    page_title = "Dashboard teste",
    page_icon = "📊",
    layout = "wide",
)

df = pipeline_etl.carregar_dados_tratados("https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv")  

anos_disponiveis = sorted(df["ano"].unique())
campo_anos = st.sidebar.multiselect("Ano", anos_disponiveis, default=anos_disponiveis)

senioridades_disponiveis = sorted(df["senioridade"].unique())
campo_senioridade = st.sidebar.multiselect("Senioridade", senioridades_disponiveis ,default=senioridades_disponiveis)

contratos_disponiveis = sorted(df["contrato"].unique())
campo_contratos = st.sidebar.multiselect("contrato", contratos_disponiveis ,default=contratos_disponiveis)

tamanho_empresas_disponiveis = sorted(df["tamanho_empresa"].unique())
campo_tamanho_empresa = st.sidebar.multiselect("Tammanho da empresa", tamanho_empresas_disponiveis ,default=tamanho_empresas_disponiveis)

df_selecionado = df[
    (df["ano"].isin(campo_anos)) &
    (df["senioridade"].isin(campo_senioridade)) &
    (df["contrato"].isin(campo_contratos)) &
    (df["tamanho_empresa"].isin(campo_tamanho_empresa))
]

st.title("📈 Dashboard de análise de Salário na área de dados")
st.markdown("Explore dados e conheça oportunidades da área de dados no mundo todo. Ultilize os filtros a direita para embasar sua pesquisa")

if not df_selecionado.empty:
    salario_medio = df_selecionado["usd"].mean()
    salario_maximo = df_selecionado["usd"].max()
    total_registros = df_selecionado.shape[0]
    cargo_mais_frequente = df_selecionado["cargo"].mode()[0]
else:
    salario_maximo, salario_medio, total_registros, cargo_mais_frequente = 0, 0, 0, ""
    st.warning("Não há dados para os filtros selecionados!")


col1, col2, col3,col4 = st.columns(4)
col1.metric("Salário médio", f"${salario_medio:,.0f}")
col2.metric("Salário máximo", f"${salario_maximo:,.0f}")
col3.metric("Total de registros", f"{total_registros:,}")
col4.metric("Cargo mais frequente", cargo_mais_frequente)
st.markdown("---")

col_graf1, col_graf2 = st.columns(2)
with col_graf1:
    if not df_selecionado.empty:
        top_cargos = df_selecionado.groupby("cargo")["usd"].mean().nlargest(10).sort_values(ascending= True).reset_index()
        grafico_cargos = px.bar(
            data_frame= top_cargos,
            x = "usd",
            y = "cargo",
            orientation= "h",
            title= "Top 10 cargos por salário médio",
            labels={"usd" :"Media de Salário anual","cargo" : "Cargos"}
        )
        grafico_cargos.update_layout(title_x=0.1, yaxis={"categoryorder" : "total ascending"})
        st.plotly_chart(grafico_cargos, use_container_width=True)
    else:
        st.warning("Nenhum dado para ser exibido")








