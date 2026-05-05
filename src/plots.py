from database import CRUD as db
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def comparativo_PIB():
    
    df = pd.DataFrame
    df = db.ler_dados()

    if df.empty:
        print("Sem dados para plotar.")
        return
    
    # separando os dados de cada ano em diferentes conjuntos para plotagem
    df_2024 = df[df['ano'] == 2024]
    df_2023 = df[df['ano'] == 2023]

    # criando uma lista com nome dos paises para usar como uma das chaves do plot
    paises = df['pais'].unique().tolist()

    # coordenadas do gráfico
    x = np.arange(len(paises))
    largura = 0.35
    fig, ax = plt.subplots(figsize=(10,6))

    barras2023 = ax.bar(x - largura/2,
                    [df_2023[df_2023['pais'] == p]['pib_trilhoes'].values[0] for p in paises],
                    largura, label='2023', alpha=0.6
    )

    barras2024 = ax.bar(x + largura/2,
                        [df_2024[df_2024['pais'] == p]['pib_trilhoes'].values[0] for p in paises],
                        largura, label='2024'                    
    )
    # Diferenciando as cores para melhor visualização
    barras2023[0].set_color('blue')
    barras2024[0].set_color('darkblue')
    barras2023[1].set_color('red')
    barras2024[1].set_color('darkred')
    # os labels do gráfico, e o que tem na coordenada x e na y
    ax.set_ylabel('PIB (Trilhões US$)')
    ax.set_title('Comparativo PIB: Argentina vs Brasil (2023-2024)')
    ax.set_xticks(x)
    ax.set_xticklabels(paises)
    ax.legend(['2023 (Transparente)', '2024 (Sólido)'])

    plt.grid(axis='y', linestyle='--', alpha=0.3)
    plt.show()


def comparativo_desemprego():

    df = pd.DataFrame
    df = db.ler_dados()

    if df.empty:
        print("Sem dados para plotar.")
        return
    
    df_2024 = df[df['ano'] == 2024]
    df_2023 = df[df['ano'] == 2023]

    paises = df['pais'].unique().tolist()
    x = np.arange(len(paises))
    largura = 0.35

    fig, ax = plt.subplots(figsize=(10,6))

    barras2023 = ax.bar(x - largura/2,
                    [df_2023[df_2023['pais'] == p]['taxa_desemprego'].values[0] for p in paises],
                    largura, label='2023', alpha=0.6
    )

    barras2024 = ax.bar(x + largura/2,
                        [df_2024[df_2024['pais'] == p]['taxa_desemprego'].values[0] for p in paises],
                        largura, label='2024'                    
    )

    barras2023[0].set_color('blue')
    barras2024[0].set_color('darkblue')
    barras2023[1].set_color('red')
    barras2024[1].set_color('darkred')

    ax.set_ylabel('Taxa de desemprego')
    ax.set_title('Comparativo Desemprego: Argentina vs Brasil (2023-2024)')
    ax.set_xticks(x)
    ax.set_xticklabels(paises)
    ax.legend(['2023 (Transparente)', '2024 (Sólido)'])

    plt.grid(axis='y', linestyle='--', alpha=0.3)
    plt.show()
