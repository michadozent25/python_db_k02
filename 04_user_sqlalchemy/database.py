from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL ="mysql+pymysql://root:@localhost:3306/db_python03"
engine = create_engine(DATABASE_URL,echo=True)
Session = sessionmaker(bind=engine) # Klassen-Factory
session = Session()# Objekt erzeugen

Base = declarative_base()# alle Models(Entity) erben von Base