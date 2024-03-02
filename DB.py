import mysql.connector

class DBCon():
    def conn(self):
        mydb=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="",
            database="Shop2"
            )

        return mydb