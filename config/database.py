import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

sqlite_file_name = "../database.sqlite"
base_dir = os.path.dirname(os.path.realpath(__file__)) # write the directory 

database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}" # URL of database

engine = create_engine(database_url, echo=True) # Database engine, echo = show in console

session = sessionmaker(bind=engine) # Session to connect to the database

base = declarative_base() # Modify the table of database