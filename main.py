from src import pipelineETL as rodar_pipeline
from src import plots as gerar_graficos
from database import tabelas as db

def main():

    print("Processo ETL")
    db.create_table()
    rodar_pipeline.run()

    print('comparativo de PIBs')
    # Mostra comparativo do PIB da Argentina e Brasil 2023 e 2024
    gerar_graficos.comparativo_PIB()

    print('comparativo de desemprego')
    # Mostra comparativo desempreog da Argentina e Brasil 2023 e 2024
    gerar_graficos.comparativo_desemprego()

main()