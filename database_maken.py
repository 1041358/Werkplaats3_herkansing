import random
import sqlite3
from accesskey import accesskey_function


class HighScores:
    def __init__(self, database_file_name):
        self.database_file_name = database_file_name
        self.init_database()

    def init_database(self):
        conn = sqlite3.connect(self.database_file_name)
        cur = conn.cursor()
        sql = "CREATE TABLE IF NOT EXISTS Games " \
              "(game_id INTEGER PRIMARY KEY AUTOINCREMENT , email TEXT NOT NULL, naam_game TEXT NOT NULL, accesskey TEXT NOT NULL);"
        cur.execute(sql)
        sql = "CREATE TABLE IF NOT EXISTS Highscores" \
              "(highscore_id INTEGER PRIMARY KEY AUTOINCREMENT, datum TEXT NOT NULL, gametag TEXT NOT NULL, score INTEGER NOT NULL, game_id INTEGER NOT NULL)"
        cur.execute(sql)
        conn.commit()
        conn.close()
    
    def insert_scores(self, gametag, score, game_id):
        conn = sqlite3.connect(self.database_file_name)
        cur = conn.cursor()
        sql = "INSERT INTO Highscores VALUES (?, CURRENT_TIMESTAMP, ?, ?, ?)"
        cur.execute(sql, [None, gametag, score, game_id])
        print(gametag + " heeft een score van "+ str(score))
        conn.commit()
        conn.close()

    def insert_game(self, email, naam_game, accesskey):
        conn = sqlite3.connect(self.database_file_name)
        cur = conn.cursor()
        sql = "INSERT INTO Games VALUES (?, ?, ?, ?)"
        cur.execute(sql, [None, email, naam_game, accesskey])
        print("De accesskey van de game " + naam_game + " is " + str(accesskey))
        conn.commit()
        conn.close()

highscores = HighScores("games.db")
highscores.insert_scores("Jelle", 1000, 1)
highscores.insert_game("joost@gmail.com", "Scrabble", accesskey_function())