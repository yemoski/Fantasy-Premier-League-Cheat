import requests
import json
import numpy as np
import pandas as pd
import datetime
from pprint import  pprint


# Make a get request to get the latest player data from the FPL API
link = "https://fantasy.premierleague.com/api/bootstrap-static/"
response = requests.get(link)

# Convert JSON data to a python object
data = json.loads(response.text)


def get_fixtures():
    player_from_unique_team = []
    unique_team_id = []

    #getting players id from unique 20 teams
    teams_counter = 0
    for z in data['elements']:
        if z['team'] not in unique_team_id and teams_counter < 20:
            unique_team_id.append(z['team'])
            player_from_unique_team.append(z['id'])
            teams_counter = teams_counter + 1

        if teams_counter==20:
            break
 


    all_fixtutes = []
    #Matching the player id to team
    for x in range(0,20):
        # Make sure to keep the trailing in the url
        player_id = player_from_unique_team[x]
        url = 'https://fantasy.premierleague.com/api/element-summary/' + \
               str(player_id) + '/'
        response = requests.get(url)
        fixtures = json.loads(response.text)

        next_5_games = []
        is_home = []
        difficulty = []

        fixtures_dict = {
            'team_id': '',
            'team_name': '',
            'fixtures': ''
        }
        # fixing the opponents team name
        for xy in range(0,5):
            if fixtures['fixtures'][xy]['is_home']:
                opponent = str(fixtures['fixtures'][xy]['team_a'])
                if len(opponent)==1:
                    opponent = opponent.replace('1','ARS')
                    opponent = str(opponent).replace('2','AVL')
                    opponent = str(opponent).replace('3','BOU')
                    opponent = str(opponent).replace('4','BRE')
                    opponent = str(opponent).replace('5','BRI')
                    opponent = str(opponent).replace('6','CHE')
                    opponent = str(opponent).replace('7','CRY')
                    opponent = str(opponent).replace('8','EVE')
                    opponent = str(opponent).replace('9','FUL')
            

                elif len(opponent)==2:
                    opponent = str(opponent).replace('10','LEI')
                    opponent = str(opponent).replace('11','LEE')
                    opponent = str(opponent).replace('12','LIV')
                    opponent = str(opponent).replace('13','MCI')
                    opponent = str(opponent).replace('14','MUFC')
                    opponent = str(opponent).replace('15','NEW')
                    opponent = str(opponent).replace('16','NOT')
                    opponent = str(opponent).replace('17','SOU')
                    opponent = str(opponent).replace('18','TOT')
                    opponent = str(opponent).replace('19','WHU')
                    opponent = str(opponent).replace('20','WOL')

                next_5_games.append(opponent)
                is_home.append(True)
            else:
                opponent = str(fixtures['fixtures'][xy]['team_h'])
                if len(opponent)==1:
                    opponent = opponent.replace('1','ARS')
                    opponent = str(opponent).replace('2','AVL')
                    opponent = str(opponent).replace('3','BOU')
                    opponent = str(opponent).replace('4','BRE')
                    opponent = str(opponent).replace('5','BRI')
                    opponent = str(opponent).replace('6','CHE')
                    opponent = str(opponent).replace('7','CRY')
                    opponent = str(opponent).replace('8','EVE')
                    opponent = str(opponent).replace('9','FUL')
            

                elif len(opponent)==2:
                    opponent = str(opponent).replace('10','LEI')
                    opponent = str(opponent).replace('11','LEE')
                    opponent = str(opponent).replace('12','LIV')
                    opponent = str(opponent).replace('13','MCI')
                    opponent = str(opponent).replace('14','MUFC')
                    opponent = str(opponent).replace('15','NEW')
                    opponent = str(opponent).replace('16','NOT')
                    opponent = str(opponent).replace('17','SOU')
                    opponent = str(opponent).replace('18','TOT')
                    opponent = str(opponent).replace('19','WHU')
                    opponent = str(opponent).replace('20','WOL')

                next_5_games.append(opponent)
                is_home.append(False)
            difficulty.append(fixtures['fixtures'][xy]['difficulty'])

        fixtures_dict['team_id'] = unique_team_id[x]
        fixtures_dict['fixtures'] = next_5_games
        fixtures_dict['is_home'] = is_home
        
        
        if len(str(fixtures_dict['team_id']))==1:
            fixtures_dict['team_id'] = str(fixtures_dict['team_id']).replace('1','Arsenal')
            fixtures_dict['team_id'] = str(fixtures_dict['team_id']).replace('2','Aston Villa')
            fixtures_dict['team_id'] = str(fixtures_dict['team_id']).replace('3','Bournemouth')
            fixtures_dict['team_id'] = str(fixtures_dict['team_id']).replace('4','Brentford')
            fixtures_dict['team_id'] = str(fixtures_dict['team_id']).replace('5','Brighton')
            fixtures_dict['team_id'] = str(fixtures_dict['team_id']).replace('6','Chelsea')
            fixtures_dict['team_id'] = str(fixtures_dict['team_id']).replace('7','Crystal Palace')
            fixtures_dict['team_id'] = str(fixtures_dict['team_id']).replace('8','Everton')
            fixtures_dict['team_id'] = str(fixtures_dict['team_id']).replace('9','Fulham')
            

        elif len(str(fixtures_dict['team_id']))==2:
            fixtures_dict['team_id'] = str(fixtures_dict['team_id']).replace('10','Leicester')
            fixtures_dict['team_id'] = str(fixtures_dict['team_id']).replace('11','Leeds')
            fixtures_dict['team_id'] = str(fixtures_dict['team_id']).replace('12','Liverpool')
            fixtures_dict['team_id'] = str(fixtures_dict['team_id']).replace('13','Man city')
            fixtures_dict['team_id'] = str(fixtures_dict['team_id']).replace('14','Man United')
            fixtures_dict['team_id'] = str(fixtures_dict['team_id']).replace('15','Newcastle')
            fixtures_dict['team_id'] = str(fixtures_dict['team_id']).replace('16','Nottingham Forest')
            fixtures_dict['team_id'] = str(fixtures_dict['team_id']).replace('17','Southampton')
            fixtures_dict['team_id'] = str(fixtures_dict['team_id']).replace('18','Tottenham')
            fixtures_dict['team_id'] = str(fixtures_dict['team_id']).replace('19','Westham')
            fixtures_dict['team_id'] = str(fixtures_dict['team_id']).replace('20','Wolves')

        
        fixtures_dict['fixtures'] = next_5_games
        fixtures_dict['difficulty'] = difficulty


        all_fixtutes.append(fixtures_dict)



    return all_fixtutes


def get_fixtures_header():
    url = 'https://fantasy.premierleague.com/api/element-summary/' + \
               str(1) + '/'
    response = requests.get(url)
    fixtures = json.loads(response.text)

    headers = [] # Next 5 game week names

    for xy in range(0,5):
            headers.append(fixtures['fixtures'][xy]['event'])
        

    return headers



