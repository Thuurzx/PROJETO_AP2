"""
Dashboard Financeiro Profissional
Versão sem Plotly
"""

import streamlit as st
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np

# ─────────────────────────────────────────────
# CONFIGURAÇÃO DA PÁGINA
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Dashboard Financeiro",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─────────────────────────────────────────────
# CSS CUSTOMIZADO
# ─────────────────────────────────────────────
st.markdown("""
<style>

    @import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=DM+Sans:wght@300;400;500;600&display=swap');

    :root {
        --bg-primary: #0a0e1a;
        --bg-card: #111827;
        --accent: #00e5ff;
        --accent2: #7c3aed;
        --text-primary: #f1f5f9;
        --text-muted: #64748b;
        --border: rgba(0,229,255,0.12);
    }

    .stApp {
        background: var(--bg-primary);
        color: var(--text-primary);
        font-family: 'DM Sans', sans-serif;
    }

    [data-testid="stSidebar"] {
        background: var(--bg-card);
        border-right: 1px solid var(--border);
    }

    .main-title {
        font-family: 'Space Mono', monospace;
        font-size: 2.3rem;
        font-weight: 700;
        background: linear-gradient(135deg, #00e5ff, #7c3aed);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }

    .main-subtitle {
        color: var(--text-muted);
        margin-bottom: 2rem;
    }

    .kpi-card {
        background: #111827;
        border: 1px solid rgba(0,229,255,0.12);
        border-radius: 15px;
        padding: 1.5rem;
        margin-bottom: 1rem;
    }

    .kpi-label {
        color: #64748b;
        font-size: 0.8rem;
        text-transform: uppercase;
    }

    .kpi-value {
        font-size: 2rem;
        font-weight: bold;
        color: white;
    }

    .section-title {
        color: #00e5ff;
        font-size: 1rem;
        font-weight: bold;
        margin-bottom: 1rem;
        margin-top: 1rem;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# CARREGAR DADOS
# ─────────────────────────────────────────────
@st.cache_data
def carregar_dados():
    return pd.read_excel("planilhao.xlsx")

df = carregar_dados()

# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────
st.sidebar.title("⚙ Filtros")

setores = st.sidebar.multiselect(
    "Selecione os setores",
    options=df["setor"].unique(),
    default=df["setor"].unique()
)

# FILTRAR DADOS
df_filtrado = df[df["setor"].isin(setores)]

# ─────────────────────────────────────────────
# TÍTULO
# ─────────────────────────────────────────────
st.markdown(
    '<div class="main-title">📊 Dashboard Financeiro</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-subtitle">Análise interativa de empresas</div>',
    unsafe_allow_html=True
)

# ─────────────────────────────────────────────
# KPIs
# ─────────────────────────────────────────────
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Empresas</div>
        <div class="kpi-value">{len(df_filtrado)}</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Setores</div>
        <div class="kpi-value">{df_filtrado["setor"].nunique()}</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">ROE Médio</div>
        <div class="kpi-value">{df_filtrado["roe"].mean():.2f}</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">ROE Máximo</div>
        <div class="kpi-value">{df_filtrado["roe"].max():.2f}</div>
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
# ABAS
# ─────────────────────────────────────────────
menu = st.tabs([
    "📋 Tabela",
    "📊 Barras",
    "🥧 Pizza",
    "📈 Histograma",
    "🔵 Scatter",
    "🔥 Correlação"
])

# ─────────────────────────────────────────────
# TABELA
# ─────────────────────────────────────────────
with menu[0]:

    st.markdown(
        '<div class="section-title">Tabela de Dados</div>',
        unsafe_allow_html=True
    )

    st.dataframe(
        df_filtrado,
        use_container_width=True
    )

# ─────────────────────────────────────────────
# BARRAS
# ─────────────────────────────────────────────
with menu[1]:

    st.markdown(
        '<div class="section-title">Empresas por Setor</div>',
        unsafe_allow_html=True
    )

    fig, ax = plt.subplots(figsize=(12,6))

    contagem = df_filtrado["setor"].value_counts()

    sn.barplot(
        x=contagem.index,
        y=contagem.values,
        palette="viridis",
        ax=ax
    )

    ax.set_title("Quantidade de Empresas por Setor")
    ax.set_xlabel("Setor")
    ax.set_ylabel("Quantidade")

    plt.xticks(rotation=45)

    st.pyplot(fig)

# ─────────────────────────────────────────────
# PIZZA
# ─────────────────────────────────────────────
with menu[2]:

    st.markdown(
        '<div class="section-title">Distribuição dos Setores</div>',
        unsafe_allow_html=True
    )

    fig, ax = plt.subplots(figsize=(8,8))

    setor = df_filtrado["setor"].value_counts()

    ax.pie(
        setor,
        labels=setor.index,
        autopct="%1.1f%%"
    )

    st.pyplot(fig)

# ─────────────────────────────────────────────
# HISTOGRAMA
# ─────────────────────────────────────────────
with menu[3]:

    st.markdown(
        '<div class="section-title">Distribuição do ROE</div>',
        unsafe_allow_html=True
    )

    fig, ax = plt.subplots(figsize=(12,6))

    sn.histplot(
        df_filtrado["roe"],
        bins=20,
        kde=True,
        color="cyan",
        ax=ax
    )

    ax.set_title("Distribuição do ROE")

    st.pyplot(fig)

# ─────────────────────────────────────────────
# SCATTER
# ─────────────────────────────────────────────
with menu[4]:

    st.markdown(
        '<div class="section-title">Scatter Plot</div>',
        unsafe_allow_html=True
    )

    numeros = df.select_dtypes(include=np.number).columns

    eixo_x = st.selectbox("Eixo X", numeros)
    eixo_y = st.selectbox("Eixo Y", numeros, index=1)

    fig, ax = plt.subplots(figsize=(12,6))

    sn.scatterplot(
        data=df_filtrado,
        x=eixo_x,
        y=eixo_y,
        hue="setor",
        ax=ax
    )

    st.pyplot(fig)

# ─────────────────────────────────────────────
# CORRELAÇÃO
# ─────────────────────────────────────────────
with menu[5]:

    st.markdown(
        '<div class="section-title">Mapa de Correlação</div>',
        unsafe_allow_html=True
    )

    corr = df_filtrado.select_dtypes(include=np.number).corr()

    fig, ax = plt.subplots(figsize=(10,8))

    sn.heatmap(
        corr,
        annot=True,
        cmap="coolwarm",
        ax=ax
    )

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
