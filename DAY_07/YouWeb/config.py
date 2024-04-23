# 모듈 로딩
import os

# 다양한 DBMS URI - SQLITE
BASE_DIR = os.path.dirname(__file__)
DB_NAME_SQLITE = 'app.db'

## 다양한 DBMS URI
DB_SQLITE_URI = f'sqlite:///{os.path.join(BASE_DIR, DB_NAME_SQLITE)}'

DB_MYSQL_URI = 'mysql+pymysql://root:root@localhost:3306/testdb'

# DB_MARAI_URI = 'maria+maria://root:root@localhost:3306/testdb'
# DB_POST_URI = 'postgresql+pg8000://root:root@localhost:3306/testdb'


## 사용할 DBMS 설정
SQLALCHEMY_DATABASE_URI = DB_MYSQL_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False

# DB_USER_ID = 'root'
# DB_USER_PW = 'root'
# DB_HOST_IP = '127.0.0.1'
# DB_NAME = 'testdb'
# DB_CHARSET = 'utf-8'