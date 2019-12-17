import os

# 设置secret key
SECRET_KEY = os.urandom(24)

# 数据库配置
# mysql+pymysql://username:password@localhost:port/mydatabase
SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://transport:transport@39.107.83.159:3306/" \
                          "transport"
SQLALCHEMY_TRACK_MODIFICATIONS = False
# gioa