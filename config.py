HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'InforSphere'
USERNAME = 'root'
PASSWORD = 'longjiayu991216'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI


#pmqyeacqyjwxbebh

MAIL_SERVER = "smtp.qq.com"
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = "605889046@qq.com"
MAIL_PASSWORD = "pmqyeacqyjwxbebh"
MAIL_DEFAULT_SENDER = "605889046@qq.com"