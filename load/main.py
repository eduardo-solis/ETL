import argparse
import logging
import pandas as pd

from model import Jugador
from base import Base, engine, Session

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Metodo para iniciar la aplicacion
def main(filename):

    # Generamos el esquema de la BD
    Base.metadata.create_all(engine)

    # Iniciamos la sesión
    session = Session()

    # Leemos el archivo csv
    jugadores = pd.read_csv(filename, encoding='utf-8')

    # Iteramos entre la filas del csv mediante el metodo iterrows() y vamos pasando los articulos a la BD
    for index, row in jugadores.iterrows():
        logger.info('Cargando el jugador con id: {} en la BD'.format(row['Id']))

        jugador = Jugador(
                            row['Id'],
                            row['NombreCompleto'],
                            row['Fecha Nacimiento'],
                            row['Edad'],
                            row['Partidos'],
                            row['Goles'],
                            row['Asistencias'],
                            row['PromedioGol'],
                            row['PromedioAsistencia'],
                            row['Competicion'],
                            row['Temporada'],
                        )
        
        session.add(jugador)

        session.commit()
        session.close()


if __name__ == '__main__':
    #Creamos un nuevo parser de argumentos
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name',
                        help='La ruta al data set limpio para cargar a la base de datos',
                        type=str)
    #Parseamos los argumentos.
    args = parser.parse_args()
    main(args.file_name)
    