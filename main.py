# """
# Dashboard Financeiro Premium
# Versão Ultra Moderna
# """

# import streamlit as st
# import pandas as pd
# import seaborn as sn
# import matplotlib.pyplot as plt
# import numpy as np

# # ─────────────────────────────────────────────
# # CONFIGURAÇÃO
# # ─────────────────────────────────────────────
# st.set_page_config(
#     page_title="Dashboard Financeiro",
#     page_icon="💎",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # ─────────────────────────────────────────────
# # CSS PREMIUM
# # ─────────────────────────────────────────────
# st.markdown("""
# <style>

# @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;700&display=swap');

# * {
#     font-family: 'Space Grotesk', sans-serif;
# }

# /* FUNDO */
# .stApp {

#     background:
#         radial-gradient(circle at top left, #111827 0%, #050816 45%),
#         radial-gradient(circle at bottom right, #0f172a 0%, #020617 40%);

#     color: white;
#     overflow-x: hidden;
# }

# /* GRID NO FUNDO */
# .stApp::before {

#     content: "";

#     position: fixed;

#     width: 100%;
#     height: 100%;

#     background-image:
#         linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px),
#         linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px);

#     background-size: 40px 40px;

#     z-index: -1;
# }

# /* CURSOR */
# html, body, [class*="css"] {
#     cursor: crosshair;
# }

# /* SIDEBAR */
# [data-testid="stSidebar"] {

#     background: rgba(17,24,39,0.78);

#     backdrop-filter: blur(20px);

#     border-right: 1px solid rgba(0,229,255,0.15);
# }

# /* TÍTULO */
# .main-title {

#     font-size: 3rem;
#     font-weight: 700;

#     background: linear-gradient(
#         90deg,
#         #00e5ff,
#         #7c3aed,
#         #00e5ff
#     );

#     background-size: 200% auto;

#     -webkit-background-clip: text;
#     -webkit-text-fill-color: transparent;

#     animation: shine 6s linear infinite;

#     margin-bottom: 0;
# }

# @keyframes shine {

#     to {
#         background-position: 200% center;
#     }
# }

# /* SUBTÍTULO */
# .main-subtitle {

#     color: #94a3b8;

#     margin-bottom: 2rem;

#     font-size: 1.05rem;
# }

# /* KPI CARDS */
# .kpi-card {

#     background: rgba(17,24,39,0.55);

#     border: 1px solid rgba(255,255,255,0.08);

#     backdrop-filter: blur(18px);

#     border-radius: 24px;

#     padding: 1.7rem;

#     transition: 0.35s ease;

#     box-shadow:
#         0 0 30px rgba(0,229,255,0.04);
# }

# .kpi-card:hover {

#     transform: translateY(-8px) scale(1.02);

#     border: 1px solid rgba(0,229,255,0.45);

#     box-shadow:
#         0 0 25px rgba(0,229,255,0.25),
#         0 0 60px rgba(124,58,237,0.15);
# }

# /* TEXTO KPI */
# .kpi-label {

#     color: #94a3b8;

#     font-size: 0.85rem;

#     text-transform: uppercase;

#     letter-spacing: 1px;
# }

# .kpi-value {

#     font-size: 2.3rem;

#     font-weight: 700;

#     color: white;

#     margin-top: 10px;
# }

# /* TÍTULOS DE SESSÃO */
# .section-title {

#     font-size: 1.2rem;

#     font-weight: 600;

#     margin-bottom: 1rem;

#     color: #00e5ff;
# }

# /* TABS */
# .stTabs [data-baseweb="tab-list"] {

#     gap: 12px;
# }

# .stTabs [data-baseweb="tab"] {

#     background: rgba(255,255,255,0.04);

#     border-radius: 14px;

#     padding: 10px 20px;

#     transition: 0.3s;
# }

# .stTabs [aria-selected="true"] {

#     background: linear-gradient(
#         90deg,
#         #00e5ff,
#         #7c3aed
#     );

#     color: white !important;
# }

# /* DATAFRAME */
# [data-testid="stDataFrame"] {

#     border-radius: 20px;

#     overflow: hidden;

#     border: 1px solid rgba(255,255,255,0.08);
# }

# /* MULTISELECT PREMIUM */
# [data-baseweb="select"] > div {

#     background: rgba(2,6,23,0.88) !important;

#     border: 1px solid rgba(255,255,255,0.08) !important;

#     border-radius: 18px !important;

#     min-height: 65px;

#     padding-top: 6px;
#     padding-bottom: 6px;

#     transition: 0.3s;
# }

# /* HOVER SELECT */
# [data-baseweb="select"] > div:hover {

#     border: 1px solid rgba(0,229,255,0.45) !important;

#     box-shadow:
#         0 0 15px rgba(0,229,255,0.18);
# }

# /* TAGS */
# [data-baseweb="tag"] {

#     background: linear-gradient(
#         135deg,
#         #7c3aed,
#         #00e5ff
#     ) !important;

#     border-radius: 12px !important;

#     border: none !important;

#     color: white !important;
# }

# /* DROPDOWN */
# div[role="listbox"] {

#     background: rgba(15,23,42,0.98) !important;

#     border-radius: 18px !important;

#     border: 1px solid rgba(255,255,255,0.08);

#     padding: 8px;

#     backdrop-filter: blur(20px);

#     z-index: 999999 !important;
# }

# /* ITENS */
# div[role="option"] {

#     border-radius: 12px;

#     margin-bottom: 4px;
# }

# /* HOVER DOS ITENS */
# div[role="option"]:hover {

#     background: rgba(0,229,255,0.12) !important;
# }

# /* SCROLLBAR */
# ::-webkit-scrollbar {

#     width: 10px;
# }

# ::-webkit-scrollbar-thumb {

#     background: linear-gradient(
#         #00e5ff,
#         #7c3aed
#     );

#     border-radius: 20px;
# }

# /* REMOVE STREAMLIT */
# #MainMenu {visibility: hidden;}
# footer {visibility: hidden;}
# header {visibility: hidden;}

# </style>
# """, unsafe_allow_html=True)

# # ─────────────────────────────────────────────
# # CARREGAR DADOS
# # ─────────────────────────────────────────────
# @st.cache_data
# def carregar_dados():
#     return pd.read_excel("planilhao.xlsx")

# df = carregar_dados()

# # ─────────────────────────────────────────────
# # SIDEBAR
# # ─────────────────────────────────────────────
# st.sidebar.markdown("## ⚡ Filtros Inteligentes")

# setores = st.sidebar.multiselect(
#     "Setores",
#     options=sorted(df["setor"].unique()),
#     default=sorted(df["setor"].unique()),
#     placeholder="Escolha os setores..."
# )

# # FILTRO
# df_filtrado = df[df["setor"].isin(setores)]

# # ─────────────────────────────────────────────
# # TÍTULO
# # ─────────────────────────────────────────────
# st.markdown(
#     '<div class="main-title">💎 Dashboard Financeiro</div>',
#     unsafe_allow_html=True
# )

# st.markdown(
#     '<div class="main-subtitle">Análise avançada de performance corporativa</div>',
#     unsafe_allow_html=True
# )

# # ─────────────────────────────────────────────
# # KPIs
# # ─────────────────────────────────────────────
# c1, c2, c3, c4 = st.columns(4)

# kpis = [
#     ("Empresas", len(df_filtrado)),
#     ("Setores", df_filtrado["setor"].nunique()),
#     ("ROE Médio", f'{df_filtrado["roe"].mean():.2f}%'),
#     ("ROE Máximo", f'{df_filtrado["roe"].max():.2f}%')
# ]

# for col, (label, value) in zip([c1, c2, c3, c4], kpis):

#     with col:

#         st.markdown(f"""
#         <div class="kpi-card">
#             <div class="kpi-label">{label}</div>
#             <div class="kpi-value">{value}</div>
#         </div>

# # ─────────────────────────────────────────────
# # TABS
# # ─────────────────────────────────────────────
# tabs = st.tabs([
#     "📋 Dados",
#     "📊 Setores",
#     "🥧 Distribuição",
#     "📈 ROE"
# ])

# # ─────────────────────────────────────────────
# # TABELA
# # ─────────────────────────────────────────────
# with tabs[0]:

#     st.markdown(
#         '<div class="section-title">Base Financeira</div>',
#         unsafe_allow_html=True
#     )

#     st.dataframe(
#         df_filtrado,
#         use_container_width=True,
#         height=520
#     )

# # ─────────────────────────────────────────────
# # GRÁFICO DE BARRAS
# # ─────────────────────────────────────────────
# with tabs[1]:

#     st.markdown(
#         '<div class="section-title">Empresas por Setor</div>',
#         unsafe_allow_html=True
#     )

#     fig, ax = plt.subplots(figsize=(14,7))

#     fig.patch.set_facecolor("#020617")
#     ax.set_facecolor("#020617")

#     contagem = df_filtrado["setor"].value_counts()

#     sn.barplot(
#         x=contagem.values,
#         y=contagem.index,
#         palette="blend:#00e5ff,#7c3aed",
#         ax=ax
#     )

#     # REMOVE BORDAS
#     ax.spines['top'].set_visible(False)
#     ax.spines['right'].set_visible(False)
#     ax.spines['left'].set_visible(False)
#     ax.spines['bottom'].set_visible(False)

#     # GRID
#     ax.grid(
#         axis='x',
#         linestyle='--',
#         alpha=0.15
#     )

#     # TEXTO
#     ax.tick_params(
#         colors='white',
#         labelsize=12
#     )

#     ax.set_xlabel(
#         "Quantidade",
#         color="white",
#         fontsize=13
#     )

#     ax.set_ylabel("")

#     ax.set_title(
#         "Quantidade de Empresas por Setor",
#         color="white",
#         fontsize=18,
#         pad=20
#     )

#     # VALORES NAS BARRAS
#     for i, v in enumerate(contagem.values):

#         ax.text(
#             v + 0.3,
#             i,
#             str(v),
#             color='white',
#             va='center',
#             fontsize=11
#         )

#     plt.tight_layout()

#     st.pyplot(fig)

# # ─────────────────────────────────────────────
# # DONUT CHART
# # ─────────────────────────────────────────────
# with tabs[2]:

#     st.markdown(
#         '<div class="section-title">Distribuição dos Setores</div>',
#         unsafe_allow_html=True
#     )

#     fig, ax = plt.subplots(figsize=(10,10))

#     fig.patch.set_facecolor("#020617")
#     ax.set_facecolor("#020617")

#     setores_count = df_filtrado["setor"].value_counts()

#     cores = sn.color_palette(
#         "blend:#00e5ff,#7c3aed",
#         len(setores_count)
#     )

#     wedges, texts, autotexts = ax.pie(
#         setores_count,
#         labels=None,
#         autopct='%1.1f%%',
#         startangle=90,
#         pctdistance=0.82,
#         colors=cores,
#         wedgeprops=dict(
#             width=0.35,
#             edgecolor="#020617",
#             linewidth=2
#         )
#     )

#     # TEXTO %
#     for autotext in autotexts:

#         autotext.set_color("white")
#         autotext.set_fontsize(13)
#         autotext.set_weight("bold")

#     # CENTRO
#     centre_circle = plt.Circle(
#         (0,0),
#         0.58,
#         fc='#020617'
#     )

#     fig.gca().add_artist(centre_circle)

#     # LEGENDA
#     ax.legend(
#         wedges,
#         setores_count.index,
#         title="Setores",
#         loc="center left",
#         bbox_to_anchor=(1, 0.5),
#         frameon=False,
#         labelcolor="white",
#         title_fontsize=14,
#         fontsize=12
#     )

#     plt.tight_layout()

#     st.pyplot(fig)

# # ─────────────────────────────────────────────
# # HISTOGRAMA
# # ─────────────────────────────────────────────
# with tabs[3]:

#     st.markdown(
#         '<div class="section-title">Distribuição do ROE</div>',
#         unsafe_allow_html=True
#     )

#     fig, ax = plt.subplots(figsize=(12,6))

#     fig.patch.set_facecolor("#020617")
#     ax.set_facecolor("#020617")

#     sn.histplot(
#         df_filtrado["roe"],
#         bins=25,
#         kde=True,
#         color="#00e5ff",
#         ax=ax
#     )

#     ax.spines['top'].set_visible(False)
#     ax.spines['right'].set_visible(False)

#     ax.tick_params(colors='white')

#     ax.set_title(
#         "Distribuição de Retorno sobre Patrimônio",
#         color="white",
#         fontsize=16
#     )

#     plt.tight_layout()

#     st.pyplot(fig)

"""
Dashboard Financeiro Premium
Versão Ultra Moderna — Revisado e Completo
"""
 
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
 
# ─────────────────────────────────────────────
# CONFIGURAÇÃO
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Dashboard Financeiro",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)
[data-testid="stSidebar"][aria-expanded="false"] {
    display: block !important;
    width: 21rem !important;
    transform: none !important;
}
 
# ─────────────────────────────────────────────
# CSS PREMIUM
# ─────────────────────────────────────────────
st.markdown("""
<style>
 
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;700&display=swap');
 
* {
    font-family: 'Space Grotesk', sans-serif;
}
 
/* FUNDO */
.stApp {
    background:
        radial-gradient(circle at top left, #111827 0%, #050816 45%),
        radial-gradient(circle at bottom right, #0f172a 0%, #020617 40%);
    color: white;
    overflow-x: hidden;
}
 
/* GRID NO FUNDO */
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
    background: rgba(17,24,39,0.78);
    backdrop-filter: blur(20px);
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
    to { background-position: 200% center; }
}
 
/* SUBTÍTULO */
.main-subtitle {
    color: #94a3b8;
    margin-bottom: 2rem;
    font-size: 1.05rem;
}
 
/* KPI CARDS */
.kpi-card {
    background: rgba(17,24,39,0.55);
    border: 1px solid rgba(255,255,255,0.08);
    backdrop-filter: blur(18px);
    border-radius: 24px;
    padding: 1.7rem;
    transition: 0.35s ease;
    box-shadow: 0 0 30px rgba(0,229,255,0.04);
     margin-bottom: 2rem;
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
 
/* TÍTULOS DE SESSÃO */
.section-title {
    font-size: 1.2rem;
    font-weight: 600;
    margin-bottom: 1rem;
    color: #00e5ff;
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
 
/* DATAFRAME */
[data-testid="stDataFrame"] {
    border-radius: 20px;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.08);
}
 
/* MULTISELECT PREMIUM */
[data-baseweb="select"] > div {
    background: rgba(2,6,23,0.88) !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    border-radius: 18px !important;
    min-height: 65px;
    padding-top: 6px;
    padding-bottom: 6px;
    transition: 0.3s;
}
 
[data-baseweb="select"] > div:hover {
    border: 1px solid rgba(0,229,255,0.45) !important;
    box-shadow: 0 0 15px rgba(0,229,255,0.18);
}
 
/* TAGS */
[data-baseweb="tag"] {
    background: linear-gradient(135deg, #7c3aed, #00e5ff) !important;
    border-radius: 12px !important;
    border: none !important;
    color: white !important;
}
 
/* DROPDOWN */
div[role="listbox"] {
    background: rgba(15,23,42,0.98) !important;
    border-radius: 18px !important;
    border: 1px solid rgba(255,255,255,0.08);
    padding: 8px;
    backdrop-filter: blur(20px);
    z-index: 999999 !important;
}
 
div[role="option"] {
    border-radius: 12px;
    margin-bottom: 4px;
}
 
div[role="option"]:hover {
    background: rgba(0,229,255,0.12) !important;
}
 
/* SCROLLBAR */
::-webkit-scrollbar {
    width: 10px;
}
 
::-webkit-scrollbar-thumb {
    background: linear-gradient(#00e5ff, #7c3aed);
    border-radius: 20px;
}
 
/* REMOVE STREAMLIT */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
[data-testid="stSidebarCollapsedControl"] {
    visibility: visible !important;
    display: block !important;
    position: fixed !important;
    top: 14px !important;
    left: 14px !important;
    z-index: 999999 !important;
} 
 
/* ═══════════════════════════════════════════
   SIDEBAR APRIMORADA
═══════════════════════════════════════════ */
 
/* Botões "Todos / Limpar" */
[data-testid="stSidebar"] .stButton > button {
    border-radius: 12px !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.8rem !important;
    padding: 8px 0 !important;
    width: 100% !important;
    transition: 0.3s !important;
    border: 1px solid rgba(0,229,255,0.25) !important;
    background: rgba(0,229,255,0.07) !important;
    color: #00e5ff !important;
}
 
[data-testid="stSidebar"] .stButton > button:hover {
    background: rgba(0,229,255,0.18) !important;
    box-shadow: 0 0 14px rgba(0,229,255,0.2) !important;
}
 
/* Campo de busca */
[data-testid="stSidebar"] .stTextInput input {
    background: rgba(255,255,255,0.04) !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    border-radius: 12px !important;
    color: white !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 0.85rem !important;
    padding: 10px 14px !important;
    transition: 0.3s !important;
}
 
[data-testid="stSidebar"] .stTextInput input:focus {
    border-color: rgba(0,229,255,0.4) !important;
    box-shadow: 0 0 12px rgba(0,229,255,0.12) !important;
}
 
[data-testid="stSidebar"] .stTextInput input::placeholder {
    color: #475569 !important;
}
 
/* Checkboxes como cards */
[data-testid="stSidebar"] .stCheckbox {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 14px;
    padding: 8px 14px !important;
    margin-bottom: 5px !important;
    transition: 0.25s;
}
 
[data-testid="stSidebar"] .stCheckbox:hover {
    background: rgba(0,229,255,0.06) !important;
    border-color: rgba(0,229,255,0.22) !important;
}
 
[data-testid="stSidebar"] .stCheckbox label {
    color: #cbd5e1 !important;
    font-size: 0.83rem !important;
    font-weight: 500 !important;
    cursor: pointer !important;
    width: 100% !important;
}
 
/* Divider da sidebar */
.sb-divider {
    height: 1px;
    background: linear-gradient(
        90deg,
        transparent,
        rgba(0,229,255,0.2),
        transparent
    );
    margin: 18px 0;
}
 
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
todos_setores    = sorted(df["setor"].unique())
contagem_setor   = df["setor"].value_counts()
 
if "setores_sel" not in st.session_state:
    st.session_state.setores_sel = {s: True for s in todos_setores}
 
# ── HEADER ────────────────────────────────────
st.sidebar.markdown("""
<div style="
    padding: 6px 0 22px 0;
    border-bottom: 1px solid rgba(0,229,255,0.15);
    margin-bottom: 20px;
">
    <div style="display:flex; align-items:center; gap:13px;">
        <div style="
            width:44px; height:44px;
            background: linear-gradient(135deg, #00e5ff, #7c3aed);
            border-radius: 13px;
            display: flex; align-items: center; justify-content: center;
            font-size: 22px;
            flex-shrink: 0;
        ">⚡</div>
        <div>
            <div style="font-weight:700; font-size:1rem; color:white; line-height:1.2;">
                Filtros
            </div>
            <div style="font-size:0.72rem; color:#475569; margin-top:2px;">
                Segmentação por setor
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
 
# ── AÇÕES RÁPIDAS ─────────────────────────────
col_a, col_b = st.sidebar.columns(2)
 
if col_a.button("✓  Todos", use_container_width=True):
    for s in st.session_state.setores_sel:
        st.session_state.setores_sel[s] = True
    st.rerun()
 
if col_b.button("✗  Limpar", use_container_width=True):
    for s in st.session_state.setores_sel:
        st.session_state.setores_sel[s] = False
    st.rerun()
 
# ── BUSCA ─────────────────────────────────────
st.sidebar.markdown("<div style='margin-top:14px;'></div>", unsafe_allow_html=True)
 
busca = st.sidebar.text_input(
    "busca",
    placeholder="🔍  Buscar setor...",
    label_visibility="collapsed"
)
 
st.sidebar.markdown("<div class='sb-divider'></div>", unsafe_allow_html=True)
 
# ── CHECKBOXES POR SETOR ──────────────────────
setores_visiveis = (
    [s for s in todos_setores if busca.strip().lower() in s.lower()]
    if busca.strip() else todos_setores
)
 
if not setores_visiveis:
    st.sidebar.markdown(
        "<div style='color:#475569; font-size:0.82rem; text-align:center; padding:12px 0;'>"
        "Nenhum setor encontrado.</div>",
        unsafe_allow_html=True
    )
 
for setor in setores_visiveis:
    n = contagem_setor.get(setor, 0)
    novo_valor = st.sidebar.checkbox(
        f"{setor}   · {n}",
        value=st.session_state.setores_sel.get(setor, True),
        key=f"chk_{setor}"
    )
    st.session_state.setores_sel[setor] = novo_valor
 
# ── FILTRO RESULTANTE ─────────────────────────
setores    = [s for s, v in st.session_state.setores_sel.items() if v]
df_filtrado = df[df["setor"].isin(setores)]
 
# ── CARD RESUMO ───────────────────────────────
n_set = len(setores)
n_emp = len(df_filtrado)
 
st.sidebar.markdown("<div class='sb-divider'></div>", unsafe_allow_html=True)
 
st.sidebar.markdown(f"""
<div style="
    background: rgba(0,229,255,0.04);
    border: 1px solid rgba(0,229,255,0.12);
    border-radius: 18px;
    padding: 16px 14px;
    text-align: center;
">
    <div style="display:flex; justify-content:space-around; align-items:center;">
        <div>
            <div style="
                font-size: 1.7rem; font-weight: 700;
                background: linear-gradient(90deg, #00e5ff, #7c3aed);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            ">{n_set}</div>
            <div style="font-size:0.73rem; color:#475569; margin-top:2px;">Setores</div>
        </div>
        <div style="width:1px; height:36px; background:rgba(255,255,255,0.07);"></div>
        <div>
            <div style="
                font-size: 1.7rem; font-weight: 700;
                background: linear-gradient(90deg, #7c3aed, #00e5ff);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            ">{n_emp}</div>
            <div style="font-size:0.73rem; color:#475569; margin-top:2px;">Empresas</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
 
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
# GUARDA CONTRA SELEÇÃO VAZIA
# ─────────────────────────────────────────────
if df_filtrado.empty:
    st.warning("⚠️ Nenhum setor selecionado. Escolha ao menos um no menu lateral.")
    st.stop()
 
# ─────────────────────────────────────────────
# KPIs
# ─────────────────────────────────────────────
c1, c2, c3, c4 = st.columns(4, gap="large")
 
kpis = [
    ("Empresas",   len(df_filtrado)),
    ("Setores",    df_filtrado["setor"].nunique()),
    ("ROE Médio",  f'{df_filtrado["roe"].mean():.2f}%'),
    ("ROE Máximo", f'{df_filtrado["roe"].max():.2f}%'),
]
 
for col, (label, value) in zip([c1, c2, c3, c4], kpis):
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
        height=520
    )
 
# ─────────────────────────────────────────────
# GRÁFICO DE BARRAS
# ─────────────────────────────────────────────
with tabs[1]:
 
    st.markdown(
        '<div class="section-title">Empresas por Setor</div>',
        unsafe_allow_html=True
    )
 
    fig, ax = plt.subplots(figsize=(14, 7))
    fig.patch.set_facecolor("#020617")
    ax.set_facecolor("#020617")
 
    contagem = df_filtrado["setor"].value_counts()
 
    sns.barplot(
        x=contagem.values,
        y=contagem.index,
        palette="blend:#00e5ff,#7c3aed",
        ax=ax
    )
 
    for spine in ax.spines.values():
        spine.set_visible(False)
 
    ax.grid(axis='x', linestyle='--', alpha=0.15)
    ax.tick_params(colors='white', labelsize=12)
    ax.set_xlabel("Quantidade", color="white", fontsize=13)
    ax.set_ylabel("", color="white")
    ax.set_title(
        "Quantidade de Empresas por Setor",
        color="white",
        fontsize=18,
        pad=20
    )
 
    for i, v in enumerate(contagem.values):
        ax.text(v + 0.3, i, str(v), color='white', va='center', fontsize=11)
 
    plt.tight_layout()
    st.pyplot(fig)
 
# ─────────────────────────────────────────────
# DONUT CHART
# ─────────────────────────────────────────────
with tabs[2]:
 
    st.markdown(
        '<div class="section-title">Distribuição dos Setores</div>',
        unsafe_allow_html=True
    )
 
    fig, ax = plt.subplots(figsize=(10, 10))
    fig.patch.set_facecolor("#020617")
    ax.set_facecolor("#020617")
 
    setores_count = df_filtrado["setor"].value_counts()
    cores = sns.color_palette("blend:#00e5ff,#7c3aed", len(setores_count))
 
    # Oculta % de fatias menores que 3% para evitar sobreposição
    def autopct_limiar(pct):
        return f"{pct:.1f}%" if pct >= 3.0 else ""
 
    wedges, texts, autotexts = ax.pie(
        setores_count,
        labels=None,
        autopct=autopct_limiar,
        startangle=90,
        pctdistance=0.78,
        colors=cores,
        wedgeprops=dict(width=0.40, edgecolor="#020617", linewidth=2)
    )
 
    for autotext in autotexts:
        autotext.set_color("white")
        autotext.set_fontsize(12)
        autotext.set_weight("bold")
 
    centre_circle = plt.Circle((0, 0), 0.58, fc='#020617')
    fig.gca().add_artist(centre_circle)
 
    ax.legend(
        wedges,
        setores_count.index,
        title="Setores",
        loc="center left",
        bbox_to_anchor=(1, 0.5),
        frameon=False,
        labelcolor="white",
        title_fontsize=14,
        fontsize=12
    )
 
    plt.tight_layout()
    st.pyplot(fig)
 
# ─────────────────────────────────────────────
# HISTOGRAMA
# ─────────────────────────────────────────────
with tabs[3]:
 
    st.markdown(
        '<div class="section-title">Distribuição do ROE</div>',
        unsafe_allow_html=True
    )
 
    fig, ax = plt.subplots(figsize=(12, 6))
    fig.patch.set_facecolor("#020617")
    ax.set_facecolor("#020617")
 
    sns.histplot(
        df_filtrado["roe"],
        bins=25,
        kde=True,
        color="#00e5ff",
        ax=ax
    )
 
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)
    for spine in ["left", "bottom"]:
        ax.spines[spine].set_color((1, 1, 1, 0.15))  # tupla RGBA — matplotlib não aceita "rgba()"
 
    ax.tick_params(colors='white')
    ax.set_xlabel("ROE (%)", color="white", fontsize=13)
    ax.set_ylabel("Frequência", color="white", fontsize=13)
    ax.set_title(
        "Distribuição de Retorno sobre Patrimônio",
        color="white",
        fontsize=16
    )
 
    plt.tight_layout()
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
