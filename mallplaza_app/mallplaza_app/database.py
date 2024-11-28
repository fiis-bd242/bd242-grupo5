from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# URL de la base de datos (ajústala según tu configuración en rxconfig.py)
DATABASE_URL = "postgresql://postgres:1336C@localhost:5432/mallplaza_db"

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL)

# Crear una fábrica de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Reflex gestiona sus propias tablas. No necesitas esta parte si usas `rx.Model`:
# from .models import Base
# Base.metadata.create_all(bind=engine)
