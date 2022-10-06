import requests
import json
import numpy as np
import pandas as pd
from datetime import datetime
from pprint import  pprint
import re




# GETTING GAME WEEK DEADLINE 
# Make a get request to get the latest player data from the FPL API
link3 = "https://fantasy.premierleague.com/api/bootstrap-static/"
response3 = requests.get(link3)

# Convert JSON data to a python object
data3 = json.loads(response3.text)

events = data3['events']

events_df = pd.DataFrame(events)


current_gameweek = {'Gameweek': ''}

for index, row in events_df.iterrows():
    if str(row['finished']).lower() == 'false':
        current_gameweek['Gameweek'] = row['name']
        current_gw = [int(s) for s in re.findall(r'\b\d+\b', current_gameweek['Gameweek'])]
        current_gw= current_gw[0]
        break



# Make a get request to get the latest player data from the FPL API
link2 = "https://fantasy.premierleague.com/api/bootstrap-static/"
response2 = requests.get(link2)

# Convert JSON data to a python object
data2 = json.loads(response2.text)
all_players = []
for i in data2['elements']:
    first_name = i['first_name']
    second_name = i['second_name']
    id = i['id']
    full_name = first_name + ' ' + second_name
    row = {
        'id': id,
        'name': full_name
    }

    all_players.append(row)


def get_player_name(player_code):
   for i in all_players:
       if player_code==i['id']:
           return i['name']




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


def get_team_badge(code):
    team = get_team_name(code)

    team_shirt = team

    team_shirt = team_shirt.replace('Arsenal',
                                    'https://resources.premierleague.com/premierleague/badges/70/t3.png')
    team_shirt = team_shirt.replace('Aston Villa',
                                    'https://resources.premierleague.com/premierleague/badges/70/t7.png')
    team_shirt = team_shirt.replace('Bournemouth',
                                    'https://resources.premierleague.com/premierleague/badges/70/t91.png')
    team_shirt = team_shirt.replace('Brentford',
                                    'https://resources.premierleague.com/premierleague/badges/70/t94.png')
    team_shirt = team_shirt.replace('Brighton',
                                    'https://resources.premierleague.com/premierleague/badges/70/t36.png')
    team_shirt = team_shirt.replace('Chelsea',
                                    'https://resources.premierleague.com/premierleague/badges/70/t8.png')
    team_shirt = team_shirt.replace('Crystal Palace',
                                    'https://resources.premierleague.com/premierleague/badges/70/t31.png')
    team_shirt = team_shirt.replace('Everton',
                                    'https://resources.premierleague.com/premierleague/badges/70/t11.png')
    team_shirt = team_shirt.replace('Fulham',
                                    'https://resources.premierleague.com/premierleague/badges/70/t54.png')


    team_shirt = team_shirt.replace('Leicester',
                                    'https://resources.premierleague.com/premierleague/badges/70/t13.png')
    team_shirt = team_shirt.replace('Leeds',
                                    'https://resources.premierleague.com/premierleague/badges/70/t2.png')
    team_shirt = team_shirt.replace('Liverpool',
                                    'https://resources.premierleague.com/premierleague/badges/70/t14.png')
    team_shirt = team_shirt.replace('Man city',
                                    'https://resources.premierleague.com/premierleague/badges/70/t43.png')
    team_shirt = team_shirt.replace('Man United',
                                    'https://resources.premierleague.com/premierleague/badges/70/t1.png')
    team_shirt = team_shirt.replace('Newcastle',
                                    'https://resources.premierleague.com/premierleague/badges/70/t4.png')
    team_shirt = team_shirt.replace('Nottingham Forest',
                                    'https://resources.premierleague.com/premierleague/badges/70/t17.png')
    team_shirt = team_shirt.replace('Southampton',
                                    'https://resources.premierleague.com/premierleague/badges/70/t20.png')
    team_shirt = team_shirt.replace('Tottenham',
                                    'https://resources.premierleague.com/premierleague/badges/70/t6.png')
    team_shirt = team_shirt.replace('Westham',
                                    'https://resources.premierleague.com/premierleague/badges/70/t21.png')
    team_shirt = team_shirt.replace('Wolves',
                                    'https://resources.premierleague.com/premierleague/badges/70/t39.png')


    return team_shirt





def get_livescore():

    

    link2 = 'https://fantasy.premierleague.com/api/fixtures/'
    response = requests.get(link2)

    # Convert JSON data to a python object
    data = json.loads(response.text)

    #list of games in this game week
    gw = []


    #Distinct days in the game week {Friday, saturday, sunday etc}
    distinct_days = []

    distinct_days_dict = {
        'day': '',
        'games':[]
    }






    for x in data:
        if x['event']==current_gw:
            gw.append(x)





    total_info = []
    for p in range(0,len(gw)):
        time = gw[p]['kickoff_time']
        time_arr = time.split('T',1)
        time = time_arr[0] # Date part of the datetime
        time_2 = time_arr[1] #Time part of the datetime
        time_2 = time_2.split('Z',1)
        time2 = datetime.strptime(time_2[0],'%H:%M:%S')
        time = datetime.strptime(time,'%Y-%m-%d')
        month_name = str(time.strftime('%B'))
        year = str(time.strftime('%Y'))
        day = str(time.strftime('%d'))

        day_name = pd.Timestamp(time)
        day_name = day_name.day_name() 
        full_date = day_name + ', '+day+ ' '+ month_name + ' ' + year + ' at '+ time_2[0] +  ' UK Time'

        if day_name not in distinct_days :
            distinct_days.append(day_name)


        #If the game has been played or is being played
        if gw[p]['stats'] != []:
            goal_scored =  gw[p]['stats'][0]
            assist = gw[p]['stats'][1]
            own_goals = gw[p]['stats'][2]
            mins = gw[p]['minutes'] #Current minute in the game
            finished = gw[p]['finished'] # Has the game finished
            started = gw[p]['started'] #Has the game started
            total_events = []
            yellow_cards = gw[p]['stats'][5]
            red_cards = gw[p]['stats'][6]
            bonus = gw[p]['stats'][8]
            #Getting all the stats (goal scored, assist, own goal and bonus ) for away team
            for z in goal_scored['a']:
                events_dict = {
                    'event_name': 'goal_scored',
                    'player_name': get_player_name(z['element'])+' x'+str(z['value']),
                    'team': 'a'

                }

                total_events.append(events_dict)
            for z in assist['a']:
                events_dict = {
                    'event_name': 'assist',
                    'player_name': get_player_name(z['element'])+' x'+str(z['value']),
                    'team': 'a'

                }

                total_events.append(events_dict)
            for z in own_goals['a']:
                events_dict = {
                    'event_name': 'own_goal',
                    'player_name': get_player_name(z['element'])+' x'+str(z['value']),
                    'team': 'a'

                }

                total_events.append(events_dict)
            for z in bonus['a']:
                events_dict = {
                    'event_name': 'bonus',
                    'player_name': get_player_name(z['element'])+' ='+str(z['value']),
                    'team': 'a'

                }

                total_events.append(events_dict)


            #Getting all the stats (goal scored, assist, own goal and bonus ) for away team
            for z in goal_scored['h']:
                events_dict = {
                    'event_name': 'goal_scored',
                    'player_name': get_player_name(z['element'])+' x'+str(z['value']),
                    'team': 'h'

                }
                total_events.append(events_dict)
            for z in assist['h']:
                events_dict = {
                    'event_name': 'assist',
                    'player_name': get_player_name(z['element'])+' x'+str(z['value']),
                    'team': 'h'

                }

                total_events.append(events_dict)
            for z in own_goals['h']:
                events_dict = {
                    'event_name': 'own_goal',
                    'player_name': get_player_name(z['element'])+' x'+str(z['value']),
                    'team': 'h'

                }

                total_events.append(events_dict)
            for z in bonus['h']:
                events_dict = {
                    'event_name': 'bonus',
                    'player_name': get_player_name(z['element'])+' ='+str(z['value']),
                    'team': 'h'

                }

                total_events.append(events_dict)


            
        
            game_info = {
                'kick_off_time':full_date,
                'started': started,
                'finished': finished ,
                'minutes': mins,
                'team_h':get_team_name(gw[p]['team_h']),
                 'team_a':get_team_name(gw[p]['team_a']),
                 'team_h_score':gw[p]['team_h_score'],
                 'team_a_score':gw[p]['team_a_score'],
                 'team_h_badge':get_team_badge(gw[p]['team_h']),
                 'team_a_badge':get_team_badge(gw[p]['team_a']),
                 'events':total_events

                }
        #If the game has not been played yet
        else:
            total_events = None
            mins = gw[p]['minutes'] #Current minute in the game
            finished =  gw[p]['finished'] # Has the game finished
            started = gw[p]['started'] #Has the game started
            
            game_info = {
                'kick_off_time':full_date,
                'started': started,
                'finished': finished,
                'minutes': mins,
                'team_h':get_team_name(gw[p]['team_h']),
                 'team_a':get_team_name(gw[p]['team_a']),
                 'team_h_score':gw[p]['team_h_score'],
                 'team_a_score':gw[p]['team_a_score'],
                 'team_h_badge':get_team_badge(gw[p]['team_h']),
                 'team_a_badge':get_team_badge(gw[p]['team_a']),
                 'events':total_events

                }
        total_info.append(game_info)
    new_list = []
    for days in distinct_days:
        for y in range(0,len(total_info)):
            if total_info[y]['kick_off_time'].find(days)!=-1:
              new_list.append(total_info[y]['team_h'])

    #print(new_list) 
    info = {
        'game_week': current_gw,
        'days': distinct_days,
        'Game_results': total_info

    }
    
    return info
