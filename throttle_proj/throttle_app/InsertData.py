from throttle_app.Database import Database
import json



class InsertThrottleData(object):

    def __init__(self,inputdata):


        self.id = inputdata['id']
        self.real_name = inputdata['real_name']
        self.tz = inputdata['tz']
        self.activity_periods = inputdata['activity_periods']


        print("Connecting to database...")

    def insertuserdata(self):

        db1 = Database()
        conn = db1.getConnection()
        cursor = conn.cursor()

        Result = cursor.execute("insert into User(id,real_name,tz) values(%s,%s,%s)",(self.id,self.real_name,self.tz))

        conn.commit()
        for i in self.activity_periods:

            start_time = i['start_time']
            
            end_time = i['end_time']
            Result2 = cursor.execute("insert into ActivityPeriod(id,start_time,end_time) values(%s,%s,%s)",(self.id,start_time,end_time))
            conn.commit()
        print("query got executed...")

        



