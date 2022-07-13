from enum import unique
from sqlalchemy import Column, String, Integer, Float
from base import Base

# Declaramos la clase article que define la tabla de la BD
class Jugador(Base):
    __tablename__ = 'jugadores'
    # Definicion de columnas
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    fechaNac = Column(String)
    edad = Column(Integer)
    partidos = Column(Integer)
    goles = Column(Integer)
    asistencias = Column(Integer)
    promedio_gol = Column(Float)
    promedio_asistencia = Column(Float)
    competicion = Column(String)
    temporada = Column(String)

    def __init__(self, id, nombre, fechaNac, edad, partidos, goles, asistencias, promedio_gol, promedio_asistencia, competicion, temporada):
        self.id = id
        self.nombre = nombre
        self.fechaNac = fechaNac
        self.edad = edad
        self.partidos = partidos
        self.goles = goles
        self.asistencias = asistencias
        self.promedio_gol = promedio_gol
        self.promedio_asistencia = promedio_asistencia
        self.competicion = competicion
        self.temporada = temporada