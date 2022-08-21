from os import system
from bd.connect import Conn

conn = Conn()
conn.createTables()

def ArtMenu():
    system("clear")
    print("----------------------------------")
    print("     1 : Registrar Serviço        ")
    print("     2 : Cadastrar Cliente        ")
    print("     3 : Listar Clientes          ")
    print("     4 : Agenda de Serviços       ")
    print("     5 : Fechar Aplicação         ")
    print("----------------------------------")
    
    
def operacao(x):
    # Aqui, limpamos a tela antes de qualquer outra
    # operação
    system("clear")

    match x:
        case '1':
            conn.insertService()
        case '2':
            conn.insertCliente()
        case '3':
            conn.listarClientes()
        case '4':
            conn.createTables()
        case '5':
            conn.close()
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