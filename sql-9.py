import sqlite3
from os.path import exists


def bancoDeDados(*args: tuple):
    """
    Função que comita os comandos sql.
    """
    connection = sqlite3.connect('teste9.db')
    cursor = connection.cursor()
    cursor.execute(*args)
    retorno = cursor.fetchall()
    connection.commit()
    connection.close()
    return retorno


def main():
    existiaDb = exists('teste9.db')
    comandoSql = ('CREATE TABLE IF NOT EXISTS exercise_logs (id INTEGER'
                  ' PRIMARY KEY AUTOINCREMENT, type TEXT, minutes INTEGER,'
                  ' calories INTEGER, heart_rate INTEGER)')
    comandoSql2 = ('CREATE TABLE IF NOT EXISTS drs_favorites (id INTEGER'
                   ' PRIMARY KEY, type TEXT, reason TEXT)')
    bancoDeDados(comandoSql)
    bancoDeDados(comandoSql2)
    if not existiaDb:
        # table exercise_logs
        bancoDeDados(('INSERT INTO exercise_logs(type, minutes, calories,'
                      ' heart_rate) VALUES ("biking", 30, 100, 110)'))
        bancoDeDados(('INSERT INTO exercise_logs(type, minutes, calories,'
                      ' heart_rate) VALUES ("biking", 10, 30, 105)'))
        bancoDeDados(('INSERT INTO exercise_logs(type, minutes, calories,'
                      ' heart_rate) VALUES ("dancing", 15, 200, 120)'))
        bancoDeDados(('INSERT INTO exercise_logs(type, minutes, calories,'
                      ' heart_rate) VALUES ("tree climbing", 30, 70, 90)'))
        bancoDeDados(('INSERT INTO exercise_logs(type, minutes, calories,'
                      ' heart_rate) VALUES ("tree climbing", 25, 72, 80)'))
        bancoDeDados(('INSERT INTO exercise_logs(type, minutes, calories,'
                      ' heart_rate) VALUES ("rowing", 30, 70, 90)'))
        bancoDeDados(('INSERT INTO exercise_logs(type, minutes, calories,'
                      ' heart_rate) VALUES ("hiking", 60, 80, 85)'))
        # table drs_favorites
        bancoDeDados(('INSERT INTO drs_favorites(type, reason) VALUES'
                      ' ("biking", "Improves endurance and flexibility.")'))
        bancoDeDados(('INSERT INTO drs_favorites(type, reason) VALUES'
                      ' ("hiking", "Increases cardiovascular health.")'))
    print(bancoDeDados(('SELECT * FROM exercise_logs WHERE type = "biking" OR'
                        ' type = "hiking" OR type = "tree climbing" OR '
                        'type = "rowing"')))
    print(bancoDeDados(('SELECT * FROM exercise_logs WHERE type NOT IN'
                        ' ("biking", "hiking", "tree climbing", "rowing")')))
    print(bancoDeDados('SELECT type FROM drs_favorites'))
    print(bancoDeDados(('SELECT * FROM exercise_logs WHERE type IN (SELECT'
                        ' type FROM drs_favorites)')))
    print(bancoDeDados(('SELECT * FROM exercise_logs'
                        ' WHERE type IN '
                        '(SELECT type FROM drs_favorites '
                        'WHERE reason = "Increases cardiovascular health.")')))
    print(bancoDeDados(('SELECT * FROM exercise_logs'
                        ' WHERE type IN '
                        '(SELECT type FROM drs_favorites '
                        'WHERE reason LIKE "%cardiovascular%")')))


if __name__ == '__main__':
    main()
