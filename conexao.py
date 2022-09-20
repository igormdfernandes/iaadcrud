import mysql.connector
from mysql.connector import errorcode

try:
    con = mysql.connector.connect(host="localhost", user="root", password="iaadcrUD1", db="iaadcrud")
    print("Banco conectado com sucesso")
    cursor = con.cursor()
except mysql.connector.Error as error:
    if error.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database não encontrada")
    elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Usuario ou senha incorretos")
    else:
        print(error)
else:
    con.close()
