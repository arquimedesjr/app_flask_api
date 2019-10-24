import sqlite3

db_name = "disciplina.db"
table_name = "disciplinas"

sql_create_table = f'CREATE TABLE IF NOT EXISTS {table_name} (id integer PRIMARY KEY, nome text NOT NULL, ' \
                   f'status text NOT NULL,' \
                   f'plano_ensino text NOT NULL,' \
                   f'carga_horaria text NOT NULL);'


def createTable(cursor, sql):
    cursor.execute(sql)


def popularDb(cursor, id, nome, status, plano_ensino, carga_horaria):
    sql = f"INSERT INTO {table_name} (id, nome, status, plano_ensino, carga_horaria) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(sql, (id, nome, status, plano_ensino, carga_horaria))


def init():
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    createTable(cursor, sql_create_table)
    try:
        popularDb(cursor, 1, "Engenharia de Requisito", "Ativo", "1-aula", "80")
        popularDb(cursor, 2, "Gestão de Projetos", "DESATIVADO", "11-aula", "160")
        popularDb(cursor, 3, "Desenvolvimento de Aplicações Distribuídas", "DESATIVADO", "11-aula", "160")
        popularDb(cursor, 4, "Interface Homem Computador", "Ativo", "1-aula", "80")
    except:
        print("erro")
    cursor.close()
    connection.commit()
    connection.close()


init()
