# Dashboard Aula 21/05
import streamlit as st
import seaborn as sn
import matplotlib.pyplot as plt
import pandas as pd

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Dashboard Financeiro",
    page_icon="📊",
    layout="wide"
)

# CARREGAR DADOS
df = pd.read_excel("planilhao.xlsx", sheet_name="Sheet1")

# TÍTULO
st.title("📊 Dashboard Financeiro")
st.markdown("Análise interativa das empresas por setor")

# SIDEBAR
st.sidebar.header("Filtros")

setores = st.sidebar.multiselect(
    "Selecione os setores",
    options=df["setor"].unique(),
    default=df["setor"].unique()
)

# FILTRAR DADOS
df_filtrado = df[df["setor"].isin(setores)]

# KPIs
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Total de Empresas",
        value=len(df_filtrado)
    )

with col2:
    st.metric(
        label="Número de Setores",
        value=df_filtrado["setor"].nunique()
    )

with col3:
    st.metric(
        label="ROE Médio",
        value=f"{df_filtrado['roe'].mean():.2f}"
    )

st.divider()

# ABAS
menu = st.tabs([
    "📋 Tabela",
    "📊 Barras",
    "🥧 Pizza",
    "📈 Histograma"
])

# TABELA
with menu[0]:

    st.subheader("Tabela de Dados")

    st.dataframe(
        df_filtrado,
        use_container_width=True
    )

# GRÁFICO DE BARRAS
with menu[1]:

    st.subheader("Empresas por Setor")

    fig, ax = plt.subplots(figsize=(12,6))

    sn.countplot(
        data=df_filtrado,
        x="setor",
        order=df_filtrado["setor"].value_counts().index,
        palette="viridis",
        ax=ax
    )

    plt.title("Quantidade de Empresas por Setor")
    plt.xlabel("Setor")
    plt.ylabel("Quantidade")
    plt.xticks(rotation=45)

    st.pyplot(fig)

# PIZZA
with menu[2]:

    st.subheader("Distribuição dos Setores")

    fig, ax = plt.subplots(figsize=(8,8))

    setor = df_filtrado["setor"].value_counts()

    ax.pie(
        setor,
        labels=setor.index,
        autopct="%1.1f%%",
        startangle=90
    )

    ax.axis("equal")

    st.pyplot(fig)

# HISTOGRAMA
with menu[3]:

    st.subheader("Distribuição do ROE")

    setor_escolhido = st.selectbox(
        "Escolha um setor",
        df_filtrado["setor"].unique()
    )

    filtro = df_filtrado["setor"] == setor_escolhido
    df_setor = df_filtrado[filtro]

    fig, ax = plt.subplots(figsize=(10,6))

    sn.histplot(
        df_setor["roe"],
        bins=20,
        kde=True,
        color="blue",
        ax=ax
    )

    plt.title(f"Distribuição do ROE - {setor_escolhido}")
    plt.xlabel("ROE")
    plt.ylabel("Frequência")

    st.pyplot(fig)


# #                         # Código da Aula 14/05 
# import streamlit as st
# import seaborn as sn
# import matplotlib.pyplot as plt
# import pandas as pd

# # st.text("Meu Primeiro Dashboard")
# df = pd.read_excel("planilhao.xlsx", sheet_name="Sheet1")
# # Titulo de Dashboard
# st.header("Meu Dashboard")
# menu = st.tabs(["Tabela", "Barras", "Pizza"])
# # Expondo o df no Dashboard
# with menu[0]:
#         st.dataframe(df)
# # Gráfico de Barras Vertical
# with menu[1]:
#         fig = plt.figure(figsize=(10,6)) # Tamanho do grafico
#         sn.countplot(data=df, 
#                 x="setor", # Colocar Y="setor" deixa horizontal
#                 order=df['setor'].value_counts().index,
#                 palette="tab10")
#         plt.title("Grafico de Barras por setor")
#         plt.xlabel("Numero de Empresas")
#         plt.ylabel("Setor")
#         plt.xticks(rotation=45)
#         plt.show()
#         st.pyplot(fig)
# # Gráfico de Pizza
# with menu[2]:
#         fig = plt.figure(figsize=(10,6)) # Tamanho do grafico
#         setor = df["setor"].value_counts()
#         plt.pie(setor, labels=setor.index,
#                 autopct="%1.1f%%")
#         st.pyplot(fig)


#                         # Código da Aula 12/05
# import seaborn as sn
# import pandas as pd
# import matplotlib.pyplot as plt
# #Gravando o excel em uma variável DF
# df = pd.read_excel("planilhao.xlsx", sheet_name="Sheet1")
# df.columns
# # Grafifo de Barras
# plt.figure(figsize=(10,6)) # Tamanho do grafico
# sn.countplot(data=df, 
#              x="setor", # Colocar Y="setor" deixa horizontal
#              order=df['setor'].value_counts().index,
#              palette="tab10")
# plt.title("Grafico de Barras por setor")
# plt.xlabel("Numero de Empresas")
# plt.ylabel("Setor")
# plt.xticks(rotation=45)
# plt.show()

# # Grafico de Pizza
# plt.figure(figsize=(10,6)) # Tamanho do grafico
# setor = df["setor"].value_counts()
# plt.pie(setor, labels=setor.index,
#         autopct="%1.1f%%")
# # Nesse caso, usar IA é bom para deixar bonito, estético e funcional

# # Grafico de Histograma
# filtro = df["setor"] == "saúde"
# df_setor = df[filtro]
# sn.histplot(df_setor["roe"], bins = 20, kde=True, color="blue") 


#                         # Códido da Aula 05/05
# # Gráfico de Linha
# # import pandas as pd
# # df = pd.read_excel("planilhao.xlsx", sheet_name="Biom")
# # filtro = df["Conta"]=="EBIT"
# # df.columns
# # colunas = [ '20254T', '20252T',
# #        '20251T', '20244T', '20243T', '20242T', '20241T', '20234T', '20233T',
# #        '20232T', '20231T', '20224T', '20223T', '20222T', '20221T', '20214T',
# #        '20213T', '20212T', '20211T', '20204T', '20203T', '20202T', '20201T',
# #        '20194T', '20193T', '20192T', '20191T', '20184T', '20183T', '20182T',
# #        '20181T', '20174T', '20173T', '20172T', '20171T', '20164T', '20163T',
# #        '20162T', '20161T', '20154T']
# # colunas = sorted(colunas)
# # # instalar a biblioteca matplolib (uv add matplotlib)
# # ebit = df[filtro][colunas].iloc[0]

# # import seaborn as sn
# # sn.lineplot(ebit)
# # sn.histplot(ebit)
# # sn.boxplot(ebit)

# # import matplotlib.pyplot as plt
# # # Grafico do lucro liquido (para casa)
# # filtro_lucro_liquido = df["Conta"]=="Lucro Líquido"
# # df.columns
# # colunas =  [ '20254T', '20252T',
# #        '20251T', '20244T', '20243T', '20242T', '20241T', '20234T', '20233T',
# #        '20232T', '20231T', '20224T', '20223T', '20222T', '20221T', '20214T',
# #        '20213T', '20212T', '20211T', '20204T', '20203T', '20202T', '20201T',
# #        '20194T', '20193T', '20192T', '20191T', '20184T', '20183T', '20182T',
# #        '20181T', '20174T', '20173T', '20172T', '20171T', '20164T', '20163T',
# #        '20162T', '20161T', '20154T']
# # colunas = sorted(colunas)
# # lucro_liquido = df[filtro_lucro_liquido][colunas].iloc[0]
# # sn.lineplot(x=colunas, y=lucro_liquido.values)

# # sn.lineplot(lucro_liquido)
# # sn.histplot(lucro_liquido)
# # sn.boxplot(lucro_liquido)
