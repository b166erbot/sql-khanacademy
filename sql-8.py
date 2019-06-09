import sqlite3
from os.path import exists


def bancoDeDados(*args: tuple):
    """
    Função que comita os comandos sql.
    """
    connection = sqlite3.connect('teste8.db')
    cursor = connection.cursor()
    cursor.execute(*args)
    retorno = cursor.fetchall()
    connection.commit()
    connection.close()
    return retorno


def main():
    existiaDb = exists('teste8.db')
    comandoSql = ('CREATE TABLE IF NOT EXISTS songs (id INTEGER'
                  ' PRIMARY KEY, title TEXT, artist TEXT, mood INTEGER,'
                  ' duration INTEGER, released INTEGER)')
    bancoDeDados(comandoSql)
    if not existiaDb:
        bancoDeDados(('INSERT INTO songs (title, artist, mood, duration,'
                      ' released) VALUES ("Bohemian Rhapsody", "Queen",'
                      ' "epic", 60, 1975)'))
        bancoDeDados(('INSERT INTO songs (title, artist, mood, duration,'
                      ' released) VALUES ("Let it go", "Idina Menzel",'
                      ' "epic", 227, 2013)'))
        bancoDeDados(('INSERT INTO songs (title, artist, mood, duration,'
                      ' released) VALUES ("I will survive", "Gloria'
                      ' Gaynor", "epic", 198, 1978)'))
        bancoDeDados(('INSERT INTO songs (title, artist, mood, duration,'
                      ' released) VALUES ("Twist and Shout", "The Beatles",'
                      ' "happy", 152, 1963)'))
        bancoDeDados(('INSERT INTO songs (title, artist, mood, duration,'
                      ' released) VALUES ("La Bamba", "Ritchie Valens", '
                      '"happy", 166, 1958)'))
        bancoDeDados(('INSERT INTO songs (title, artist, mood, duration,'
                      ' released) VALUES ("I will always love you",'
                      ' "Whitney Houston", "epic", 273, 1992)'))
        bancoDeDados(('INSERT INTO songs (title, artist, mood, duration,'
                      ' released) VALUES ("Sweet Caroline", "Neil Diamond",'
                      ' "happy", 201, 1969)'))
        bancoDeDados(('INSERT INTO songs (title, artist, mood, duration,'
                      ' released) VALUES ("Call me maybe", "Carly Rae'
                      ' Jepsen", "happy", 193, 2011)'))
    print(bancoDeDados('SELECT title FROM songs'))
    print(bancoDeDados(('SELECT title FROM songs WHERE mood == "epic"'
                        ' or released > 1990')))
    print(bancoDeDados(('SELECT title FROM songs WHERE mood == "epic"'
                       ' and released > 1990 and duration < 240')))


if __name__ == '__main__':
    main()
