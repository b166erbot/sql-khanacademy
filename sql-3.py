import sqlite3
from os.path import exists


def bancoDeDados(*args: tuple):
    """
    Função que comita os comandos sql.
    """
    connection = sqlite3.connect('teste3.db')
    cursor = connection.cursor()
    cursor.execute(*args)
    retorno = cursor.fetchall()
    connection.commit()
    connection.close()
    return retorno


def main():
    existiaDb = exists('teste3.db')
    comandoSql = ('CREATE TABLE movies (id INTEGER PRIMARY KEY, name TEXT,'
                  ' release_year INTEGER)')
    bancoDeDados(comandoSql)
    if not existiaDb:
        bancoDeDados('INSERT INTO movies VALUES(1, "Avatar", 2009)')
        bancoDeDados('INSERT INTO movies VALUES(2, "Titanic", 1997)')
        bancoDeDados(('INSERT INTO movies VALUES(3, "Star Wars: Episode IV'
                      ' - A New Hope", 1997)'))
        bancoDeDados('INSERT INTO movies VALUES(4, "Shrek 2", 2004)')
        bancoDeDados('INSERT INTO movies VALUES(5, "The Lion King", 1994)')
        bancoDeDados('INSERT INTO movies VALUES(6, "Disney\'s Up", 2009)')
    print(bancoDeDados('SELECT * FROM movies'))
    print(bancoDeDados(
        'SELECT * FROM movies WHERE release_year > 2000 ORDER BY release_year'
    ))


if __name__ == '__main__':
    main()
