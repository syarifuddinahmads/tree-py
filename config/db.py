from flask import Flask
from flaskext.mysql import MySQL
app = Flask(__name__)

# mysql
mysql = MySQL()
# config db
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'udin'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
app.config['MYSQL_DATABASE_DB'] = 'mahasiswa'
# init
mysql.init_app(app)