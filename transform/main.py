import argparse #Parseador de argumentos
# Importamos la libreria logging para mostrar mensajes al usuario
import logging
# Importamos la libreria de pandas para analisis de datos
import pandas as pd
import datetime

# Le pasamos la configuracion basica al logging
logging.basicConfig(level=logging.INFO)

#Obtenemos una referencia al logger
logger = logging.getLogger(__name__)

# Definimos la Funcion principal
def main(file_name):
    logger.info('..:: Iniciando Proceso de limpieza de datos ::..')

    # Invocamos a la funcion para leer los datos.
    df = _read_data(file_name)
    # Eliminamos los espacios vacios de las columnas referentes al nombre
    df = _clear_player_name(df)
    # Concatenamos el nombre completo
    df= _concat_fullName(df)
    # Calculamos la edad
    df = _age_player(df)
    # Calculamos el promedio de los goles
    df = _goal_average(df)
    # Calculamos el promedio de las asistencias
    df = _assists_average(df)
    # Eliminamos las columnas innecesarias del dataframe
    df = _remove_columns(df, ['Nombre', 'ApePaterno','ApeMaterno'])
    # Agregamos los index
    df = _setindex(df)
    # Ordenamos las columnas del dataframe
    df = _sort_columns(df)
    # Invocamos a la función para guardar el df un archivo csv.
    _save_data_to_csv(df, file_name)

    return df

####################################################################
#           Función para leer los datos del Data Set               #
####################################################################
def _read_data(file_name):
    logger.info('Leyendo el archivo {}'.format(file_name))
    #Leemos el archvo csv y lo devolvemos el data frame
    return pd.read_csv(file_name, encoding='latin')

########################################################
#           Función para añadir un index               #
########################################################
def _setindex(df):
    logger.info('Añadiendo los index')

    i = 0
    index = []
    while i < df['NombreCompleto'].count():
        indice = i + 1
        index.append(indice)
        i += 1

    index
    df["Id"] = index
    return df.set_index("Id")


#########################################################################################
#  Función para eliminar los espacios en blanco de las columnas referentes al nombre    #
#########################################################################################
def _clear_player_name(df):
    logger.info('Extrayendo espacios en blanco')
    df['Nombre'] = df['Nombre'].apply( lambda nombre : nombre.strip() )
    df['ApePaterno'] = df['ApePaterno'].apply( lambda apaterno : apaterno.strip() )
    df['ApeMaterno'] = df['ApeMaterno'].apply( lambda amaterno : str(amaterno).strip() )
    
    return df

################################################################
#   Función para agregar la columna con el nombre completo     #
################################################################
def _concat_fullName(df):
    logger.info('Creando los nombre completos')
    listaNombres = []

    i = 0

    while i < df["Nombre"].count():
        
        nombre = df["Nombre"][i] + " " + df["ApePaterno"][i]
        
        if str(df["ApeMaterno"][i]) != 'nan':
            nombre += " " + df["ApeMaterno"][i]
        
        listaNombres.append(nombre)
        i += 1

    # Almacenando la lista de nombres completos en una columna del dataframe
    df['NombreCompleto'] = listaNombres
    return df

###################################################################
#           Función para obtener la edad del jugador              #
###################################################################
def _age_player(df):
    logger.info('Obteniendo las edades')

    fechaActual = datetime.datetime.now()
    anio = fechaActual.year

    df["Edad"] = df["Fecha Nacimiento"].apply( lambda fecha : int(anio) - int(fecha[:4]) )

    return df

#############################################
# Función para obtener el promedio de goles #
#############################################
def _goal_average(df):
    logger.info('Obteniendo el promedio de goles')
    
    j = 0
    listaPromediosGoles = []

    while j < df["NombreCompleto"].count():
        
        promedio = int(df["Goles"][j]) / int(df["Partidos"][j])
        
        listaPromediosGoles.append( round(promedio, 2) )
        
        j += 1

    listaPromediosGoles

    # Añadiendo la columna de promedio de goles
    df["PromedioGol"] = listaPromediosGoles

    return df



###################################################
# Función para obtener el promedio de asistencias #
###################################################
def _assists_average(df):
    logger.info('Obteniendo el promedio de asistencias')

    k = 0

    listaPromediosAsistencias = []

    while k < df["NombreCompleto"].count():
        
        promedio = int(df["Asistencias"][k]) / int(df["Partidos"][k])
        
        listaPromediosAsistencias.append( round(promedio, 2) )
        
        k += 1

    # Añadiendo la columna de promedio de goles
    df["PromedioAsistencia"] = listaPromediosAsistencias

    return df


######################################################
#   Función para remover las columnas innecesarias   #
######################################################
def _remove_columns(df, columnas):
    logger.info('Removiendo las columnas innecesarias')

    df.drop(columnas, axis = 1, inplace = True)

    return df


#####################################################
#  Función para Ordenar las columnas del dataframe  #
#####################################################
def _sort_columns(df):
    logger.info('Ordenando las columnas')
    df = df[['NombreCompleto','Fecha Nacimiento', "Edad",'Partidos','Goles','Asistencias','PromedioGol', "PromedioAsistencia", "Competicion","Temporada"]]
    return df


##################################################################################
#         Función que guarda los datos del DataFrame en un archivo csv           #
##################################################################################
def _save_data_to_csv(df, filename):
    clean_filename = 'clean_{}'.format(filename)
    logger.info('Guardando los datos limpios en el archivo: {}'.format(clean_filename))
    df.to_csv(clean_filename)

##################################################################################
#                          Inicio de la aplicación                               #
##################################################################################
if __name__ == '__main__':
    #Creamos un nuevo parser de argumentos
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name',help='La ruta al dataset sucio',type=str)
    #Parseamos los argumentos.
    args = parser.parse_args()
    df = main(args.file_name)
    #Mostramos el Data Frame
    print(df)