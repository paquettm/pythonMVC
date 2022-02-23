#DBConnection

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://usr:pass@localhost:5432/sqlalchemy')
Session = sessionmaker(bind=engine)

Base = declarative_base()
#import mysql.python


import mysql.connector

class MySQL:
    message = ""
    connection = None
    
    @staticmethod
    def connect():
        serverType = "mysql"
        host = "localhost"
        user = "root"
        password = ""
        database = "myPythonApp"
        port = 3306
        try:
            if MySQL.connection == None:
                MySQL.connection = create_engine(serverType+"://"+user+":"+password+"@"+host+":"+port+"/"+database)

            return MySQL.connection
        except Exception as e:
            MySQL.message = e
    
    @staticmethod
    def close():
        MySQL.connection.Close()
