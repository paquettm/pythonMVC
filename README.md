# pythonMVC

## Installation

1. Create your MySQL database, table, and user, for example:
```
CREATE DATABASE myapplication;
CREATE TABLE user (
    user_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(72) NOT NULL
)ENGINE=INNODB;
CREATE USER 'myapplication_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'myapplication_password';
```
Note that for this application, the table structure is mandatory.

2. Pull the repository
3. Enter the `pipenv shell`
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
export db_username=myapplication_user
export db_password=myapplication_password
export db_host=localhost
export db_port=3306
export db_name=myapplication
```
or write the .env file containing
```
db_server_type=mysql+pymysql
db_username=myapplication_user
db_password=myapplication_password
db_host=localhost
db_port=3306
db_name=myapplication
```
