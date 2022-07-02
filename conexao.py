import mysql.connector
from mysql.connector import errorcode


def conectar():
    try:
        db_connection = mysql.connector.connect(host='localhost', user='root', password='', database='quiz')
        print('Conectado com sucesso!')
        return db_connection
    except mysql.connector.Error as erro:
        if erro.errno == errorcode.ER_BAD_DB_ERROR:
            print('Banco de dados não existe!, {}'.format(erro))
        elif erro.errnor == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Usuario ou senha não são validas!, {}', format(erro))
        else:
            print(erro)
    else:
        db_conncetion.close()
