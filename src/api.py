import requests

def pegar_dados_PIB(country_code):

    # Pegando dados da API gratuita World Bank
    url = f"https://api.worldbank.org/v2/country/{country_code}/indicator/NY.GDP.MKTP.CD?format=json&date=2023:2024"

    try:
        resposta = requests.get(url)

        resposta.raise_for_status()

        dados = resposta.json()

        return dados[1]
        
    except Exception as e:
        print(f"Erro: {e}")


def pegar_dados_desemprego(country_code):

    url = f"https://api.worldbank.org/v2/country/{country_code}/indicator/SL.UEM.TOTL.ZS?format=json&date=2023:2024"

    try:
        resposta = requests.get(url)

        resposta.raise_for_status()

        dados = resposta.json()

        return dados[1]
        
    except Exception as e:
        print(f"Erro: {e}")
