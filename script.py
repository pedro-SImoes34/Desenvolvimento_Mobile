import pandas as pd
import re

#carregar e separar as colunas (split)
def carregar_e_separar(caminho_arquivo):
    df_raw = pd.read_excel(caminho_arquivo)
    #divide o texto pelas vírgulas
    coluna_unica = df_raw.columns[0]
    df = df_raw[coluna_unica].str.split(',', expand=True)
    df.columns = [c.strip() for c in coluna_unica.split(',')]
    return df

df1 = carregar_e_separar('Base de Dados 1- Cadastro de Clientes.xlsx')
df2 = carregar_e_separar('Base de Dados 2- Acessos e Compras no Site.xlsx')
df3 = carregar_e_separar('Base de Dados 3- Detalhes dos Pedidos.xlsx')

#tratando duplicidades nos dados de clientes
#deixa o registro mais completo do cliente e apaga o resto
df1 = df1.sort_values(by='Telefone', ascending=False)
df1 = df1.drop_duplicates(subset=['Nome', 'Email', 'Data_Nascimento'], keep='first')

#normalização clientes
df1['Telefone'] = df1['Telefone'].apply(lambda x: re.sub(r'\D', '', str(x)) if str(x) != 'NA' else None)
df1['Data_Nascimento'] = pd.to_datetime(df1['Data_Nascimento'], errors='coerce')

#normalização acessos
df2['Valor_Carrinho'] = pd.to_numeric(df2['Valor_Carrinho'], errors='coerce')
df2['Compra_Finalizada'] = df2['Compra_Finalizada'].str.strip()

#normalização pedidos
df3['Quantidade'] = pd.to_numeric(df3['Quantidade'], errors='coerce')
df3['Preco_Unitario'] = pd.to_numeric(df3['Preco_Unitario'], errors='coerce')
df3['Data_Compra'] = pd.to_datetime(df3['Data_Compra'], errors='coerce')

#merge nos detalhes do pedido + sessão do site
df_integrado = pd.merge(df3, df2, on='ID_Sessao', how='left')

# merge integrado + dados dos clientes
df_integrado = pd.merge(df_integrado, df1, left_on='Nome_Cliente', right_on='Nome', how='left')

#apaga coluna duplicada de nome após a junção
df_integrado = df_integrado.drop(columns=['Nome'])

#salvar e mostrar o resultado final
df_integrado.to_excel('Base_Final_Integrada.xlsx', index=False)
print("Base integrada com sucesso! Shape final:", df_integrado.shape)
print(df_integrado.head())