# Standard Configuration
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
DATABASE_URL=DATABASE_URL =  "sqlite:///courses.db"

engine =  create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine) 
session = Session() # kapselt Datenbankzugriff -> kein direkter Zugriff auf Datenbank
Base = declarative_base()  # alle Model-Klassen erben von Base (Objekte für die Datenbank)
