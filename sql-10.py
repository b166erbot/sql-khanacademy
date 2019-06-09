import sqlite3
from os.path import exists


def bancoDeDados(*args: tuple):
    """
    Função que comita os comandos sql.
    """
    connection = sqlite3.connect('teste10.db')
    cursor = connection.cursor()
    cursor.execute(*args)
    retorno = cursor.fetchall()
    connection.commit()
    connection.close()
    return retorno


def main():
    existiaDb = exists('teste10.db')
    comandoSql = ('CREATE TABLE IF NOT EXISTS artists(id INTEGER PRIMARY'
                  ' KEY AUTOINCREMENT, name TEXT, country  TEXT, genre  TEXT)')
    comandoSql2 = ('CREATE TABLE IF NOT EXISTS songs(id INTEGER PRIMARY'
                   ' KEY AUTOINCREMENT, artist TEXT, title TEXT)')
    bancoDeDados(comandoSql)
    bancoDeDados(comandoSql2)
    if not existiaDb:
        # table artists
        bancoDeDados(('INSERT INTO artists (name, country, genre) VALUES'
                      ' ("Taylor Sqift", "US", "Pop")'))
        bancoDeDados(('INSERT INTO artists (name, country, genre) VALUES'
                      ' ("Led Zeppelin", "US", "Hard rock")'))
        bancoDeDados(('INSERT INTO artists (name, country, genre) VALUES'
                      ' ("ABBA", "Sqeden", "Disco")'))
        bancoDeDados(('INSERT INTO artists (name, country, genre) VALUES'
                      ' ("Queen", "UK", "Rock")'))
        bancoDeDados(('INSERT INTO artists (name, country, genre) VALUES'
                      ' ("Celine Doin", "Canada", "Pop")'))
        bancoDeDados(('INSERT INTO artists (name, country, genre) VALUES'
                      ' ("Meatloaf", "US", "Hard rock")'))
        bancoDeDados(('INSERT INTO artists (name, country, genre) VALUES'
                      ' ("Garth Brooks", "US", "Country")'))
        bancoDeDados(('INSERT INTO artists (name, country, genre) VALUES'
                      ' ("Shania Twain", "Canada", "Country")'))
        bancoDeDados(('INSERT INTO artists (name, country, genre) VALUES'
                      ' ("Rihanna", "US", "Pop")'))
        bancoDeDados(('INSERT INTO artists (name, country, genre) VALUES'
                      ' ("Guns N\' Roses", "US", "Hard rock")'))
        bancoDeDados(('INSERT INTO artists (name, country, genre) VALUES'
                      ' ("Gloria Estefan", "US", "Pop")'))
        bancoDeDados(('INSERT INTO artists (name, country, genre) VALUES'
                      ' ("Bob Marley", "Jamaica", "Reggae")'))
        # table songs
        bancoDeDados(('INSERT INTO songs (artist, title) VALUES'
                      ' ("Taylor Swift", "Shake it off")'))
        bancoDeDados(('INSERT INTO songs (artist, title) VALUES'
                      ' ("Rihanna", "Stay")'))
        bancoDeDados(('INSERT INTO songs (artist, title) VALUES'
                      ' ("Celine Dion", "My heart will go on")'))
        bancoDeDados(('INSERT INTO songs (artist, title) VALUES'
                      ' ("Celine Dion", "A new day has come")'))
        bancoDeDados(('INSERT INTO songs (artist, title) VALUES'
                      ' ("Shania Twain", "Party for two")'))
        bancoDeDados(('INSERT INTO songs (artist, title) VALUES'
                      ' ("Gloria Estefan", "Conga")'))
        bancoDeDados(('INSERT INTO songs (artist, title) VALUES'
                      ' ("Led Zeppelin", "Stairway to heaven")'))
        bancoDeDados(('INSERT INTO songs (artist, title) VALUES'
                      ' ("ABBA", "Mamma mia")'))
        bancoDeDados(('INSERT INTO songs (artist, title) VALUES'
                      ' ("Queen", "Bicycle Race")'))
        bancoDeDados(('INSERT INTO songs (artist, title) VALUES'
                      ' ("Queen", "Bohemian Rhapsody")'))
        bancoDeDados(('INSERT INTO songs (artist, title) VALUES'
                      ' ("Guns N\' Roses", "Don\'t cry")'))
    print(bancoDeDados('SELECT title FROM songs WHERE artist = "Queen"'))
    print(bancoDeDados('SELECT name FROM artists WHERE genre = "Pop"'))
    print(bancoDeDados(('SELECT title FROM songs WHERE artist IN '
                        '(SELECT name FROM artists WHERE genre = "Pop")')))


if __name__ == '__main__':
    main()
