import sqlite3

from Objetos.cliente import Cliente
from Objetos.servico import Servico
class Conn():
    def __init__(self):
        self.__con = sqlite3.connect('./bd/oficinaBd.db')
        self.__cur = self.__con.cursor()

    def close(self):
        self.__cur.close()
        self.__con.close()

    def insertCliente(self):
        nome = input('Entre com o nome ')
        cpf = input('Entre com o CPF ')
        endereco = input('Entre com o endereço ')
        
        self.__cur.execute(f""" insert into client (namee, cpf, endereco) values ('{nome}','{cpf}', '{endereco}') """)

        self.__con.commit()

    def listarClientes(self):
        query = 'SELECT * FROM client'
        
        resultado = self.__cur.execute(query).fetchall()

        clientes = list()

        for linha in resultado:
            cli = Cliente(linha[0], linha[1], linha[2], linha[3])
            
            print("----------------------------------")
            print(f"Nome: {cli.nome}")
            print(f"CPF: {cli.cpf}")
            print(f"Endereço: {cli.endereco}")
            print(f"ID (auto): {cli.id}")

        return clientes 
    
    def listarServicos(self):
        query='SELECT * FROM servicc'
        
        resultado = self.__cur.execute(query).fetchall()
        
        servico = list()

        for linha in resultado:
            srv = Servico(linha[0], linha[1], linha[2], linha[3])
            
            print("----------------------------------")
            print(f"Tipo: {srv.serviceOption}")
            print(f"Descrição: {srv.descricao}")
            print(f"Id do cliente: {srv.id_client}")
            print(f"Id do Funcionário: {srv.id_employee}")

            
        return servico
 
    def insertService(self):
        print("Insert de serviço")

        serviceOption = input("Qual tipo de serviço: Preventiva ou Corretiva : \n\n")
        descricao = input("Descreva o serviço feito: \n\n")
        id_client = input("Informe o numeral do cliente: \n\n")
        id_employee = input("Informe o seu código de funcionario: \n\n")    
        
        self.__cur.execute(f""" insert into servicc (serviceOption, descricao, id_client, id_employee) values ('{serviceOption}','{descricao}','{id_client}','{id_employee}') """)

        self.__con.commit()
        
    def createTables(self):
        self.__cur.execute(""" CREATE TABLE IF NOT EXISTS client (namee varchar(50) not null, 
                                                            cpf varchar(11) not null,
                                                            endereco varchar(100) ,
                                                            id_cliente INTEGER primary key AUTOINCREMENT )""")
        
        self.__cur.execute(""" CREATE TABLE IF NOT EXISTS employee (namee varchar(50) not null, 
                                                            occupation varchar(11) not null, 
                                                            id_employee INTEGER primary key AUTOINCREMENT )""")
        
        self.__cur.execute(""" CREATE TABLE IF NOT EXISTS servicc ( serviceOption varchar(50), 
                                                            descricao varchar(1000), 
                                                            id_servico INTEGER primary key AUTOINCREMENT, 
                                                            data_servc datetime ,
                                                            id_client integer,
                                                            id_employee integer, 
                                                            foreign key(id_servico) references employee(id_employee),
                                                            foreign key(id_servico) references client(id_client) )""")
        self.__cur.execute(""" insert into employee (namee, occupation) values ("Rogério", "Mecânico") """)
        self.__cur.execute(""" insert into employee (namee, occupation) values ("Marcos", "Mecânico") """)
        self.__cur.execute(""" insert into employee (namee, occupation) values ("Leandro", "Mecânico") """)
        self.__cur.execute(""" insert into employee (namee, occupation) values ("Vinicius", "Mecânico") """)
        self.__cur.execute(""" insert into client (namee,cpf) values ("Lucas","123394859") """)
        self.__cur.execute(""" insert into client (namee,cpf) values ("Cindy","123424859") """)
        self.__cur.execute(""" insert into client (namee,cpf) values ("Pedro","123123259") """)
        self.__cur.execute(""" insert into client (namee,cpf) values ("Seixas","12134859") """)


        self.__con.commit()