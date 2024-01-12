import pandas as pd


caminho_planilha = 'CDB UNIFAN 2024.1.xlsx'  
df = pd.read_excel(caminho_planilha)

# Lista de nomes a serem filtrados
nomes_a_filtrar = [
    
]

# Filtrar as linhas que contêm os nomes específicos
df_filtrado = df[df['Nome candidato'].isin(nomes_a_filtrar)]

# Atualizar a coluna 'IES' para 'UNIFAN IPIRÁ'
df_filtrado['IES'] = 'UNIFAN IPIRÁ'

# Salvar as alterações de volta na planilha
df_filtrado.to_excel('dados_filtrados.xlsx.xlsx', index=False)
