#DB Connection
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
import os

def createDatabase(connectionString):
	otherEngine = create_engine(connectionString)
	create_database(otherEngine.url)

	meta = MetaData()

	user = Table(
		'user_table', meta, 
		Column('user_id', Integer, primary_key = True), 
		Column('username', String(50)), 
		Column('password_hash', String(72)), 
	)

	# generate database schema
	meta.create_all(engine)

server_type = os.getenv('db_server_type')
username = os.getenv('db_username')
password = os.getenv('db_password')
host = os.getenv('db_host')
port = os.getenv('db_port')
dbname = os.getenv('db_name')
connectionString = server_type+"://"+username+":"+password+"@"+host+":"+port+"/"+dbname

engine = create_engine(connectionString)
if not database_exists(engine.url):
	createDatabase(connectionString)

Session = sessionmaker(bind=engine)
Base = declarative_base()