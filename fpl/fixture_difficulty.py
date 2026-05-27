import requests
import json
import numpy as np
import pandas as pd
import datetime
import re
from pprint import  pprint
import fpl


# Make a get request to get the latest player data from the FPL API'sdd

link = "https://fantasy.premierleague.com/api/bootstrap-static/"
response = requests.get(link)

# Convert JSON data to a python objects
data = json.loads(response.text)
events = data['events']
events_df = pd.DataFrame(events)

team_badge_map = {
    "Arsenal": "https://resources.premierleague.com/premierleague/badges/t3.svg",
    "Aston Villa": "https://resources.premierleague.com/premierleague/badges/t7.svg",
    "Bournemouth": "https://resources.premierleague.com/premierleague/badges/t91.svg",
    "Brentford": "https://resources.premierleague.com/premierleague/badges/t94.svg",
    "Brighton": "https://resources.premierleague.com/premierleague/badges/t36.svg",
    "Burnley": "https://resources.premierleague.com/premierleague/badges/t90.svg",
    "Chelsea": "https://resources.premierleague.com/premierleague/badges/t8.svg",
    "Crystal Palace": "https://resources.premierleague.com/premierleague/badges/t31.svg",
    "Everton": "https://resources.premierleague.com/premierleague/badges/t11.svg",
    "Fulham": "https://resources.premierleague.com/premierleague/badges/t54.svg",
    "Leeds": "https://resources.premierleague.com/premierleague/badges/t2.svg",
    "Liverpool": "https://resources.premierleague.com/premierleague/badges/t14.svg",
    "Man city": "https://resources.premierleague.com/premierleague/badges/t43.svg",
    "Man United": "https://resources.premierleague.com/premierleague/badges/t1.svg",
    "Newcastle": "https://resources.premierleague.com/premierleague/badges/t4.svg",
    "Nottingham Forest": "https://resources.premierleague.com/premierleague/badges/t17.svg",
    "Sunderland": "https://resources.premierleague.com/premierleague/badges/t56.svg",
    "Tottenham": "https://resources.premierleague.com/premierleague/badges/t6.svg",
    "Westham": "https://resources.premierleague.com/premierleague/badges/t21.svg",
    "Wolves": "https://resources.premierleague.com/premierleague/badges/t39.svg"
}



# Default so the module still imports during the off-season, when every event
# is finished and the loop below never finds an "unfinished" gameweek.
current_gw = 1
for index, row in events_df.iterrows():
    if str(row['finished']).lower() == 'false':
        current_gw = row['name']
        current_gw = [int(s) for s in re.findall(r'\b\d+\b', current_gw)]
        current_gw = current_gw[0]
        break

# function to convert the number to the actual team names
def get_team_name(team_code):
   
    team_names = {i+1: team for i, team in enumerate(all_distict_teams)}
   
    return team_names[team_code]


all_distict_teams = ['Arsenal','Aston Villa','Burnley','Bournemouth','Brentford','Brighton','Chelsea','Crystal Palace','Everton','Fulham','Leeds',
                     'Liverpool','Man city','Man United','Newcastle','Nottingham Forest','Sunderland','Tottenham','Westham','Wolves']


#gets the short form of the team name (Arsenal -> ARS)
def get_short_team(team_code):
    team = str(team_code)
    if len(team) == 1:
        team = team.replace('1', 'ARS')
        team = team.replace('2', 'AVL')
        team = team.replace('3', 'BUR')
        team = team.replace('4', 'BOU')
        team = team.replace('5', 'BRE')
        team = team.replace('6', 'BHA')
        team = team.replace('7', 'CHE')
        team = team.replace('8', 'CRY')
        team = team.replace('9', 'EVE')
        

    elif len(team) == 2:
        team = team.replace('10', 'FUL')
        team = team.replace('11', 'LEE')
        team = team.replace('12', 'LIV')
        team = team.replace('13', 'MCI')
        team = team.replace('14', 'MUN')
        team = team.replace('15', 'NEW')
        team = team.replace('16', 'NFO')
        team = team.replace('17', 'SUN')
        team = team.replace('18', 'TOT')
        team = team.replace('19', 'WHU')
        team = team.replace('20', 'WOL')

    return team
next_7 = []

def get_fixtures():
    next_7.clear()
    link2 = 'https://fantasy.premierleague.com/api/fixtures/'
    response = requests.get(link2)

    # Convert JSON data to a python object
    data = json.loads(response.text)

 

    #getting all the games playing in this game week
    for i in range(0, min(7, 39 - current_gw)):
        gw = []
    
        for x in data:
            if x['event']==current_gw+i:
                gw.append(x)
        total_info = [] #a dummy that stores all the fixtures this game week
        final_total_info = [] # a structures list that groups double game weeks
        for p in gw:
            #this stores all the home teams playing
            gw_info= {
                'team': get_team_name(p['team_h']),
                'event': p['event'],
                'opponent': get_short_team(p['team_a']) + '(H)',
                'opponent_difficulty': p['team_h_difficulty']

            }

            #this stores all the away teams playing
            gw_info2 = {
                'team': get_team_name(p['team_a']),
                'event': p['event'],
                'opponent':get_short_team(p['team_h']) + '(A)',
                'opponent_difficulty': p['team_a_difficulty']

            }


            

            total_info.append(gw_info)
            total_info.append(gw_info2)

        all_teams =[] #stores the team name of  all the teams playing
        teams_playing_twice =  []    # stores all the team name of all the teams playing twice 
        teams_playing_once =  []   # stores all the team name of all the teams playing once 


        #from all the games playing this game week, find all the teams that play twice
        for i in range(0, len(total_info)):
            if total_info[i]['team'] not in all_teams:
                all_teams.append(total_info[i]['team'])

            else :
                teams_playing_twice.append(total_info[i]['team'])

        #distincting teams that play once from those that play twice
        for team in all_teams:
            if team not in teams_playing_twice:
                teams_playing_once.append(team)


        teams_playing_twice_indices = [] #stores all the teams that play twice i.e [{'team':'arsenal', index:[1,3]}]
        #the index is where they occur in the total info array which would make it easier for us to access them
        for team in teams_playing_twice:
            team_dict = {
                'team': team,
                'index': []
            }
            teams_playing_twice_indices.append(team_dict)


        # for all the the teams playing twice, append the indices to the 'teams_playing_twice_indices' and the team name
        for i in range(len(total_info)):
            for j in range(len(teams_playing_twice_indices)):
                if total_info[i]['team'] in teams_playing_twice and teams_playing_twice_indices[j]['team']==total_info[i]['team']:
                    teams_playing_twice_indices[j]['index'].append(i)

        #
        for team in teams_playing_twice_indices:
            dgw_info = {
                'team': team['team'],
                'event': total_info[team['index'][0]]['event'],
                'opponent': total_info[team['index'][0]]['opponent'] +' '+  total_info[team['index'][1]]['opponent'],
                'opponent_difficulty': 0

            }

            final_total_info.append(dgw_info)


        for i in range(len(total_info)):
            if total_info[i]['team'] in teams_playing_once:
                final_total_info.append(total_info[i])


        next_7.append(final_total_info)


    total_data = []



    # this handles the blank game week (if the team is not found in the list then make the fixture blank )
    for i in all_distict_teams:
        fixtures = []
        fixtures_dict = {}

        for gw in next_7:
            found = False
            for games in gw:
                if games['team']==i:
                    fixtures_dict = {
                        'team':games['opponent'],
                        'event':games['event'],
                        'difficulty': games['opponent_difficulty']
                    }
                    fixtures.append(fixtures_dict)
                    found = True

            if found == False:
                fixtures.append('Blank')

        fixture_score = calculate_fixture_score(fixtures, horizon=5)
        has_next = isinstance(fixtures[0], dict)

        data_dict = {
            'team': i,
            'badge': team_badge_map[i],
            'next_7': fixtures,
            'fixture_score': fixture_score,
            'next_game_difficulty': fixtures[0]['difficulty'] if has_next else 5,
            'has_next_fixture': has_next
        }

        total_data.append(data_dict)

    


    #pprint(total_data)
    return total_data

def calculate_fixture_score(fixtures, horizon=5):
    """
    Calculate a team's average fixture difficulty over the next horizon games.
    Lower score = tougher fixtures, higher score = easier fixtures.
    Blank GWs (no fixture) count as difficulty 5 — worst case.
    """
    difficulties = [
        f['difficulty'] if isinstance(f, dict) else 5
        for f in fixtures[:horizon]
    ]

    if not difficulties:
        return 0

    return round(sum(difficulties) / len(difficulties), 2)


#gets the name of the next 5 gw's -> [1,2,3,4,5]
def get_fixtures_header():
    
    headers = [] # Next 5 game week names
    max_gw = min(current_gw + 5, 39)  # Ensure the maximum game week is 38

    for gw in range(current_gw, max_gw):
        headers.append(gw)
        

    return headers

#gets a list of postponed games
def get_postponed_games():
    all_distict_teams = ['Arsenal','Aston Villa','Burnley','Brentford','Bournemouth','Brighton', 'Chelsea','Crystal Palace','Everton','Fulham','Leeds',
                     'Liverpool','Man city','Man United','Newcastle','Nottingham Forest','Sunderland','Tottenham','Westham','Wolves']

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




#gets a list of all players
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
        status = i['status']
        form_ict_index = float(i['form']) * float(i['ict_index'])
        photo = i['photo']
        cost = i["now_cost"]/10
        points_per_game = i['points_per_game']
        photo = photo.replace('jpg','png')
        useful_stats = {
            "minutes": i["minutes"],
            "goals_scored": i["goals_scored"],
            "assists": i["assists"],
            "clean_sheets": i["clean_sheets"],
            "goals_conceded": i["goals_conceded"],
            "penalties_saved": i["penalties_saved"],
            "cost" : cost,
            "saves": i["saves"],
            "bps": i["bps"],
            "bonus": i["bonus"],
            "expected_goals": i["expected_goals"],
            "expected_assists": i["expected_assists"],
            "expected_goal_involvements": i["expected_goal_involvements"],
            "expected_goals_conceded": i["expected_goals_conceded"],
            "ict_index": i["ict_index"],
            "influence": i["influence"],
            "creativity": i["creativity"],
            "threat": i["threat"],
            "points_per_game_rank": i["points_per_game_rank"],
            "selected_by_percent": i['selected_by_percent']
        }



        if len(team) == 1:
            team = team.replace('1', 'Arsenal')
            team = team.replace('2', 'Aston Villa')
            team = team.replace('3', 'Burnley')
            team = team.replace('4', 'Bournemouth')
            team = team.replace('5', 'Brentford')
            team = team.replace('6', 'Brighton')
            team = team.replace('7', 'Chelsea')
            team = team.replace('8', 'Crystal Palace')
            team = team.replace('9', 'Everton')
            
            


        elif len(team) == 2:
            team = team.replace('10', 'Fulham')
            team = team.replace('11', 'Leeds')
            team = team.replace('12', 'Liverpool')
            team = team.replace('13', 'Man city')
            team = team.replace('14', 'Man United')
            team = team.replace('15', 'Newcastle')
            team = team.replace('16', 'Nottingham Forest')
            team = team.replace('16', 'Sunderland')
            team = team.replace('18', 'Tottenham')
            team = team.replace('19', 'Westham')
            team = team.replace('20', 'Wolves')
        
    



        stats = [name,form_ict_index,team,webname,status,photo,points_per_game, useful_stats]
        all_players.append(stats)


    all_players = np.array(all_players)
    dataset = pd.DataFrame({
        'name': all_players[:, 0],
        'form_ict_index': all_players[:,1].astype(float),
        'team': all_players[:,2],
        'webname': all_players[:,3],
        'status': all_players[:,4],
        'photo': all_players[:,5],
        'points_per_game': all_players[:,6],
        'stats': all_players[:,7]
    })


    dataset = dataset.sort_values(by=['form_ict_index'], ascending=False)

    return dataset


# function that returns a list of 5 players from both teams in all fixtures that game week that we should watch (might do well)
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
                elif row['team']==get_team_name(x['team_h']) and row['status']=='a':
                    player = { 
                        "name": row["webname"],
                        "photo": row["photo"],
                        "ppg": row["points_per_game"]
                    }
                    player_list.append(player)
                    counter = counter +1
                elif row['team']==get_team_name(x['team_a']) and row['status']=='a':
                    player = { 
                        "name": row["webname"],
                        "photo": row["photo"],
                        "ppg": row["points_per_game"]
                    }
                    player_list.append(player)
                    counter = counter +1
        
            fixtures = {
            'teams':get_team_name(x['team_h']) + ' VS ' + get_team_name(x['team_a']),
            'players_to_watch':player_list}
            teams_playing.append(fixtures) 
    return teams_playing
    

