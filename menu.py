import operacoes
import this
this.opcao = -1
this.codigo = 0
this.perguntas = ""
this.respostas = ""


def menu():
    print('\nEscolha uma das opções abaixo: \n\n'+
          '1. Cadastrar Pergunta\n'+
          '2. Consultar Questão\n'+
          '3. Atualizar Pergunta\n'+
          '4. Atualizar Resposta\n'+
          '5. Deletar\n'+
          '0. Sair\n')
    this.opcao = int(input())

def operacao():
    while(this.opcao != 0):
        menu()
        if this.opcao == 1:
            print('Informe a pergunta que você quer adicionar: ')
            perguntas = input()
            print('Informe a resposta que você qeur adicionar: ')
            respostas = input()
            operacoes.inserir(perguntas,respostas)
        elif this.opcao == 2:
            operacoes.consultar()
        elif this.opcao == 3:
            print("Informe o código que deseja atualizar: ")
            this.codigo = int(input())
            print("Informe a nova Pergunta: ")
            this.perguntas = input()
            operacoes.atualizar(this.codigo, 'perguntas', this.perguntas)
        elif this.opcao == 4:
            print("Informe o código que deseja atualizar: ")
            this.codigo = int(input())
            print("Informe a nova Resposta: ")
            this.respostas = input()
            operacoes.atualizar(this.codigo, 'respostas', this.respostas)
        elif this.opcao == 5:
            print("Informe o codigo que deseja excluir: ")
            this.codigo = int(input())
            operacoes.excluir(this.codigo)
        else:
            print('Opcão escolhida não é válida!')
