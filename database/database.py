from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "sqlite:///./voluntarios.db"

# Configuración de SQLAlchemy para SQLite
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()


# La función create_database() llama a Base.metadata.create_all(bind=engine), 
# lo que crea todas las tablas definidas en tus modelos en la base de datos, si aún no existen.
def create_database():
    Base.metadata.create_all(bind=engine)
