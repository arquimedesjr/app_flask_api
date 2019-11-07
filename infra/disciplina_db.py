import sqlite3

db_name = "disciplina.db"
table_name = "disciplinas"

sql_create_table = f'CREATE TABLE IF NOT EXISTS {table_name} (id integer PRIMARY KEY, nome text NOT NULL, ' \
                   f'status text NOT NULL,' \
                   f'plano_ensino text NOT NULL,' \
                   f'carga_horaria text NOT NULL,' \
                   f'id_professor integer);'


def createTable(cursor, sql):
    cursor.execute(sql)


def popularDb(cursor, id, nome, status, plano_ensino, carga_horaria, id_professor):
    sql = f"INSERT INTO {table_name} (id, nome, status, plano_ensino, carga_horaria, id_professor) VALUES (?, ?, ?, ?, ?, ?)"
    cursor.execute(sql, (id, nome, status, plano_ensino, carga_horaria, id_professor))


def init():
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    createTable(cursor, sql_create_table)
    cursor.close()
    connection.commit()
    connection.close()


init()
