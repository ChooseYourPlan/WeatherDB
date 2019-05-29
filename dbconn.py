import pymysql

def get_connection():
    temp = open('dbconn.cfg','r').read().split('\n')

    hostname = temp[1]
    username = temp[3]
    password = temp[5]
    database = temp[7]

    myConnection = pymysql.connect( host=hostname, user=username, passwd=password, db=database )
    return myConnection

