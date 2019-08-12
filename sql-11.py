import sqlite3
from os.path import exists


def bancoDeDados(*args: tuple):
    """
    Função que comita os comandos sql.
    """
    connection = sqlite3.connect('teste11.db')
    cursor = connection.cursor()
    cursor.execute(*args)
    retorno = cursor.fetchall()
    connection.commit()
    connection.close()
    return retorno


def main():
    existiaDb = exists('teste11.db')
    comandoSql = ('CREATE TABLE IF NOT EXISTS exercise_logs (id INTEGER '
                  'PRIMARY KEY AUTOINCREMENT, type TEXT, minutes INTEGER,'
                  ' calories INTEGER, heart_rate INTEGER)')
    bancoDeDados(comandoSql)
    if not existiaDb:
        bancoDeDados(('INSERT INTO exercise_logs(type, minutes, calories,'
                      ' heart_rate) VALUES ("biking", 30, 115, 110)'))
        bancoDeDados(('INSERT INTO exercise_logs(type, minutes, calories,'
                      ' heart_rate) VALUES ("biking", 10, 45, 105)'))
        bancoDeDados(('INSERT INTO exercise_logs(type, minutes, calories,'
                      ' heart_rate) VALUES ("dancing", 15, 200, 120)'))
        bancoDeDados(('INSERT INTO exercise_logs(type, minutes, calories,'
                      ' heart_rate) VALUES ("dancing", 15, 165, 120)'))
        bancoDeDados(('INSERT INTO exercise_logs(type, minutes, calories,'
                      ' heart_rate) VALUES ("tree climbing", 30, 70, 90)'))
        bancoDeDados(('INSERT INTO exercise_logs(type, minutes, calories,'
                      ' heart_rate) VALUES ("tree climbing", 25, 72, 80)'))
        bancoDeDados(('INSERT INTO exercise_logs(type, minutes, calories,'
                      ' heart_rate) VALUES ("rowing", 30, 70, 90)'))
        bancoDeDados(('INSERT INTO exercise_logs(type, minutes, calories,'
                      ' heart_rate) VALUES ("hiking", 60, 80, 85)'))
    print(bancoDeDados('SELECT * FROM exercise_logs'))
    print(bancoDeDados(('SELECT type, SUM(calories) AS total_calories FROM'
                        ' exercise_logs GROUP BY type')))
    print(bancoDeDados(('SELECT type, SUM(calories) AS total_calories FROM'
                        ' exercise_logs GROUP BY type HAVING total_calories'
                        ' > 150')))
    print(bancoDeDados(('SELECT type, AVG(calories) AS avg_calories FROM'
                        ' exercise_logs GROUP BY type HAVING avg_calories'
                        ' > 70')))
    print(bancoDeDados(('SELECT type FROM exercise_logs GROUP BY type HAVING'
                        ' COUNT(*) >= 2')))


if __name__ == '__main__':
    main()
