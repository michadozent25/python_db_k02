from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from typing import Generator


#DATABASE_URL = "postgresql+psycopg://username:passwort@localhost:5432/datenbankname"
DATABASE_URL =  "sqlite:///todo.db"
#DATABASE_URL ="mysql+pymysql://root:@localhost:3306/db_python05"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autoflush=False,autocommit=False, bind=engine)

Base = declarative_base()

def get_db() -> Generator[Session,None,None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
