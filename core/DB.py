#DB Connection
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

serverType = "mysql+pymysql"
host = "127.0.0.1"
user = "root"
password = "password"
database = "myPythonApp"
port = "3306"

engine = create_engine(serverType+"://"+user+":"+password+"@"+host+":"+port+"/"+database)
Session = sessionmaker(bind=engine)
Base = declarative_base()