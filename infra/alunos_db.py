import sqlite3

db_name = "alunos.db"
table_name = "aluno"

sql_create_table = f"CREATE TABLE IF NOT EXISTS {table_name} (id integer PRIMARY KEY, nome text NOT NULL);"

def createTable(cursor, sql):
    cursor.execute(sql)

def popularDb(cursor, id, nome):
    sql = f"INSERT INTO {table_name} (id, nome) VALUES (?, ?)"
    cursor.execute(sql, (id, nome))

def init():
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    createTable(cursor, sql_create_table)

    cursor.close()
    connection.commit()
    connection.close()
    
init()