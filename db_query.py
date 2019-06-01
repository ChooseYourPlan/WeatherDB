import dbconn as dbc


def insert_db(values):
    connection = dbc.get_connection()
    
    with connection.cursor() as cursor:
         sql = "DROP TABLE IF EXISTS wetter"
         cursor.execute(sql)
         sql = "CREATE TABLE wetter (latitude float NOT NULL,longtitude float NOT NULL,timezone VARCHAR(60) NOT NULL, currently_summary VARCHAR(120),currently_temperature float NOT NULL ,currently_time VARCHAR(30),currently_apparentTemperature float, cuurently_humidity float, currently_pressure float, currently_windSpeed float, currently_cloudCover float, currently_visibility float);"
        
         cursor.execute(sql)
           
         sql = "INSERT INTO wetter VALUES ("
            
         for list in values:
             for value in list: 
                  if isinstance(value,basestring):
                      sql = sql + "'" + value + "',"
                  else:
                      sql = sql + str(value) + ","

             sql = sql[:-1] +  "),("
         
         sql = sql[:-2] + ";"

         cursor.execute(sql) 
         connection.commit()
