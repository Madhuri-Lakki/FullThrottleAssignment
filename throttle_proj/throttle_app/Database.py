import mysql.connector


class Database(object):

    def __init__(self):
        print("Connecting to database...")

    def getConnection(self):       
        conn = mysql.connector.connect(
        host="localhost",
        database="THROTTLE",
        user="root",
        password="Lakki@123"
        )


        print("sucess")

        return conn   




