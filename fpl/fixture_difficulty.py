import requests
import json
import numpy as np
import pandas as pd
import datetime
import re
from pprint import  pprint
import fpl


# Make a get request to get the latest player data from the FPL API
link = "https://fantasy.premierleague.com/api/bootstrap-static/"
response = requests.get(link)

# Convert JSON data to a python object
data = json.loads(response.text)


events = data['events']

events_df = pd.DataFrame(events)




for index, row in events_df.iterrows():
    if str(row['finished']).lower() == 'false':
        current_gw = row['name']
        current_gw = [int(s) for s in re.findall(r'\b\d+\b', current_gw)]
        current_gw= current_gw[0]
        break


def get_team_name(team_code):
    team = str(team_code)
    if len(team) == 1:
        team = team.replace('1', 'Arsenal')
        team = team.replace('2', 'Aston Villa')
        team = team.replace('3', 'Bournemouth')
        team = team.replace('4', 'Brentford')
        team = team.replace('5', 'Brighton')
        team = team.replace('6', 'Chelsea')
        team = team.replace('7', 'Crystal Palace')
        team = team.replace('8', 'Everton')
        team = team.replace('9', 'Fulham')


    elif len(team) == 2:
        team = team.replace('10', 'Leicester')
        team = team.replace('11', 'Leeds')
        team = team.replace('12', 'Liverpool')
        team = team.replace('13', 'Man city')
        team = team.replace('14', 'Man United')
        team = team.replace('15', 'Newcastle')
        team = team.replace('16', 'Nottingham Forest')
        team = team.replace('17', 'Southampton')
        team = team.replace('18', 'Tottenham')
        team = team.replace('19', 'Westham')
        team = team.replace('20', 'Wolves')

    return team

def get_short_team(team_code):
    team = str(team_code)
    if len(team) == 1:
        team = team.replace('1', 'ARS')
        team = team.replace('2', 'AVL')
        team = team.replace('3', 'BOU')
        team = team.replace('4', 'BRE')
        team = team.replace('5', 'BHA')
        team = team.replace('6', 'CHE')
        team = team.replace('7', 'CRY')
        team = team.replace('8', 'EVE')
        team = team.replace('9', 'FUL')


    elif len(team) == 2:
        team = team.replace('10', 'LEI')
        team = team.replace('11', 'LEE')
        team = team.replace('12', 'LIV')
        team = team.replace('13', 'MCI')
        team = team.replace('14', 'MUN')
        team = team.replace('15', 'NEW')
        team = team.replace('16', 'NFO')
        team = team.replace('17', 'SOU')
        team = team.replace('18', 'TOT')
        team = team.replace('19', 'WHU')
        team = team.replace('20', 'WOL')

    return team
next_5 = []
all_distict_teams = ['Arsenal','Aston Villa','Bournemouth','Brentford','Brighton','Chelsea','Crystal Palace','Everton','Fulham','Leicester','Leeds','Liverpool','Man city','Man United','Newcastle','Nottingham Forest','Southampton','Tottenham','Westham','Wolves']

def get_fixtures():
    link2 = 'https://fantasy.premierleague.com/api/fixtures/'
    response = requests.get(link2)

    # Convert JSON data to a python object
    data = json.loads(response.text)



    for i in range(0,5):
        gw = []
        for x in data:
            if x['event'] == current_gw+i:
                gw.append(x)

        total_info = []
        for p in range(0,len(gw)):
            gw_info = {
                'team': get_team_name(gw[p]['team_h']),
                'opponent': get_short_team(gw[p]['team_a'])+'(H)',
                'opponent_difficulty': gw[p]['team_h_difficulty'],


            }

            gw_info2 = {
                'team': get_team_name(gw[p]['team_a']),
                'opponent': get_short_team(gw[p]['team_h'])+'(A)',
                'opponent_difficulty': gw[p]['team_a_difficulty'],

            }


            total_info.append(gw_info)
            total_info.append(gw_info2)

        next_5.append(total_info)





        #pprint(total_info)

    total_data = []


    #pprint(all_distict_teams)


    for i in all_distict_teams:
        fixtures = []
        fixtures_dict = {}

        for gw in next_5:
            found = False
            for games in gw:
                if games['team']==i:
                    fixtures_dict = {
                        'team':games['opponent'],
                        'difficulty': games['opponent_difficulty']
                    }
                    fixtures.append(fixtures_dict)
                    found = True
            if found == False:
                fixtures.append('Blank')
            #print(found)


        data_dict = {
            'team': i,
            'next_5':fixtures
        }

        total_data.append(data_dict)





    return total_data


def get_fixtures_header():
    
    headers = [] # Next 5 game week names

    for xy in range(0,5):
            headers.append(current_gw+xy)
        

    return headers


def get_postponed_games():

    all_distict_teams = ['Arsenal','Aston Villa','Bournemouth','Brentford','Brighton','Chelsea','Crystal Palace','Everton','Fulham','Leicester','Leeds','Liverpool','Man city','Man United','Newcastle','Nottingham Forest','Southampton','Tottenham','Westham','Wolves']
    link2 = 'https://fantasy.premierleague.com/api/fixtures/'
    response = requests.get(link2)

    # Convert JSON data to a python object
    data = json.loads(response.text)
    teams_playing = []
    postponed = []
    for x in data:
        if x['event'] == current_gw:
            teams_playing.append(get_team_name(x['team_h']))
            teams_playing.append(get_team_name(x['team_a']))


    for team in all_distict_teams:
        if team not in teams_playing:
            postponed.append(team)



    return postponed
def get_dataset():
    # Make a get request to get the latest player data from the FPL API
    link5 = "https://fantasy.premierleague.com/api/bootstrap-static/"
    response5 = requests.get(link5)

    # Convert JSON data to a python object
    data5 = json.loads(response5.text)
    all_players = []
    for i in data5['elements']:
        name = i['first_name'] + " " + i['second_name']
        webname = i['web_name']
        team = str(i['team'])
        form_ict_index = float(i['form']) * float(i['ict_index'])


        if len(team)==1:
            team = team.replace('1','Arsenal')
            team = team.replace('2','Aston Villa')
            team = team.replace('3','Bournemouth')
            team = team.replace('4','Brentford')
            team = team.replace('5','Brighton')
            team = team.replace('6','Chelsea')
            team = team.replace('7','Crystal Palace')
            team = team.replace('8','Everton')
            team = team.replace('9','Fulham')
      

      
        elif len(team)==2:
            team = team.replace('10','Leicester')
            team = team.replace('11','Leeds')
            team = team.replace('12','Liverpool')
            team = team.replace('13','Man city')
            team = team.replace('14','Man United')
            team = team.replace('15','Newcastle')
            team = team.replace('16','Nottingham Forest')
            team = team.replace('17','Southampton')
            team = team.replace('18','Tottenham')
            team = team.replace('19','Westham')
            team = team.replace('20','Wolves')
     
            



        stats = [name,form_ict_index,team,webname]
        all_players.append(stats)


    all_players = np.array(all_players)
    dataset = pd.DataFrame({
        'name': all_players[:, 0],
        'form_ict_index': all_players[:,1].astype(float),
        'team': all_players[:,2],
        'webname': all_players[:,3]
        
     


    })


    dataset = dataset.sort_values(by=['form_ict_index'], ascending=False)

    return dataset

def players_to_watch():
    link2 = 'https://fantasy.premierleague.com/api/fixtures/'
    response = requests.get(link2)

    # Convert JSON data to a python object
    data = json.loads(response.text)
    teams_playing = []
   
    dataset = get_dataset()
    
    for x in data:
        if x['event'] == current_gw:
            top_5 = []
            counter = 0
            player_list = []
            for index,row in dataset.iterrows():
                if counter ==5:
                    break
                elif row['team']==get_team_name(x['team_h']):
                    player_list.append(row['webname'])
                    counter = counter +1
                elif row['team']==get_team_name(x['team_a']):
                    player_list.append(row['webname'])
                    counter = counter +1
        
            fixtures = {
            'teams':get_team_name(x['team_h']) + ' VS ' + get_team_name(x['team_a']),
            'players_to_watch':player_list}
            teams_playing.append(fixtures)

           

    return teams_playing
    

