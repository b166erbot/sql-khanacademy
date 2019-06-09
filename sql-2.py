import sqlite3
from os.path import exists


def bancoDeDados(*args: tuple):
    """
    Função que comita os comandos sql.
    """
    connection = sqlite3.connect('teste2.db')
    cursor = connection.cursor()
    cursor.execute(*args)
    retorno = cursor.fetchall()
    connection.commit()
    connection.close()
    return retorno


def main():
    existiaDb = exists('teste2.db')
    comandoSql = ('CREATE TABLE IF NOT EXISTS groceries (id INTEGER PRIMARY'
                  ' KEY, name TEXT,quantity INTEGER, aisle INTEGER)')
    bancoDeDados(comandoSql)
    if not existiaDb:
        bancoDeDados('INSERT INTO groceries VALUES (1, "Bananas", 4, 7)')
        bancoDeDados('INSERT INTO groceries VALUES(2, "Peanut Butter", 1, 2)')
        bancoDeDados(
            'INSERT INTO groceries VALUES(3, "Dark Chocolate Bars", 2, 2)')
        bancoDeDados('INSERT INTO groceries VALUES(4, "Ice cream", 1, 12)')
        bancoDeDados('INSERT INTO groceries VALUES(5, "Cherries", 6, 2)')
        bancoDeDados(
            'INSERT INTO groceries VALUES(6, "Chocolate syrup", 1, 4)')
    print(bancoDeDados(
        'SELECT * FROM groceries WHERE aisle > 5 ORDER BY aisle'))


if __name__ == '__main__':
    main()
