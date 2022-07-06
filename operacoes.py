import mysql.connector
import conexao

db_connection = conexao.conectar()
con = db_connection.cursor()

def inserir(perguntas, respostas):
    try:
        sql = "insert into jogo(codigo, perguntas, respostas) values('', '{}', '{}')".format(perguntas,respostas)
        con.execute(sql)
        db_connection.commit()
        print("{} Inserido".format(con.rowcount))

    except Exception as erro:
        return erro

def consultar():
    try:
         sql = 'select * from jogo'
         con.execute(sql)

         for(codigo, perguntas, respostas) in con:
             print('codigo: {}, perguntas: {}, respostas: {}'.format(codigo, perguntas, respostas))
         print('\n')
    except Exception as erro:
        print(erro)

def atualizar(cod, novasPerguntas, novasRespostas):
    try:
        sql = "update jogo set {} = '{}' where codigo = '{}'".format(novasPerguntas, novasRespostas, cod)
        con.execute(sql)
        db_connection.commit()
        print('{} Atualizado!'.format(con.rowcount))
    except Exception as erro:
        print(erro)

def excluir(cod):
    try:
        sql = "delete from jogo where codigo = '{}'".format(cod)
        con.execute(sql)
        db_connection.commit()
        print('{} Excluido!'.format(con.rowcount))
    except Exception as erro:
        print(erro)