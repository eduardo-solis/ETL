import datetime
#Permite invocar comandos del sistema operativo
import subprocess
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#Función principal que ejecuta el ETL paso a paso
def main():
    _extract()
    _transform()
    _load()
    logger.info('..::Proceso ETL finalizado::..')

#Función encargada de invocar el proceso de extracción
def _extract():
    logger.info('..::Iniciando el proceso de extracción::..')
    subprocess.run(['python', 'main.py'], cwd='./extract')
    subprocess.run(['move', r'extract\*.csv', r'transform'], shell=True)

#Función encargada de invocar el proceso de transformación
def _transform():
    logger.info('..::Iniciando el proceso de transformación::..')
    now = datetime.datetime.now().strftime('%Y_%m_%d')

#Función encargada de invocar el proceso de carga
def _load():
    logger.info('..::Iniciando el proceso de carga::..')
    now = datetime.datetime.now().strftime('%Y_%m_%d')


if __name__ == '__main__':
    main()