import mysql.connector
from mysql.connector import errorcode


def Jogo():

    print('Bem vindo ao jogo :)!')

    jogar = input('Você quer jogar? (Yes/No)')
    if jogar != 'yes':
        quit(print('Obrigado! Volte Sempre!'))
        print('Ok Vamos jogar!')



    jogo2 = input(print('Vamos jogar um QUIZ! Aperta ENTER para começar'))
    jogo2 = input(print('O Jogo começou!'))


    pergunta1 = input(print('1) Qual o presidente atual do Brasil?\n\n'
                            'Escolha a Opção correta\n\n'
                            'A)Jair Messias Bolsonaro\n'
                            'B)Lula\n'
                            'C)Neymar Junior\n'
                            'D)Bob Esponja\n'))
    if pergunta1.upper() == "A":
        print('Correto! Próxima Pergunta :)')
    else:
        print('Você não mora no Brasil! Tente Novamente!')


    pergunta2 = input(print('2) Qual é o coletivo de cães?\n\n'
                            'A)Cachorros\n'
                            'B)Gatos\n'
                            'C)Matilha\n'
                            'D)Alcateia\n'))
    if pergunta2.upper() == "C":
        print('Correto! Próxima Pergunta :)')
    else:
        print('Incorreta! Próxima Pergunta!')


    pergunta3 = input(print('3) Qual é o melhor professor do Senac?\n\n'
                            'A)Allan\n'
                            'B)Ualace\n'
                            'C)Daniel\n'
                            'D)Akira\n'
                            'E)...'))
    if pergunta3.upper() == "A" or "B" or "C" or "D":
        print('Correto! Próxima Pergunta :)')
    elif pergunta3.upper() == "E":
        print('Eles são os melhores professores do Senac!')


    pergunta4 = input(print('4)Qual melhor time do Brasil?\n\n'
                            'A)Palmeiras\n'
                            'B)Corinthias\n'
                            'C)Flamengo\n'
                            'D)Vasco\n'))

    if pergunta4.upper() == "C":
        print('Correto! Próxima Pergunta :)')
    elif pergunta4.upper() == "A":
        print('Palmeiras Não tem Mundial, Palmeiras não tem mundial,\n'
              'é Bi-Rebaixado e não tem mundial\n'
              'é Bi-Rebaixado e não tem mundial\n')
    else:
        print('Você não entende de Futebol! Próxima Pergunta!')


    pergunta5 = input(print('5)Qual a capital da Russia?\n\n'
                            'A)Moscol\n'
                            'B)Washington\n'
                            'C)Brasil\n'
                            'D)Lisboa\n'))
    if pergunta5.upper() == "A":
        print('Correto! Próxima Pergunta :)')
    else:
        print('Incorreto! Próxima Pergunta!')

    print('Obrigado por jogar o nosso jogo, Volte Sempre.')