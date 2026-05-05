import pandas as pd # para organizar e visualizar os dados
from database import CRUD as db
import src.api as api # para fazer chamadas a API

def run():
    paises = ['BR', 'AR']
    lista_pib = []
    lista_desemprego = []

    # Extraindo os dados da minha API para transforma-los

    for pais in paises:
        
        dados_pais = api.pegar_dados_PIB(pais)

        lista_pib.extend(dados_pais)

    for pais in paises:
        
        dados_pais = api.pegar_dados_desemprego(pais)

        lista_desemprego.extend(dados_pais)


    # Criando conjuntos de dados distintos com pandas

    df_pib = pd.DataFrame(lista_pib)
    df_desemprego = pd.DataFrame(lista_desemprego)

    # country é um dicionario, o que não entra no banco de dados, então tiramos o value de dentro que é o nome do país
    # para quando adicionar-mos no banco de dados.
    for df_temp in [df_pib, df_desemprego]:
        df_temp['country'] = df_temp['country'].apply(lambda x: x['value'] if isinstance(x, dict) else x)

    # Renomeando Values antes de juntar as tabelas
    df_pib = df_pib.rename(columns={'value': 'pib_valor'})
    df_desemprego = df_desemprego.rename(columns={'value': 'taxa_desemprego'})

    # Fazendo merge
    df_final = pd.merge(
        df_pib[['country', 'date', 'pib_valor']],
        df_desemprego[['country', 'date', 'taxa_desemprego']],
        on=['country', 'date'],
        how='outer'
    )

    # Pensei que o numero do pib em notação cientifica é ruim para visualizar então coloque em casa de trilhões
    # Saindo de '2.191132e+12' para '2.191132' e depois arredondando para '2.191' trilhões.
    df_final['pib_trilhoes'] = df_final['pib_valor'] / 1_000_000_000_000
    df_final['pib_trilhoes'] = df_final['pib_trilhoes'].round(3)

    df_final = df_final.drop(columns=['pib_valor']) # excluindo antiga coluna

    # Arredondando taxa_desemprego para os gráficos também
    df_final['taxa_desemprego'] = df_final['taxa_desemprego'].round(2)

    db.salvar_dados(df_final)