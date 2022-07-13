from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Declaramos el motor de la BD a usar
engine = create_engine('sqlite:///jugadores.db')

# Creamos una nueva sesion
Session = sessionmaker(bind=engine)

# Creamos el objeto de la Base de datos
Base = declarative_base()