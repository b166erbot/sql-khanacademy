import sqlite3
from os.path import exists


def bancoDeDados(*args: tuple):
    """
    Função que comita os comandos sql.
    """
    connection = sqlite3.connect('teste12.db')
    cursor = connection.cursor()
    cursor.execute(*args)
    retorno = cursor.fetchall()
    connection.commit()
    connection.close()
    return retorno


def main():
    existiaDb = exists('teste12.db')
    comandoSql = ('CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY'
                  ' KEY AUTOINCREMENT, author TEXT, title TEXT, words'
                  ' INTEGER)')
    bancoDeDados(comandoSql)
    if not existiaDb:
        bancoDeDados(('INSERT INTO books (author, title, words) VALUES'
                      ' ("J.K. Rowling", "Harry Potter and the Philosopher\'s'
                      ' Stone", 79944)'))
        bancoDeDados(('INSERT INTO books (author, title, words) VALUES'
                      ' ("J.K. Rowling", "Harry Potter and the Chamber of'
                      ' Secrets", 85141)'))
        bancoDeDados(('INSERT INTO books (author, title, words) VALUES'
                      ' ("J.K. Rowling", "Harry Potter and the Prisoner of'
                      ' Azkaban", 107253)'))
        bancoDeDados(('INSERT INTO books (author, title, words) VALUES'
                      ' ("J.K. Rowling", "Harry Potter and the Goblet of'
                      ' Fire", 190637)'))
        bancoDeDados(('INSERT INTO books (author, title, words) VALUES'
                      ' ("J.K. Rowling", "Harry Potter and the Order of the'
                      ' Phoenix", 257045)'))
        bancoDeDados(('INSERT INTO books (author, title, words) VALUES'
                      ' ("J.K. Rowling", "Harry Potter and the Half-Blood'
                      ' Prince", 168923)'))
        bancoDeDados(('INSERT INTO books (author, title, words) VALUES'
                      ' ("J.K. Rowling", "Harry Potter and the Deathly'
                      ' Hallows", 197651)'))
        bancoDeDados(('INSERT INTO books (author, title, words) VALUES'
                      ' ("Stephenie Meyer", "Twilight", 118501)'))
        bancoDeDados(('INSERT INTO books (author, title, words) VALUES'
                      ' ("Stephenie Meyer", "New Moon", 132807)'))
        bancoDeDados(('INSERT INTO books (author, title, words) VALUES'
                      ' ("Stephenie Meyer", "Eclipse", 147930)'))
        bancoDeDados(('INSERT INTO books (author, title, words) VALUES'
                      ' ("Stephenie Meyer", "Breaking Dawn", 192196)'))
        bancoDeDados(('INSERT INTO books (author, title, words) VALUES'
                      ' ("J.R.R. Tolkien", "The Hobbit", 95022)'))
        bancoDeDados(('INSERT INTO books (author, title, words) VALUES'
                      ' ("J.R.R. Tolkien", "Fellowship of the Ring", 177227)'))
        bancoDeDados(('INSERT INTO books (author, title, words) VALUES'
                      ' ("J.R.R. Tolkien", "Two Towers", 143436)'))
        bancoDeDados(('INSERT INTO books (author, title, words) VALUES'
                      ' ("J.R.R. Tolkien", "Return of the King", 134462)'))
    print(bancoDeDados(('SELECT author, SUM(words) AS total_words FROM books'
                        ' GROUP BY author HAVING total_words > 1000000')))
    print(bancoDeDados(('SELECT author, AVG(words) AS avg_words FROM books'
                        ' GROUP BY author HAVING avg_words > 150000')))


if __name__ == '__main__':
    main()
