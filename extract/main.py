import argparse #Parseador de argumentos
import logging #Para mostrar mensajes en consola
import csv
import datetime
from os import write

#Importamos los errores
from requests.exceptions import HTTPError
from urllib3.exceptions import MaxRetryError


#Le pasamos la configuración básica al logging
logging.basicConfig(level=logging.INFO)
#Obtenemos una referencia al logger
logger = logging.getLogger(__name__)
#pip install mysql-connector-python
#pip install mysql-connector
from mysql.connector import connect

cnx = connect(user='root', password='root', host='127.0.0.1', database='etl')

#Método para recuperar las url's de los sitios de noticias guardados en
#la configuración
def _players_scrapper():
    logging.info('..::Iniciando el scrapper para la obtención de los jugadores::..')
    cursor = cnx.cursor()
    sql = "SELECT * FROM v_jugador"
    cursor.execute(sql)
    jugadores = cursor.fetchall()
    cnx.close()
    _save_players(jugadores)
    print(f"Num. Jugadores {str(len(jugadores))}")

#Función para guardar los artículos en un archivo CSV
def _save_players(jugadores):
    now = datetime.datetime.now().strftime('%Y_%m_%d')
    out_file_name = 'jugadores_{}.csv'.format(now)
    csv_headers = ['Nombre', 'ApePaterno', 'ApeMaterno', 'Fecha Nacimiento',
                   'Partidos', 'Goles', 'Asistencias', 'Equipo', 'Competicion',
                   'Temporada']

    #Escribimos en el archivo
    with open(out_file_name, mode='w+', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(csv_headers)

        for jugador in jugadores:
            row = [jugador[0], jugador[1], jugador[2], jugador[3], jugador[4],
                   jugador[5], jugador[6], jugador[7], jugador[8], jugador[9]]
            writer.writerow(row)

if __name__ == '__main__':
    _players_scrapper()