from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# URL de la base de datos (ajústala según tu configuración en rxconfig.py)
DATABASE_URL = "postgresql://postgres:1336C@localhost:5432/reflex_db"

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL)

# Crear una fábrica de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

from .models import Base

Base.metadata.create_all(bind=engine)