import sqlite3
from os.path import exists


def bancoDeDados(*args: tuple):
    """
    Função que comita os comandos sql.
    """
    connection = sqlite3.connect('teste6.db')
    cursor = connection.cursor()
    cursor.execute(*args)
    retorno = cursor.fetchall()
    connection.commit()
    connection.close()
    return retorno


def main():
    existiaDb = exists('teste6.db')
    comandoSql = ('CREATE TABLE IF NOT EXISTS padaria (id INTEGER PRIMARY'
                  ' KEY, nome TEXT, quantidade INTEGER, preço INTEGER,'
                  ' lucro INTEGER)')
    bancoDeDados(comandoSql)
    if not existiaDb:
        bancoDeDados('INSERT INTO padaria VALUES (1, "rosca", 30, 0.30, 0.05)')
        bancoDeDados('INSERT INTO padaria VALUES(2, "pão", 50, 0.20, 0.05)')
        bancoDeDados('INSERT INTO padaria VALUES(3, "pudim", 30, 0.50, 0.15)')
        bancoDeDados(
            'INSERT INTO padaria VALUES(4, "mortadela", 15, 3.00, 1.00)')
        bancoDeDados(
            'INSERT INTO padaria VALUES(5, "iogurte", 20, 2.50, 1.00)')
        bancoDeDados('INSERT INTO padaria VALUES(6, "bolo", 10, 30.00, 10.00)')
        bancoDeDados('INSERT INTO padaria VALUES(7, "torta", 5, 20.00, 7.50)')
        bancoDeDados(
            'INSERT INTO padaria VALUES(8, "brigadeiro", 30, 0.50, 0.15)')
        bancoDeDados('INSERT INTO padaria VALUES(9, "pastel", 15, 1.50, 0.50)')
        bancoDeDados(
            'INSERT INTO padaria VALUES(10, "coxinha", 15, 1.30, 0.40)')
        bancoDeDados(
            'INSERT INTO padaria VALUES(11, "pão de queijo", 200, 0.30, 0.10)')
        bancoDeDados(
            'INSERT INTO padaria VALUES(12, "pão de forma", 10, 2.50, 0.90)')
        bancoDeDados(
            'INSERT INTO padaria VALUES(13, "biscoito", 10, 1.50, 0.50)')
        bancoDeDados(
            'INSERT INTO padaria VALUES(14, "bolacha", 90, 1.50, 0.70)')
        bancoDeDados(
            'INSERT INTO padaria VALUES(15, "chocolate", 50, 0.70, 0.20)')
    print(bancoDeDados('SELECT SUM(lucro) FROM padaria'))
    print(bancoDeDados('SELECT * FROM padaria ORDER BY quantidade'))


if __name__ == '__main__':
    main()
