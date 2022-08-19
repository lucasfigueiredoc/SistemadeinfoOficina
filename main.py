#import bd.connectBd 
#from Objetos.cliente import Cliente
from os import system
from bd.connectBd import insertCliente, createTables, insertService
#from Objetos.cliente import Cliente



def ArtMenu():
    system("clear")
    print("----------------------------------")
    print("     1 : Registrar Serviço        ")
    print("     2 : Cadastrar Cliente        ")
    print("     3 : Agenda de Serviços       ")
    print("     4 : Criar tabelas SQL        ")
    print("     5 : Fechar Aplicação         ")
    print("----------------------------------")
    
    
def operacao(x):
    # Aqui, limpamos a tela antes de qualquer outra
    # operação
    system("clear")

    match x:
        case '1':
            insertService()
        case '2':
            insertCliente()
        case '3':
            return print("Case 3 selected")
        case '4':
            createTables()
        case '5':
            exit()
    
        
        case _:
            return print('Valor inválido, retorne!')
        
        
# def clienteAdd():
#     print('Cadastrando Cliente, adicione os dados respectivamente: \n')

#     # Adicionamos um item a nossa lista, neste caso, o objeto
#     # cliente, através do método "append"

    
    # Cliente(input('Nome: '), input('CPF: '), input('Endereço completo: '))

    # # Limpar a tela antes de concluir
    # system("clear")
    # print("Cliente cadastrado com sucesso!")
        
        
while True:
    ArtMenu()
    operacao(input('Define '))
    
    print("----------------------------------")
    input("Pressione ENTER para continuar...")