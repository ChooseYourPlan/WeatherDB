import requests
import json 
import argparse
import getstate as gs

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

def get_request(city,state,key):
#Get-Request for lat and lng
    response = requests.get("https://www.mapquestapi.com/geocoding/v1/address?key=" + str(key) + "&inFormat=kvp&outFormat=json&location=" + city + state + "%2CGermany&thumbMaps=false")
    return response

def get_jsond(json_data):
#Json evaluation
    json_data = json.loads(response.text)

    bundesland = json_data['results'][0]['locations'][0]['adminArea3']
    lat  = json_data['results'][0]['locations'][0]['latLng']['lat']
    lng  = json_data['results'][0]['locations'][0]['latLng']['lng']

    info_list = [bundesland,lat,lng];
    return info_list

def ausgabe(info_list):
#Print to console
   print info_list[0]
   print info_list[1]
   print info_list[2]

if __name__ == '__main__':
    key = get_apik()
    args = parser.parse_args()
    city = args.city
    state = gs.get_state(args) 
    response = get_request(city,state,key) 
    info_list = get_jsond(response)
    ausgabe(info_list)