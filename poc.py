import requests
import json 
import argparse
import statebyargs as stba
import weathload as wl
import valuesbydata as vbd
import db_query as dbq

def get_apik():
#Get Api-Key from File
    key_file = open("key.txt","r")
    key = key_file.read()
    return key

#CLI-Arguments
parser = argparse.ArgumentParser(description='lat and lng getter')
parser.add_argument('-c','--city',type = str, help = 'City to Request')
parser.add_argument('-BW','--Baden-Wuerttemberg',dest = 'BW',action = 'store_true', help = 'Baden-Wuerttemberg')
parser.add_argument('-BY','--Bayern',dest = 'BY',action = 'store_true', help = 'Bayern')
parser.add_argument('-BE','--Berlin',dest = 'BE',action = 'store_true', help = 'Berlin')
parser.add_argument('-BB','--Brandenburg',dest = 'BB',action = 'store_true', help = 'Brandenburg')
parser.add_argument('-HV','--Bremen',dest = 'HV',action = 'store_true', help = 'Bremen')
parser.add_argument('-HH','--Hamburg',dest = 'HH',action = 'store_true', help = 'Hamburg')
parser.add_argument('-HE','--Hessen',dest = 'HE',action = 'store_true', help = 'Hessen')
parser.add_argument('-MV','--Mecklenburg-Vorpommern',dest = 'MV',action = 'store_true', help = 'Mecklenburg-Vorpommern')
parser.add_argument('-NI','--Niedersachsen',dest = 'NI',action = 'store_true', help = 'Niedersachsen')
parser.add_argument('-NW','--Nordrhein-Westfalen',dest = 'NW',action = 'store_true', help = 'Nordrhein-Westfalen')
parser.add_argument('-RP','--Rheinland-Pfalz',dest = 'RP',action = 'store_true', help = 'Rheinland-Pfalz')
parser.add_argument('-SL','--Saarland',dest = 'SL',action = 'store_true', help = 'Saarland')
parser.add_argument('-SN','--Sachsen',dest = 'SN',action = 'store_true', help = 'Sachsen')
parser.add_argument('-ST','--Sachsen-Anhalt',dest = 'ST',action = 'store_true', help = 'Sachsen-Anhalt')
parser.add_argument('-SH','--Schleswig-Holstein',dest = 'SH',action = 'store_true', help = 'Schleswig-Holstein')
parser.add_argument('-TH','--Thueringen',dest = 'TH',action = 'store_true', help = 'Thueringen')
parser.add_argument('-D', '--date',dest = 'date', help="Date format YYYY-MM-DD HH:MM")
parser.add_argument('-H','--Hourly',dest = 'H', help = 'Hourly Report for 1 Year', action = 'store_true')

def get_request(city,state,key):
#Get-Request for lat and lng
    response = requests.get("https://www.mapquestapi.com/geocoding/v1/address?key=" + str(key) + "&inFormat=kvp&outFormat=json&location=" + city + state + "%2CGermany&thumbMaps=false")
    return response

def get_jsond(response):
#Json evaluation
    json_data = json.loads(response.text)

    bundesland = json_data['results'][0]['locations'][0]['adminArea3']
    lat  = json_data['results'][0]['locations'][0]['latLng']['lat']
    lng  = json_data['results'][0]['locations'][0]['latLng']['lng']

    info_list = [bundesland,lat,lng]
    return info_list

def getter(args,info_list):
#Getter method (moved from Main)
    if args.H:
       values = []
       for j in range(0,364):
           data = wl.get_weather(info_list,args,j)
           for x in range(1,23):
               value = vbd.get_values(data,x)
               values.append(value) 
    else:
       data = wl.get_weather(info_list,args)
       values = vbd.get_values(data)
       values = [values]
       return values
    return values

def main():
#Main method
    key = get_apik()
    args = parser.parse_args()
    city = args.city
    state = stba.get_state(args) 
    response = get_request(city,state,key) 
    info_list = get_jsond(response)
    values = getter(args,info_list)
    dbq.insert_db(values)
    print values, city

if __name__ == '__main__':
    main()
