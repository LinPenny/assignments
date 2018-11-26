1. 
https://api.propublica.org/congress/v1/house/votes/recent.json


2. 
https://api.propublica.org/congress/v1/members/house/MO/current.json
https://api.propublica.org/congress/v1/members/senate/MO/current.json

#What would happen if I take out the 'chamber' parameter or use 'both'?
#https://api.propublica.org/congress/v1/members/{chamber}/{state}/current.json 
#https://api.propublica.org/congress/v1/members/MO/current.json
#https://api.propublica.org/congress/v1/members/both/MO/current.json

#What about adding a 'state' parameter to the 'list of members' request?
#https://api.propublica.org/congress/v1/{congress}/{chamber}/members.json    
#https://api.propublica.org/congress/v1/115/house/MO/members.json
#https://api.propublica.org/congress/v1/115/senate/MO/members.json


3.
https://api.propublica.org/congress/v1/senate/votes/2017-04-06/2017-04-07.json


4.
import json
import requests

API_KEY = 'OylOqGPorg2UjpgDMgoGnVtRBKDhcNn7q6XF0rVb' #same key for different APIs?

url = https://api.propublica.org/congress/v1/115/senate/members/leaving.json
#url = https://api.propublica.org/congress/v1/115/house/members/leaving.json

response = requests.get(url, headers={"X-API-Key": API_KEY}).content

data = json.loads(response)

print data['results'][0]['members'][0]['first_name', 'last_name']
