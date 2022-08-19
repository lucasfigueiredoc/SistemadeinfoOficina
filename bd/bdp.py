from calendar import c
import sqlite3

# Conexão
con = sqlite3.connect('data.db')

# Cursor pra executar os comandos
cur = con.cursor()

# CUIDADO: Apaga a tabela se necessário
##cur.execute(f"DROP TABLE users")

# Cria uma tabela com os valores
cur.execute(f"CREATE TABLE IF NOT EXISTS users (nome, cpf)")

# Insere os dados na tabela
cur.execute(f"INSERT INTO users VALUES ('usuario 1', 'cpf 1')")

con.commit()
con.close()