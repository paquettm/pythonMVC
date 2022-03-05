# pythonMVC

## Installation

1. Pull the repository
2. Enter the `pipenv shell`
3. Run `pipenv install`
4. Set the following environment variables in .env or in the system:
- db_server_type: your database server type, e.g., mysql+pymysql
- db_username: your database connection username
- db_password: your database connection password
- db_host: your database server host uri, e.g., localhost
- db_port: your database server port, e.g., 3306
- db_name: your database name
e.g. run the commands
```bash
export db_server_type=mysql+pymysql
export db_username=root
export db_password=pass
export db_host=localhost
export db_port=3306
export db_name=myDatabase
```
or write the .env file containing
```
db_server_type=mysql+pymysql
db_username=root
db_password=pass
db_host=localhost
db_port=3306
db_name=myDatabase
```