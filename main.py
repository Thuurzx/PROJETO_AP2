"""
Dashboard Financeiro Profissional
Aula 21/05 — Versão Avançada
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
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
# CSS CUSTOMIZADO — TEMA ESCURO PROFISSIONAL
# ─────────────────────────────────────────────
st.markdown("""
<style>
    /* ── Imports ── */
    @import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=DM+Sans:wght@300;400;500;600&display=swap');

    /* ── Root / Tema base ── */
    :root {
        --bg-primary:   #0a0e1a;
        --bg-card:      #111827;
        --bg-card2:     #1a2236;
        --accent:       #00e5ff;
        --accent2:      #7c3aed;
        --accent3:      #10b981;
        --text-primary: #f1f5f9;
        --text-muted:   #64748b;
        --border:       rgba(0,229,255,0.12);
        --glow:         0 0 24px rgba(0,229,255,0.15);
    }

    /* ── Background global ── */
    .stApp {
        background: var(--bg-primary);
        background-image:
            radial-gradient(ellipse at 20% 20%, rgba(124,58,237,0.08) 0%, transparent 60%),
            radial-gradient(ellipse at 80% 80%, rgba(0,229,255,0.06) 0%, transparent 60%);
        font-family: 'DM Sans', sans-serif;
    }

    /* ── Sidebar ── */
    [data-testid="stSidebar"] {
        background: var(--bg-card) !important;
        border-right: 1px solid var(--border);
    }
    [data-testid="stSidebar"] * {
        color: var(--text-primary) !important;
    }

    /* ── Título principal ── */
    .main-title {
        font-family: 'Space Mono', monospace;
        font-size: 2.2rem;
        font-weight: 700;
        background: linear-gradient(135deg, #00e5ff, #7c3aed);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.2rem;
    }
    .main-subtitle {
        color: var(--text-muted);
        font-size: 0.95rem;
        font-weight: 300;
        letter-spacing: 0.04em;
        margin-bottom: 1.5rem;
    }

    /* ── Cards KPI ── */
    .kpi-card {
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: 16px;
        padding: 1.4rem 1.6rem;
        position: relative;
        overflow: hidden;
        box-shadow: var(--glow);
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    .kpi-card:hover {
        transform: translateY(-3px);
        border-color: var(--accent);
    }
    .kpi-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 3px;
        background: linear-gradient(90deg, var(--accent), var(--accent2));
    }
    .kpi-label {
        font-size: 0.78rem;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        color: var(--text-muted);
        margin-bottom: 0.5rem;
    }
    .kpi-value {
        font-family: 'Space Mono', monospace;
        font-size: 2rem;
        font-weight: 700;
        color: var(--text-primary);
        line-height: 1;
    }
    .kpi-delta {
        font-size: 0.8rem;
        margin-top: 0.4rem;
        color: var(--accent3);
    }
    .kpi-icon {
        position: absolute;
        top: 1.2rem; right: 1.4rem;
        font-size: 1.6rem;
        opacity: 0.25;
    }

    /* ── Section titles ── */
    .section-title {
        font-family: 'Space Mono', monospace;
        font-size: 1rem;
        font-weight: 700;
        color: var(--accent);
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 1px solid var(--border);
    }

    /* ── Abas ── */
    .stTabs [data-baseweb="tab-list"] {
        background: var(--bg-card);
        border-radius: 12px;
        padding: 4px;
        border: 1px solid var(--border);
        gap: 4px;
    }
    .stTabs [data-baseweb="tab"] {
        background: transparent;
        color: var(--text-muted) !important;
        border-radius: 8px;
        font-family: 'DM Sans', sans-serif;
        font-weight: 500;
        padding: 0.5rem 1.2rem;
        transition: all 0.2s;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #00e5ff22, #7c3aed22) !important;
        color: var(--accent) !important;
        border: 1px solid var(--border) !important;
    }

    /* ── Dataframe ── */
    .stDataFrame {
        border-radius: 12px;
        overflow: hidden;
        border: 1px solid var(--border);
    }

    /* ── Divider ── */
    hr {
        border-color: var(--border) !important;
        margin: 1.5rem 0 !important;
    }

    /* ── Selectbox / multiselect ── */
    .stMultiSelect [data-baseweb="tag"] {
        background-color: rgba(0,229,255,0.15) !important;
        color: var(--accent) !important;
    }

    /* ── Download button ── */
    .stDownloadButton button {
        background: linear-gradient(135deg, #00e5ff22, #7c3aed22) !important;
        border: 1px solid var(--accent) !important;
        color: var(--accent) !important;
        border-radius: 8px !important;
        font-family: 'Space Mono', monospace !important;
        font-size: 0.8rem !important;
        letter-spacing: 0.05em !important;
        padding: 0.4rem 1rem !important;
        transition: all 0.2s !important;
    }
    .stDownloadButton button:hover {
        background: rgba(0,229,255,0.2) !important;
        box-shadow: 0 0 16px rgba(0,229,255,0.3) !important;
    }

    /* ── Slider ── */
    .stSlider [data-testid="stSliderThumb"] {
        background: var(--accent) !important;
    }

    /* ── Info box ── */
    .info-box {
        background: rgba(0,229,255,0.06);
        border: 1px solid var(--border);
        border-radius: 10px;
        padding: 0.8rem 1rem;
        font-size: 0.82rem;
        color: var(--text-muted);
        margin-top: 1rem;
    }

    /* ── Hide Streamlit branding ── */
    #MainMenu, footer, header { visibility: hidden; }
    .block-container { padding-top: 1.5rem !important; }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# PALETA DE CORES PLOTLY (COERENTE COM O TEMA)
# ─────────────────────────────────────────────
PALETTE = [
    "#00e5ff", "#7c3aed", "#10b981", "#f59e0b",
    "#ef4444", "#3b82f6", "#ec4899", "#84cc16",
    "#f97316", "#06b6d4"
]

PLOTLY_LAYOUT = dict(
    font_family="DM Sans",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font_color="#f1f5f9",
    title_font_family="Space Mono",
    title_font_color="#00e5ff",
    title_font_size=14,
    legend=dict(
        bgcolor="rgba(17,24,39,0.8)",
        bordercolor="rgba(0,229,255,0.15)",
        borderwidth=1,
    ),
    xaxis=dict(
        gridcolor="rgba(255,255,255,0.05)",
        linecolor="rgba(255,255,255,0.1)",
        zerolinecolor="rgba(255,255,255,0.1)",
    ),
    yaxis=dict(
        gridcolor="rgba(255,255,255,0.05)",
        linecolor="rgba(255,255,255,0.1)",
        zerolinecolor="rgba(255,255,255,0.1)",
    ),
    margin=dict(l=10, r=10, t=50, b=10),
)


# ─────────────────────────────────────────────
# CARREGAR DADOS
# ─────────────────────────────────────────────
@st.cache_data
def carregar_dados():
    df = pd.read_excel("planilhao.xlsx", sheet_name="Sheet1")
    # Garante tipos numéricos nas colunas principais
    for col in df.select_dtypes(include="object").columns:
        try:
            df[col] = pd.to_numeric(df[col])
        except Exception:
            pass
    return df

df = carregar_dados()

# Detectar colunas numéricas além de "setor"
num_cols = df.select_dtypes(include="number").columns.tolist()
has_roe  = "roe" in df.columns
has_pl   = "p_l" in df.columns or "pl" in df.columns or "p/l" in df.columns.str.lower()

# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='font-family:Space Mono,monospace; font-size:1.1rem;
                color:#00e5ff; font-weight:700; margin-bottom:0.3rem;'>
        ⚙ FILTROS
    </div>
    <div style='color:#64748b; font-size:0.8rem; margin-bottom:1.2rem;
                border-bottom:1px solid rgba(0,229,255,0.12); padding-bottom:0.8rem;'>
        Ajuste os filtros para explorar os dados
    </div>
    """, unsafe_allow_html=True)

    # Filtro de setor
    setores_disponiveis = sorted(df["setor"].dropna().unique().tolist())
    setores = st.multiselect(
        "Setores",
        options=setores_disponiveis,
        default=setores_disponiveis,
        placeholder="Selecione setores..."
    )

    # Filtro de ROE (slider)
    if has_roe:
        roe_min = float(df["roe"].min())
        roe_max = float(df["roe"].max())
        roe_range = st.slider(
            "Faixa de ROE",
            min_value=round(roe_min, 2),
            max_value=round(roe_max, 2),
            value=(round(roe_min, 2), round(roe_max, 2)),
            step=0.5
        )

    # Eixo X e Y para o scatter
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style='font-family:Space Mono,monospace; font-size:0.75rem;
                color:#00e5ff; text-transform:uppercase; letter-spacing:0.08em;
                margin-bottom:0.5rem;'>Scatter Plot</div>
    """, unsafe_allow_html=True)

    eixo_x = st.selectbox("Eixo X", num_cols, index=0)
    eixo_y = st.selectbox("Eixo Y", num_cols, index=min(1, len(num_cols)-1))

    # Info de linha
    st.markdown(f"""
    <div class='info-box'>
        📁 <b>{len(df)}</b> empresas no dataset<br>
        🏭 <b>{df['setor'].nunique()}</b> setores disponíveis<br>
        📐 <b>{len(num_cols)}</b> variáveis numéricas
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────
# FILTRAR DADOS
# ─────────────────────────────────────────────
df_filtrado = df[df["setor"].isin(setores)]
if has_roe:
    df_filtrado = df_filtrado[
        df_filtrado["roe"].between(roe_range[0], roe_range[1])
    ]


# ─────────────────────────────────────────────
# CABEÇALHO
# ─────────────────────────────────────────────
col_tit, col_dl = st.columns([5, 1])
with col_tit:
    st.markdown('<div class="main-title">📊 Dashboard Financeiro</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-subtitle">Análise interativa de empresas por setor · dados em tempo real</div>', unsafe_allow_html=True)
with col_dl:
    st.markdown("<br>", unsafe_allow_html=True)
    csv = df_filtrado.to_csv(index=False).encode("utf-8")
    st.download_button(
        "⬇ Exportar CSV",
        data=csv,
        file_name="dados_filtrados.csv",
        mime="text/csv"
    )


# ─────────────────────────────────────────────
# KPIs
# ─────────────────────────────────────────────
k1, k2, k3, k4, k5 = st.columns(5)

roe_medio  = df_filtrado["roe"].mean()  if has_roe else 0
roe_median = df_filtrado["roe"].median() if has_roe else 0
roe_max_v  = df_filtrado["roe"].max()   if has_roe else 0

kpis = [
    (k1, "Empresas",       len(df_filtrado),             f"{len(df_filtrado)/len(df)*100:.0f}% do total", "🏢"),
    (k2, "Setores",        df_filtrado["setor"].nunique(),"selecionados",                                  "🏭"),
    (k3, "ROE Médio",      f"{roe_medio:.2f}",            f"mediana: {roe_median:.2f}",                    "📈"),
    (k4, "ROE Máximo",     f"{roe_max_v:.2f}",            "maior rentabilidade",                           "🚀"),
    (k5, "Concentração",   f"{df_filtrado['setor'].value_counts().iloc[0] if len(df_filtrado)>0 else 0}",
                           f"empresas no setor líder",                                                      "🎯"),
]

for col, label, value, delta, icon in kpis:
    with col:
        st.markdown(f"""
        <div class="kpi-card">
            <span class="kpi-icon">{icon}</span>
            <div class="kpi-label">{label}</div>
            <div class="kpi-value">{value}</div>
            <div class="kpi-delta">▲ {delta}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.divider()


# ─────────────────────────────────────────────
# ABAS
# ─────────────────────────────────────────────
menu = st.tabs([
    "📋 Tabela",
    "📊 Barras",
    "🥧 Pizza",
    "📈 Distribuição",
    "🔵 Scatter",
    "📦 Boxplot",
    "🔥 Correlação"
])


# ── 0. TABELA ────────────────────────────────
with menu[0]:
    st.markdown('<div class="section-title">Dados Completos</div>', unsafe_allow_html=True)

    # Busca
    search = st.text_input("🔍 Buscar empresa ou setor", placeholder="Digite para filtrar...")
    df_show = df_filtrado.copy()
    if search:
        mask = df_show.apply(lambda row: row.astype(str).str.contains(search, case=False).any(), axis=1)
        df_show = df_show[mask]

    st.markdown(f"*Exibindo {len(df_show)} de {len(df_filtrado)} registros*")

    st.dataframe(
        df_show.style.background_gradient(
            subset=[c for c in ["roe"] if c in df_show.columns],
            cmap="RdYlGn"
        ),
        use_container_width=True,
        height=420
    )


# ── 1. BARRAS ────────────────────────────────
with menu[1]:
    st.markdown('<div class="section-title">Empresas por Setor</div>', unsafe_allow_html=True)

    contagem = df_filtrado["setor"].value_counts().reset_index()
    contagem.columns = ["setor", "count"]

    fig = px.bar(
        contagem,
        x="setor", y="count",
        color="count",
        color_continuous_scale=["#7c3aed", "#00e5ff"],
        text="count",
        title="Quantidade de Empresas por Setor",
    )
    fig.update_traces(
        textposition="outside",
        textfont_size=11,
        marker_line_width=0,
    )
    fig.update_layout(
        **PLOTLY_LAYOUT,
        coloraxis_showscale=False,
        xaxis_tickangle=-40,
        bargap=0.3,
    )
    st.plotly_chart(fig, use_container_width=True)

    # ROE médio por setor (segundo gráfico)
    if has_roe:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('<div class="section-title">ROE Médio por Setor</div>', unsafe_allow_html=True)

        roe_setor = (df_filtrado.groupby("setor")["roe"]
                     .mean()
                     .reset_index()
                     .sort_values("roe", ascending=True))

        fig2 = px.bar(
            roe_setor,
            x="roe", y="setor",
            orientation="h",
            color="roe",
            color_continuous_scale=["#ef4444", "#f59e0b", "#10b981"],
            text=roe_setor["roe"].round(2),
            title="ROE Médio por Setor (ordenado)"
        )
        fig2.update_traces(textposition="outside", marker_line_width=0)
        fig2.update_layout(**PLOTLY_LAYOUT, coloraxis_showscale=False, height=max(300, len(roe_setor)*38))
        st.plotly_chart(fig2, use_container_width=True)


# ── 2. PIZZA ─────────────────────────────────
with menu[2]:
    st.markdown('<div class="section-title">Distribuição dos Setores</div>', unsafe_allow_html=True)

    c1, c2 = st.columns([3, 2])

    setor_cnt = df_filtrado["setor"].value_counts().reset_index()
    setor_cnt.columns = ["setor", "count"]

    with c1:
        fig = px.pie(
            setor_cnt,
            values="count",
            names="setor",
            hole=0.45,
            color_discrete_sequence=PALETTE,
            title="Composição por Setor"
        )
        fig.update_traces(
            textposition="outside",
            textinfo="label+percent",
            pull=[0.03]*len(setor_cnt),
        )
        fig.update_layout(**PLOTLY_LAYOUT, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        # Treemap como alternativa
        fig2 = px.treemap(
            setor_cnt,
            path=["setor"],
            values="count",
            color="count",
            color_continuous_scale=["#1a2236", "#7c3aed", "#00e5ff"],
            title="Treemap dos Setores"
        )
        fig2.update_layout(**PLOTLY_LAYOUT, coloraxis_showscale=False)
        fig2.update_traces(textinfo="label+value+percent root")
        st.plotly_chart(fig2, use_container_width=True)


# ── 3. DISTRIBUIÇÃO / HISTOGRAMA ─────────────
with menu[3]:
    st.markdown('<div class="section-title">Distribuição por Variável</div>', unsafe_allow_html=True)

    col_sel, col_modo = st.columns([2, 2])
    with col_sel:
        var_dist = st.selectbox("Variável", num_cols, key="var_dist")
    with col_modo:
        modo = st.selectbox("Separar por setor?", ["Global", "Por Setor"])

    if modo == "Global":
        fig = px.histogram(
            df_filtrado,
            x=var_dist,
            nbins=30,
            marginal="violin",
            color_discrete_sequence=["#00e5ff"],
            title=f"Distribuição de {var_dist.upper()}"
        )
    else:
        setores_hist = st.multiselect(
            "Setores para comparar",
            df_filtrado["setor"].unique().tolist(),
            default=df_filtrado["setor"].unique().tolist()[:4],
            key="hist_setor"
        )
        fig = px.histogram(
            df_filtrado[df_filtrado["setor"].isin(setores_hist)],
            x=var_dist,
            color="setor",
            nbins=25,
            barmode="overlay",
            opacity=0.7,
            color_discrete_sequence=PALETTE,
            title=f"Distribuição de {var_dist.upper()} por Setor"
        )

    fig.update_layout(**PLOTLY_LAYOUT)
    st.plotly_chart(fig, use_container_width=True)

    # Estatísticas descritivas
    st.markdown('<div class="section-title">Estatísticas Descritivas</div>', unsafe_allow_html=True)
    desc = df_filtrado[num_cols].describe().T.round(3)
    st.dataframe(desc.style.background_gradient(cmap="Blues"), use_container_width=True)


# ── 4. SCATTER ───────────────────────────────
with menu[4]:
    st.markdown('<div class="section-title">Dispersão entre Variáveis</div>', unsafe_allow_html=True)

    col_s1, col_s2, col_s3 = st.columns([2, 2, 1])
    with col_s1:
        sx = st.selectbox("Eixo X", num_cols, index=0, key="sx")
    with col_s2:
        sy = st.selectbox("Eixo Y", num_cols, index=min(1, len(num_cols)-1), key="sy")
    with col_s3:
        trendline = st.checkbox("Tendência", value=True)

    nome_col = [c for c in df.columns if c not in num_cols and c != "setor"]

    fig = px.scatter(
        df_filtrado,
        x=sx, y=sy,
        color="setor",
        color_discrete_sequence=PALETTE,
        hover_name=nome_col[0] if nome_col else None,
        hover_data={sx: ":.2f", sy: ":.2f"},
        trendline="ols" if trendline else None,
        trendline_color_override="white",
        size_max=14,
        opacity=0.8,
        title=f"{sy.upper()} vs {sx.upper()} por Setor"
    )
    fig.update_traces(marker=dict(size=9, line=dict(width=0.5, color="#1a2236")))
    fig.update_layout(**PLOTLY_LAYOUT)
    st.plotly_chart(fig, use_container_width=True)


# ── 5. BOXPLOT ───────────────────────────────
with menu[5]:
    st.markdown('<div class="section-title">Boxplot por Setor</div>', unsafe_allow_html=True)

    var_box = st.selectbox("Variável", num_cols, key="var_box")

    fig = px.box(
        df_filtrado,
        x="setor",
        y=var_box,
        color="setor",
        color_discrete_sequence=PALETTE,
        points="outliers",
        title=f"Distribuição de {var_box.upper()} por Setor",
        notched=True,
    )
    fig.update_layout(
        **PLOTLY_LAYOUT,
        showlegend=False,
        xaxis_tickangle=-40
    )
    st.plotly_chart(fig, use_container_width=True)


# ── 6. CORRELAÇÃO ────────────────────────────
with menu[6]:
    st.markdown('<div class="section-title">Heatmap de Correlação</div>', unsafe_allow_html=True)

    corr = df_filtrado[num_cols].corr().round(2)

    fig = go.Figure(data=go.Heatmap(
        z=corr.values,
        x=corr.columns.tolist(),
        y=corr.columns.tolist(),
        colorscale=[
            [0.0,  "#ef4444"],
            [0.5,  "#1a2236"],
            [1.0,  "#00e5ff"],
        ],
        zmid=0,
        text=corr.values.round(2),
        texttemplate="%{text}",
        textfont_size=10,
        hoverongaps=False,
    ))
    fig.update_layout(
        **PLOTLY_LAYOUT,
        title="Correlação entre Variáveis Numéricas",
        height=max(400, len(num_cols) * 55)
    )
    st.plotly_chart(fig, use_container_width=True)

    # Interpretação automática
    st.markdown('<div class="section-title">Correlações Mais Fortes</div>', unsafe_allow_html=True)
    corr_pairs = (corr.where(np.triu(np.ones(corr.shape), k=1).astype(bool))
                      .stack()
                      .reset_index())
    corr_pairs.columns = ["Var A", "Var B", "Correlação"]
    corr_pairs["|r|"] = corr_pairs["Correlação"].abs()
    top_corr = corr_pairs.sort_values("|r|", ascending=False).head(10)

    st.dataframe(
        top_corr[["Var A", "Var B", "Correlação"]].style
            .bar(subset=["Correlação"], color=["#ef4444", "#10b981"], vmin=-1, vmax=1)
            .format({"Correlação": "{:.3f}"}),
        use_container_width=True,
        hide_index=True
    )


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
