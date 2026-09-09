import os

import mysql.connector
from dotenv import load_dotenv

load_dotenv()

conexao = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
)


cursor = conexao.cursor()



#cursor.close()
#conexao.close()