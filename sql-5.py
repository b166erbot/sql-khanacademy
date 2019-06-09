import sqlite3
from os.path import exists


def bancoDeDados(*args: tuple):
    """
    Função que comita os comandos sql.
    """
    connection = sqlite3.connect('teste5.db')
    cursor = connection.cursor()
    cursor.execute(*args)
    retorno = cursor.fetchall()
    connection.commit()
    connection.close()
    return retorno


def main():
    existiaDb = exists('teste5.db')
    comandoSql = ('CREATE TABLE IF NOT EXISTS todo_list (id INTEGER PRIMARY'
                  ' KEY, item TEXT, minutes INTEGER)')
    bancoDeDados(comandoSql)
    if not existiaDb:
        bancoDeDados('INSERT INTO todo_list VALUES (1, "Wash the dishes", 15)')
        bancoDeDados('INSERT INTO todo_list VALUES(2, "vacuuming", 20)')
        bancoDeDados(
            'INSERT INTO todo_list VALUES(3, "Learn some stuff on KA", 30)')
        bancoDeDados('INSERT INTO todo_list VALUES(4, "time to i die", 30)')
    print(bancoDeDados('SELECT SUM(minutes) FROM todo_list'))


if __name__ == '__main__':
    main()
