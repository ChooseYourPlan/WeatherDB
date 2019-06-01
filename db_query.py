import dbconn as dbc


def insert_db(values):
    connection = dbc.get_connection()
    
    with connection.cursor() as cursor:
         sql = "DROP TABLE IF EXISTS wetter"
         cursor.execute(sql)
         sql = "CREATE TABLE wetter (latitude float NOT NULL,longtitude float NOT NULL,timezone VARCHAR(60) NOT NULL, currently_summary VARCHAR(120),currently_temperature float NOT NULL ,currently_time VARCHAR(30),currently_apparentTemperature float, cuurently_humidity float, currently_pressure float, currently_windSpeed float, currently_cloudCover float, currently_visibility float);"
        
         cursor.execute(sql)
          
         sql = "INSERT INTO wetter (latitude, longtitude, timezone, currently_summary, currently_temperature, currently_time) VALUES ("+ str(values[0]) + "," + str(values[1]) + ",'" + values[2] + "','" + str(values[3]) + "'," + str(values[4]) + ",'" + str(values[5]) + "');"
         
         sql = "INSERT INTO wetter VALUES ("

         for value in values:
             if isinstance(value,basestring):
                 sql = sql + "'" + value + "',"
             else:
                 sql = sql + str(value) + ","

         sql = sql[:-1] +  ");"

         cursor.execute(sql) 
         connection.commit()
         result = cursor.fetchone()
         print result
