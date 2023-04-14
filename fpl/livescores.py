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
    web_name = i['web_name']
    
    id = i['id']
    
    row = {
        'id': id,
        'name': web_name
    }

    all_players.append(row)

# returns the name of the player when you give it the code of the player
def get_player_name(player_code):
   for i in all_players:
       if player_code==i['id']:
           return i['name']

# returns the stadium name when you give it the code of the stadium
def get_home_stadium(team_code):
    team = str(team_code)
    if len(team) == 1:
        team = team.replace('1', 'Emirates Stadium, London')
        team = team.replace('2', 'Villa Park, Birmingham')
        team = team.replace('3', 'Vitality Stadium, Bournemouth')
        team = team.replace('4', 'Gtech Community Stadium, London')
        team = team.replace('5', 'Amex Stadium, Falmer')
        team = team.replace('6', 'Stamford Bridge, London')
        team = team.replace('7', 'Selhurst Park, London')
        team = team.replace('8', 'Goodison Park, Liverpool')
        team = team.replace('9', 'Craven Cottage, London')


    elif len(team) == 2:
        team = team.replace('10', 'King Power Stadium, Leicester')
        team = team.replace('11', 'Elland Road, Leeds')
        team = team.replace('12', 'Anfield, Liverpool')
        team = team.replace('13', 'Etihad, Manchester')
        team = team.replace('14', 'Old Trafford, Manchester')
        team = team.replace('15', 'St. Jame\'s Park, Newcastle')
        team = team.replace('16', 'The City Ground, Nottingham')
        team = team.replace('17', 'St. Mary\'s Stadium, Southampton ')
        team = team.replace('18', 'Tottenham Hotspur Stadium, London')
        team = team.replace('19', 'London Stadium, London')
        team = team.replace('20', 'Molineux Stadium, Wolverhampton')

    return team

#get the twitter handle for a team
def get_twitter_handle(team_code): 
    team = str(team_code)
    if len(team)==1:
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

#get a teams name when you give it the teams code
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


#getting the badge of each team

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


# for all the fixtures this gw, get all the scores, players who scored, bonus points if available, etc.


def get_livescore():

    

    link2 = 'https://fantasy.premierleague.com/api/fixtures/'
    response = requests.get(link2)

    # Convert JSON data to a python object
    data = json.loads(response.text)

    #list of games in this game week
    gw = []


    #Distinct days in the game week {Friday, saturday, sunday etc}
    distinct_days = []
    #Distict date like 08 october 2022
    distinct_date = []

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



        temp_time = pd.Timestamp(time_2[0])
        hour = str(temp_time.hour+1)
        minutes = str(temp_time.minute)
        if minutes== '0':
            minutes = '00'
        
        full_time = hour +':'+minutes

        day_name = pd.Timestamp(time)
        day_name = day_name.day_name() 
        full_date = day_name + ', '+day+ ' '+ month_name + ' ' + year + ' at '+ time_2[0] +  ' UK Time'
        display_date = day+ ' '+ month_name + ' ' + year + ' at '+ time_2[0] +  ' UK Time'
        display_time = full_time +  ' UK Time'
        date_name = day_name + ', '+day+ ' '+ month_name + ' ' + year





       


        if day_name not in distinct_days :
            distinct_days.append(day_name)

        if date_name not in distinct_date :
            distinct_date.append(date_name)


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

            away_goals_string = ''
            for z in goal_scored['a']:
                away_goals_string =  get_player_name(z['element'])+' x'+str(z['value']) + ', ' + away_goals_string
            
            for z in own_goals['h']:
                away_goals_string =  get_player_name(z['element'])+' x'+str(z['value']) + '   ' + away_goals_string 

            away_assists_string = ''
            for z in assist['a']:
                away_assists_string =  get_player_name(z['element'])+' x'+str(z['value']) + ', ' + away_assists_string

            away_yellowcards_string = ''
            for z in yellow_cards['a']:
                away_yellowcards_string =  get_player_name(z['element']) + ', ' + away_yellowcards_string

            away_redcards_string = ''
            for z in red_cards['a']:
                away_redcards_string =  get_player_name(z['element']) + ', ' + away_redcards_string

            away_bonus = ''
            for z in bonus['a']:
                away_bonus = get_player_name(z['element'])+' ='+str(z['value']) + ', ' + away_bonus


            #Getting all the stats (goal scored, assist, own goal and bonus ) for home team
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

            #Getting goals and own goals for the home team
            home_goals_string = ''
            for z in goal_scored['h']:
                home_goals_string =  get_player_name(z['element'])+' x'+str(z['value']) + ', ' + home_goals_string 
            
            for z in own_goals['a']:
                home_goals_string =  '(OG) ' + get_player_name(z['element'])+' x'+str(z['value']) + ', ' + home_goals_string 

            #home_goals_string = home_goals_string.rstrip(home_goals_string[-1])

            home_assists_string = ''
            for z in assist['h']:
                home_assists_string =  get_player_name(z['element'])+' x'+str(z['value']) + ', ' + home_assists_string

            home_yellowcards_string = ''
            for z in yellow_cards['h']:
                home_yellowcards_string =  get_player_name(z['element']) + ', ' + home_yellowcards_string

            home_redcards_string = ''
            for z in red_cards['h']:
                home_redcards_string =  get_player_name(z['element']) + ', ' + home_redcards_string

            home_bonus = ''
            for z in bonus['h']:
                home_bonus = get_player_name(z['element'])+' ='+str(z['value']) + ', ' + home_bonus 


            

            twitter_handle = get_twitter_handle(gw[p]['team_h']) +get_twitter_handle(gw[p]['team_a'])
            twitter_link = 'https://twitter.com/search?q=%23'+twitter_handle

            home_stadium = get_home_stadium(gw[p]['team_h'])
        



            
        
            game_info = {
                'kick_off_time':full_date,
                'display_kick_off_time': display_date,
                'display_time': display_time,
                'started': started,
                'finished': finished ,
                'minutes': mins,
                'team_h':get_team_name(gw[p]['team_h']),
                 'team_a':get_team_name(gw[p]['team_a']),
                 'team_h_score':gw[p]['team_h_score'],
                 'team_a_score':gw[p]['team_a_score'],
                 'team_h_badge':get_team_badge(gw[p]['team_h']),
                 'team_a_badge':get_team_badge(gw[p]['team_a']),
                 'events':total_events,
                 'home_goals_string': home_goals_string[:-2],
                 'away_goals_string': away_goals_string[:-2],
                 'home_assists_string': home_assists_string[:-2],
                 'away_assists_string': away_assists_string[:-2],
                 'home_yellowcards_string': home_yellowcards_string[:-2],
                 'away_yellowcards_string': away_yellowcards_string[:-2],
                 'home_redcards_string': home_redcards_string[:-2],
                 'away_redcards_string': away_redcards_string[:-2],
                 'home_bonus': home_bonus[:-2],
                 'away_bonus': away_bonus[:-2],
                 'twitter_handle': '#'+twitter_handle,
                 'twitter_link': twitter_link,
                 'home_stadium': home_stadium

                }
        #If the game has not been played yet
        else:
            total_events = None
            mins = gw[p]['minutes'] #Current minute in the game
            finished =  gw[p]['finished'] # Has the game finished
            started = gw[p]['started'] #Has the game started

            twitter_handle = get_twitter_handle(gw[p]['team_h']) +get_twitter_handle(gw[p]['team_a'])
            twitter_link = 'https://twitter.com/search?q=%23'+twitter_handle
            home_stadium = get_home_stadium(gw[p]['team_h'])
            
            game_info = {
                'kick_off_time':full_date,
                'started': started,
                'finished': finished,
                'display_kick_off_time': display_date,
                'display_time': display_time,
                'minutes': mins,
                'team_h':get_team_name(gw[p]['team_h']),
                 'team_a':get_team_name(gw[p]['team_a']),
                 'team_h_score':gw[p]['team_h_score'],
                 'team_a_score':gw[p]['team_a_score'],
                 'team_h_badge':get_team_badge(gw[p]['team_h']),
                 'team_a_badge':get_team_badge(gw[p]['team_a']),
                 'events':total_events,
                 'twitter_handle': '#'+twitter_handle,
                 'twitter_link': twitter_link,
                 'home_stadium': home_stadium

                }
        total_info.append(game_info)
    

    #print(new_list) 
    info = {
        'game_week': current_gw,
        'days': distinct_days,
        'date': distinct_date,
        'Game_results': total_info

    }
    
    return info
