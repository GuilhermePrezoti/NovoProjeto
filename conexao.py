import mysql.connector
from mysql.connector import errorcode

def conectar():
    try:
        db_connection = mysql.connector.connect(host='localhost', user='root', password='', database='hospital')
        print('Conectado com sucesso!')
        return db_connection
    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_BAD_DB_ERROR:
            print('Banco de dados não existe!, {}'.format(error))
        elif error.errnor == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Usuario ou senha não são validas!, {}', format(error))
        else:
            print(error)
    else:
        db_conncetion.close()