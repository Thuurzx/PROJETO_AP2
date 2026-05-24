"""
Dashboard Financeiro Premium
Versão Ultra Moderna
"""

import streamlit as st
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np

# ─────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Dashboard Financeiro",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─────────────────────────────────────────────
# CSS AVANÇADO
# ─────────────────────────────────────────────
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;700&display=swap');

* {
    font-family: 'Space Grotesk', sans-serif;
}

/* FUNDO ANIMADO */
.stApp {
    background:
        radial-gradient(circle at top left, #111827 0%, #050816 45%),
        radial-gradient(circle at bottom right, #0f172a 0%, #020617 40%);
    color: white;
    overflow-x: hidden;
}

/* EFEITO DE GRID */
.stApp::before {
    content: "";
    position: fixed;
    width: 100%;
    height: 100%;
    background-image:
        linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px);
    background-size: 40px 40px;
    z-index: -1;
}

/* CURSOR */
html, body, [class*="css"] {
    cursor: crosshair;
}

/* SIDEBAR */
[data-testid="stSidebar"] {
    background: rgba(17,24,39,0.75);
    backdrop-filter: blur(18px);
    border-right: 1px solid rgba(0,229,255,0.15);
}

/* TÍTULO */
.main-title {
    font-size: 3rem;
    font-weight: 700;
    background: linear-gradient(90deg, #00e5ff, #7c3aed, #00e5ff);
    background-size: 200% auto;

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    animation: shine 6s linear infinite;
    margin-bottom: 0;
}

@keyframes shine {
    to {
        background-position: 200% center;
    }
}

.main-subtitle {
    color: #94a3b8;
    margin-bottom: 2rem;
    font-size: 1.1rem;
}

/* KPI CARDS */
.kpi-card {
    background: rgba(17,24,39,0.55);
    border: 1px solid rgba(255,255,255,0.08);
    backdrop-filter: blur(20px);

    border-radius: 24px;
    padding: 1.7rem;

    transition: 0.35s ease;

    box-shadow:
        0 0 0 rgba(0,0,0,0),
        0 0 30px rgba(0,229,255,0.04);
}

.kpi-card:hover {
    transform: translateY(-8px) scale(1.02);

    border: 1px solid rgba(0,229,255,0.45);

    box-shadow:
        0 0 25px rgba(0,229,255,0.25),
        0 0 60px rgba(124,58,237,0.15);
}

/* TEXTO KPI */
.kpi-label {
    color: #94a3b8;
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.kpi-value {
    font-size: 2.3rem;
    font-weight: 700;
    color: white;
    margin-top: 10px;
}

/* TABS */
.stTabs [data-baseweb="tab-list"] {
    gap: 12px;
}

.stTabs [data-baseweb="tab"] {
    background: rgba(255,255,255,0.04);
    border-radius: 14px;
    padding: 10px 20px;

    transition: 0.3s;
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(90deg, #00e5ff, #7c3aed);
    color: white !important;
}

/* SECTION TITLE */
.section-title {
    font-size: 1.2rem;
    font-weight: 600;
    margin-bottom: 1rem;

    color: #00e5ff;
}

/* DATAFRAME */
[data-testid="stDataFrame"] {
    border-radius: 20px;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.08);
}

/* SCROLLBAR */
::-webkit-scrollbar {
    width: 10px;
}

::-webkit-scrollbar-thumb {
    background: linear-gradient(#00e5ff, #7c3aed);
    border-radius: 20px;
}

/* BOTÕES */
.stButton>button {
    background: linear-gradient(90deg, #00e5ff, #7c3aed);
    border: none;
    border-radius: 12px;
    color: white;

    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.05);
    box-shadow: 0 0 20px rgba(0,229,255,0.4);
}

/* REMOVE STREAMLIT */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# DADOS
# ─────────────────────────────────────────────
@st.cache_data
def carregar_dados():
    return pd.read_excel("planilhao.xlsx")

df = carregar_dados()

# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────
st.sidebar.markdown("## ⚡ Filtros Inteligentes")

setores = st.sidebar.multiselect(
    "Setores",
    options=df["setor"].unique(),
    default=df["setor"].unique()
)

df_filtrado = df[df["setor"].isin(setores)]

# ─────────────────────────────────────────────
# TÍTULO
# ─────────────────────────────────────────────
st.markdown(
    '<div class="main-title">💎 Dashboard Financeiro</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-subtitle">Análise avançada de performance corporativa</div>',
    unsafe_allow_html=True
)

# ─────────────────────────────────────────────
# KPIs
# ─────────────────────────────────────────────
c1, c2, c3, c4 = st.columns(4)

kpis = [
    ("Empresas", len(df_filtrado)),
    ("Setores", df_filtrado["setor"].nunique()),
    ("ROE Médio", f'{df_filtrado["roe"].mean():.2f}%'),
    ("ROE Máximo", f'{df_filtrado["roe"].max():.2f}%')
]

for col, (label, value) in zip([c1,c2,c3,c4], kpis):

    with col:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">{label}</div>
            <div class="kpi-value">{value}</div>
        </div>
        """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
# TABS
# ─────────────────────────────────────────────
tabs = st.tabs([
    "📋 Dados",
    "📊 Setores",
    "🥧 Distribuição",
    "📈 ROE"
])

# ─────────────────────────────────────────────
# TABELA
# ─────────────────────────────────────────────
with tabs[0]:

    st.markdown(
        '<div class="section-title">Base Financeira</div>',
        unsafe_allow_html=True
    )

    st.dataframe(
        df_filtrado,
        use_container_width=True,
        height=500
    )

# ─────────────────────────────────────────────
# BARRAS
# ─────────────────────────────────────────────
with tabs[1]:

    st.markdown(
        '<div class="section-title">Empresas por Setor</div>',
        unsafe_allow_html=True
    )

    fig, ax = plt.subplots(figsize=(12,6))

    fig.patch.set_facecolor("#0b1120")
    ax.set_facecolor("#0b1120")

    contagem = df_filtrado["setor"].value_counts()

    sn.barplot(
        x=contagem.index,
        y=contagem.values,
        palette="mako",
        ax=ax
    )

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    ax.tick_params(colors='white')
    ax.yaxis.label.set_color('white')
    ax.xaxis.label.set_color('white')
    ax.title.set_color('white')

    ax.set_title("Quantidade de Empresas")

    plt.xticks(rotation=30)

    st.pyplot(fig)

# ─────────────────────────────────────────────
# PIZZA
# ─────────────────────────────────────────────
with tabs[2]:

    st.markdown(
        '<div class="section-title">Distribuição dos Setores</div>',
        unsafe_allow_html=True
    )

    fig, ax = plt.subplots(figsize=(8,8))

    fig.patch.set_facecolor("#0b1120")

    setores_count = df_filtrado["setor"].value_counts()

    ax.pie(
        setores_count,
        labels=setores_count.index,
        autopct='%1.1f%%',
        wedgeprops=dict(width=0.45),
        pctdistance=0.8
    )

    centre_circle = plt.Circle((0,0),0.55,fc='#0b1120')
    fig.gca().add_artist(centre_circle)

    st.pyplot(fig)

# ─────────────────────────────────────────────
# HISTOGRAMA
# ─────────────────────────────────────────────
with tabs[3]:

    st.markdown(
        '<div class="section-title">Distribuição do ROE</div>',
        unsafe_allow_html=True
    )

    fig, ax = plt.subplots(figsize=(12,6))

    fig.patch.set_facecolor("#0b1120")
    ax.set_facecolor("#0b1120")

    sn.histplot(
        df_filtrado["roe"],
        bins=25,
        kde=True,
        color="#00e5ff",
        ax=ax
    )

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    ax.tick_params(colors='white')

    ax.set_title(
        "Distribuição de Retorno sobre Patrimônio",
        color="white",
        fontsize=16
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
