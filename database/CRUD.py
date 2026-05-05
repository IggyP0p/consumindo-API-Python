import pandas as pd
import sqlite3

db_path = 'world_bank_data.db'

def salvar_dados(dados: pd.DataFrame):

    con = sqlite3.connect(db_path)

    cursor = con.cursor()

    query = "INSERT INTO comparativo_economico (pais, ano, taxa_desemprego, pib_trilhoes) VALUES (?, ?, ?, ?)"

    registros = dados.values.tolist()

    try:
        cursor.executemany(query, registros)

        con.commit()
        print("Dados salvos com sucesso")

    except Exception as e:

        print(f"Erro: {e}")
        con.rollback()

    finally:
        con.close()


def ler_dados() -> pd.DataFrame:

    con = sqlite3.connect(db_path)

    query = "SELECT * from comparativo_economico"

    try:
        df = pd.read_sql(query, con)
        return df
        
    except Exception as e:

        print(f"Erro: {e}")
        return pd.DataFrame()

    finally:
        con.close()