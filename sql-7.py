import sqlite3
from os.path import exists


def bancoDeDados(*args: tuple):
    """
    Função que comita os comandos sql.
    """
    connection = sqlite3.connect('teste7.db')
    cursor = connection.cursor()
    cursor.execute(*args)
    retorno = cursor.fetchall()
    connection.commit()
    connection.close()
    return retorno


def main():
    existiaDb = exists('teste7.db')
    comandoSql = ('CREATE TABLE IF NOT EXISTS logs_exercicios (id INTEGER'
                  ' PRIMARY KEY AUTOINCREMENT, tipo TEXT, minutos'
                  ' INTEGER, calorias INTEGER, frequencia_cardiaca INTEGER)')
    bancoDeDados(comandoSql)
    if not existiaDb:
        bancoDeDados(('INSERT INTO logs_exercicios(tipo, minutos, calorias,'
                      ' frequencia_cardiaca) VALUES ("biking", 30, 100, 110)'))
        bancoDeDados(('INSERT INTO logs_exercicios(tipo, minutos, calorias,'
                      ' frequencia_cardiaca) VALUES ("biking", 10, 30, 105)'))
        bancoDeDados(('INSERT INTO logs_exercicios(tipo, minutos, calorias,'
                      ' frequencia_cardiaca) VALUES ("dancing", 15, 200, 120)'
                      ))
    print(bancoDeDados(('SELECT * FROM logs_exercicios WHERE calorias > 50'
                        ' ORDER BY calorias')))
    print(bancoDeDados(
        'SELECT * FROM logs_exercicios WHERE calorias > 50 AND minutos < 30'))
    print(bancoDeDados(('SELECT * FROM logs_exercicios WHERE calorias >'
                        ' 50 OR frequencia_cardiaca > 100')))


if __name__ == '__main__':
    main()
