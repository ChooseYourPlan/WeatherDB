import requests
import json 
import argparse

#Get Api-Key from File
key_file = open("key.txt","r")
key = key_file.read()

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

args = parser.parse_args()

city = args.city

#Address Addition
additon = '%2C'

if args.BW:
   addition += 'BADEN-W\xc33RTTEMBERG'
elif args.BY:
   additon += 'FREE+STATE+OF+BAVARIA'
elif args.BE:
   additon += 'BERLIN'
elif args.BB:
   additon += 'BRANDENBURG'
elif args.HV:
   additon += 'FREE+HANSEATIC+CITY+OF+BREMEN'
elif args.HH:
   additon += 'HAMBURG'
elif args.HE:
   additon += 'THURINGIA'
elif args.MV:
   additon += 'MECKLENBURG-VORPOMMERN'
elif args.NI:
   additon += 'LOWER SAXONY'
elif args.NW:
     additon += 'NORTH+RHINE-WESTPHALIA'
elif args.RP:
   additon += 'RHINELAND-PALATINATE'
elif args.SL:
   additon += 'SAARLAND'
elif args.SN:
   additon += 'SAXONY'
elif args.ST:
   additon += 'SAXONY-ANHALT'
elif args.SH:
   additon += 'SCHLESWIG-HOLSTEIN'
elif args.TH:
   additon += 'THURINGIA'

#Get-Request for lat and lng
response = requests.get("https://www.mapquestapi.com/geocoding/v1/address?key=" + str(key) + "&inFormat=kvp&outFormat=json&location=" + city + additon + "%2CGermany&thumbMaps=false")

#Json evaluation
json_data = json.loads(response.text)

bundesland = json_data['results'][0]['locations'][0]['adminArea3']
lat  = json_data['results'][0]['locations'][0]['latLng']['lat']
lng  = json_data['results'][0]['locations'][0]['latLng']['lng']

#Print to console
print bundesland
print lat
print lng 
