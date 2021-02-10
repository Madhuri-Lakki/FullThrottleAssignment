from throttle_app.Database import Database
import json
from pandas import DataFrame
import pandas as pd


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

        sessions = []
        for id,row in result2.iterrows():
            a,b = row['start_time'],row['end_time']
            records = list(zip(a,b))
            records = [{'start_time':s,'end_time':e} for s,e in records]
            sessions.append((id,records)) 


        session = DataFrame(sessions,columns=['id','activity_periods'])
        out = pd.merge(result1,session)
        out = out.to_dict(orient='records')

        container = {"ok":"true","members":out}

        return json.dumps(container)
