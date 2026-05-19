












#                         # Código da Aula 14/05 
import streamlit as st
import seaborn as sn
import matplotlib.pyplot as plt
import pandas as pd

# st.text("Meu Primeiro Dashboard")
df = pd.read_excel("planilhao.xlsx", sheet_name="Sheet1")
# Titulo de Dashboard
st.header("Meu Dashboard")
menu = st.tabs(["Tabela", "Barras", "Pizza"])
# Expondo o df no Dashboard
with menu[0]:
        st.dataframe(df)
# Gráfico de Barras Vertical
with menu[1]:
        fig = plt.figure(figsize=(10,6)) # Tamanho do grafico
        sn.countplot(data=df, 
                x="setor", # Colocar Y="setor" deixa horizontal
                order=df['setor'].value_counts().index,
                palette="tab10")
        plt.title("Grafico de Barras por setor")
        plt.xlabel("Numero de Empresas")
        plt.ylabel("Setor")
        plt.xticks(rotation=45)
        plt.show()
        st.pyplot(fig)
# Gráfico de Pizza
with menu[2]:
        fig = plt.figure(figsize=(10,6)) # Tamanho do grafico
        setor = df["setor"].value_counts()
        plt.pie(setor, labels=setor.index,
                autopct="%1.1f%%")
        st.pyplot(fig)


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
