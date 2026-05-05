import sqlite3

def create_table():
    con = sqlite3.connect('world_bank_data.db')
    cursor = con.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS comparativo_economico (
            pais TEXT,
            ano INTEGER,
            pib_trilhoes REAL,
            taxa_desemprego REAL,
            PRIMARY KEY (pais, ano) -- Garante que não haverá duplicatas para o mesmo ano/país
        )
    ''')

    con.commit()
    con.close()