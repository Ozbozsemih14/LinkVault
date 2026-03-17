from sqlalchemy import create_url,create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm  import sessionmaker

#Database file location
SQLALCHEMY_DATABASE_URL ="sqlite:///./linkvault.db"

#Engine starting
engine =create_engine(
    SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread:"False}
)

#Session to talk database
SessionLocal =sessionmaker(autocommit=False,autoflush=False,bind=engine)

#Main class from which model will be derived
Base=declarative_base()
