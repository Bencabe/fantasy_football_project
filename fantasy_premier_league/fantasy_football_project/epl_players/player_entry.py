import requests
import os
import django
import sys
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath('__file__')))
sys.path.append(BASE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'fantasy_football_project.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fantasy_football_project.settings")
django.setup()
api_key = os.environ.get('RAPIDAPI')

from epl_players.models import Player


# delete records in player model to start fresh
Player.objects.all().delete()

# create a list of teams in the league
url = "https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague/table"

headers = {
    'x-rapidapi-host': "heisenbug-premier-league-live-scores-v1.p.rapidapi.com",
    'x-rapidapi-key': api_key
    }

response = requests.request("GET", url, headers=headers)
json_response = json.loads(response.text)
teams = []
for record in json_response['records']:
    teams.append(record['team'])

# create a dictionary with the players in each team in the league
url = "https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague/players"
players = {}
for team in teams:
    querystring = {"team":team}
    response = json.loads(requests.request("GET", url, headers=headers, params=querystring).text)
    if response != {'error': "No data found, player and/or team requested aren't in the database"}:
        players[team] = response['players']
        # print(response)

# iterate over this doctionary to add each player to the players model

for team in players:
    for player in players[team]:
        name_list=player['playerName'].split(' ')
        if len(name_list)>1:
            first_name = name_list[0] 
            second_name = " ".join(name_list[1:])
        else:
            first_name = name_list[0]
            second_name = 'N/A'

        p = Player()
        p.first_name = first_name
        p.last_name = second_name
        p.position = player['position']
        p.football_team = team
        p.save()