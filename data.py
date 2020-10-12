import sqlite3 as sql
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sql.connect(db_file)
        print(sql.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    return conn

if __name__ == '__main__':
    create_connection('python_sqlite.db')

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
