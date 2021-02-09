from throttle_app.Database import Database
import json
from pandas import DataFrame


class DisplayThrottleData(object):

    def __init__(self):

        print("Connecting to database...")

    def displaydata(self):

        db1 = Database()
        conn = db1.getConnection()
        cursor = conn.cursor()

        cursor.execute("select * from User")

        

        result1 = DataFrame(cursor.fetchall(), columns=cursor.column_names)


        cursor.execute("select * from ActivityPeriod")
        result2 = DataFrame(cursor.fetchall(), columns=cursor.column_names)

        result2 = result2.groupby('id').agg({
            'start_time':list,
            'end_time':list,
        })

        sessions = {}
        for id,row in result2.iterrows():
            a,b = row['start_time'],row['end_time']
            sessions[id] = list(zip(a,b))

        print(sessions)
        return None
