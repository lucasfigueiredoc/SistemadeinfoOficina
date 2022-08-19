import sqlite3


def insertCliente():
    
    con = sqlite3.connect('./bd/oficinaBd.db')
    
    cur = con.cursor()

    nome = input('Entre com o nome ')
    cpf = input('Entre com o CPF ')
    
   
    
    cur.execute(f""" insert into client (namee,cpf) values ('{nome}','{cpf}') """)

    con.commit()
    
    
    cur.close()
    con.close()
    
    
def insertService():
    
    con = sqlite3.connect('oficinaBd.db')
    
    cur = con.cursor()

    nome = input('Entre com o nome ')
    cpf = input('Entre com o CPF ')
    
    print("Inserão de serviço")
    serviceOption = input("Qual tipo de serviço: Preventiva ou Corretiva : \n\n")
    description = input("Descreva o serviço feito: \n\n")
    id_client = input("Informe o numeral do cliente: \n\n")
    id_employee = input("Informe o seu código de funcionario: \n\n")    
    
    cur.execute(f""" insert into servicc (serviceOption, descricao, id_client, id_employee) values ('{serviceOption}','{description}','{id_client}','{id_employee}') """)

    con.commit()
    
    
    cur.close()
    con.close()



    # CUIDADO: Apaga a tabela se necessário
    # cur.execute(f"DROP TABLE cliente")

    # Cria uma tabela com os valores
    
def createTables():
    con = sqlite3.connect('./bd/oficinaBd.db')
    cur = con.cursor()
    cur.execute(""" CREATE TABLE IF NOT EXISTS client (namee varchar(50) not null, 
                                                        cpf varchar(11) not null, 
                                                        id_cliente INTEGER primary key AUTOINCREMENT )""")
    
    cur.execute(""" CREATE TABLE IF NOT EXISTS employee (namee varchar(50) not null, 
                                                        occupation varchar(11) not null, 
                                                        id_employee INTEGER primary key AUTOINCREMENT )""")
    
    cur.execute(""" CREATE TABLE IF NOT EXISTS servicc ( serviceOption varchar(50), 
                                                        descricao varchar(1000), 
                                                        id_servico INTEGER primary key AUTOINCREMENT, 
                                                        data_servc datetime not null, 
                                                        foreign key(id_servico) references employee(id_employee),
                                                        foreign key(id_servico) references client(id_client) )""")

    con.commit()
    print('Tabelas Criadas')
    
    cur.close()
    con.close()
