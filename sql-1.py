import sqlite3
import click
from os.path import exists


def bancoDeDados(*args: tuple):
    """
    Função que comita os comandos sql.
    """
    connection = sqlite3.connect('teste.db')
    cursor = connection.cursor()
    cursor.execute(*args)
    retorno = cursor.fetchall()
    connection.commit()
    connection.close()
    return retorno


@click.group()
def main():
    pass


@main.command()
@click.argument('sql', type=click.STRING)
def execute(sql):
    existiaDb = exists('teste.db')
    comandoSql = ('CREATE TABLE IF NOT EXISTS livros ( id INTEGER'
                  ' NOT NULL PRIMARY KEY, livro TEXT, rating INTEGER)')
    bancoDeDados(comandoSql)
    if not existiaDb:
        bancoDeDados('INSERT INTO livros VALUES(1, "SENHOR DOS ANEIS", 5)')
        bancoDeDados('INSERT INTO livros VALUES(2, "GAME OF THRONES", 4)')
        bancoDeDados('INSERT INTO livros VALUES(3, "HARRY POTTER", 4)')
    if click.confirm('tem certeza?'):
        print(bancoDeDados(sql))


if __name__ == '__main__':
    main()
