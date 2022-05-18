from flask import Flask
from flask_mysqldb import MySQL
from src.main.network.controllers.admin_controller import app_file1
from src.main.network.controllers.item_controller import app_file2
from src.main.network.controllers.operation_controller import app_file3
from src.main.network.controllers.user_controller import app_file4

app = Flask(__name__)

# MYSQL config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'network_project'

mysql = MySQL(app)

app.register_blueprint(app_file1)
app.register_blueprint(app_file2)
app.register_blueprint(app_file3)
app.register_blueprint(app_file4)




if __name__ == '__main__':
    app.run(port=5500)
