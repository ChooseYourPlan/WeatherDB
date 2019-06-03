import dbconn as dbc


def insert_db(values):
    connection = dbc.get_connection()
    
    with connection.cursor() as cursor:
         sql = "DROP TABLE IF EXISTS wetter"
         cursor.execute(sql)
         sql = "CREATE TABLE wetter (latitude float NOT NULL,longtitude float NOT NULL,timezone VARCHAR(60) NOT NULL, summary VARCHAR(120),icon VARCHAR(25),preciptype VARCHAR(25),temperature float NOT NULL ,time VARCHAR(30),apparentTemperature float, cuurently_humidity float, dewPoint float, windSpeed float, cloudCover float, visibility float, uvIndex float);"
        
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
