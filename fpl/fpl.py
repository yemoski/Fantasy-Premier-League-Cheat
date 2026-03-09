import requests
import json
import numpy as np
import pandas as pd
from datetime import datetime
from pprint import pprint
from collections import Counter
import fixture_difficulty as fd


##testing
# Make a get request to get the latest player data from the FPL API
link = "https://fantasy.premierleague.com/api/bootstrap-static/"
response = requests.get(link)

# Convert JSON data to a python object
data = json.loads(response.text)
postponed_games = fd.get_postponed_games()

all_players = []
manager_list = []

for i in data['elements']:
    name = i['second_name']
    team = str(i['team'])
    webname = i['web_name']
    team_shirt = str(i['team'])
    ict_index = float(i['ict_index'])
    form_ict_index = float(i['form']) * float(i['ict_index'])
    photo = i['photo']
    total_points = i['total_points']
    transfers_in = i['transfers_in']
    status = i['status']
    now_cost = i['now_cost']/10
    news = i['news']
    in_dreamteam = i['in_dreamteam']
    news_added = i['news_added']
    transfers_in_event = i['transfers_in_event']
    transfers_out_event = i['transfers_out_event']
    transfers_in_event = int(transfers_in_event)
    #transfers_in_event = '{:,}'.format(int(transfers_in_event))
    #transfers_out_event = '{:,}'.format(int(transfers_out_event))
    points_per_game = i['points_per_game']
    selected_by_percent = i['selected_by_percent']
    chance_of_playing_next_round = i['chance_of_playing_next_round']
    ep_next = i['ep_next'] #expected points next game week
    cost_change_event = i['cost_change_event'] #price change for each game week

    position = str(i['element_type'])
    position = position.replace('1',"GK")
    position = position.replace('2',"DEF")
    position = position.replace('3',"MID")
    position = position.replace('4',"FOW")

    photo = photo.replace('jpg','png')

    

    if len(team)==1:
        team = team.replace('1', 'Arsenal')
        team = team.replace('2', 'Aston Villa')
        team = team.replace('3', 'Burnley')
        team = team.replace('4', 'Bournemouth')
        team = team.replace('5', 'Brentford')
        team = team.replace('6', 'Brighton')
        team = team.replace('7', 'Chelsea')
        team = team.replace('8', 'Crystal Palace')
        team = team.replace('9', 'Everton')
        team_shirt = team
        badge = team

        team_shirt = team_shirt.replace('Arsenal','https://fantasy.premierleague.com/dist/img/shirts/standard/shirt_3-66.webp')
        team_shirt = team_shirt.replace('Aston Villa','https://fantasy.premierleague.com/dist/img/shirts/standard/shirt_7-66.webp')
        team_shirt = team_shirt.replace('Bournemouth','https://fantasy.premierleague.com/dist/img/shirts/standard/shirt_91-66.webp')
        team_shirt = team_shirt.replace('Brentford','https://fantasy.premierleague.com/dist/img/shirts/standard/shirt_94-66.webp')
        team_shirt = team_shirt.replace('Brighton','https://fantasy.premierleague.com/dist/img/shirts/standard/shirt_36-66.webp')
        team_shirt = team_shirt.replace('Burnley','https://fantasy.premierleague.com/dist/img/shirts/standard/shirt_90-66.webp')       
        team_shirt = team_shirt.replace('Chelsea','https://fantasy.premierleague.com/dist/img/shirts/standard/shirt_8-66.webp')
        team_shirt = team_shirt.replace('Crystal Palace','https://fantasy.premierleague.com/dist/img/shirts/standard/shirt_31-66.webp')
        team_shirt = team_shirt.replace('Everton','https://fantasy.premierleague.com/dist/img/shirts/standard/shirt_11-66.webp')

        badge = badge.replace('Arsenal','https://resources.premierleague.com/premierleague/badges/t3.svg')
        badge = badge.replace('Aston Villa','https://resources.premierleague.com/premierleague/badges/t7.svg')
        badge = badge.replace('Bournemouth','https://resources.premierleague.com/premierleague/badges/t91.svg')
        badge = badge.replace('Brentford','https://resources.premierleague.com/premierleague/badges/t94.svg')
        badge = badge.replace('Brighton','https://resources.premierleague.com/premierleague/badges/t36.svg')
        badge = badge.replace('Burnley','https://resources.premierleague.com/premierleague/badges/t90.svg')
        badge = badge.replace('Chelsea','https://resources.premierleague.com/premierleague/badges/t8.svg')
        badge = badge.replace('Crystal Palace','https://resources.premierleague.com/premierleague/badges/t31.svg')
        badge = badge.replace('Everton','https://resources.premierleague.com/premierleague/badges/t11.svg')
    elif len(team)==2:
        team = team.replace('10', 'Fulham')
        team = team.replace('11', 'Leeds')
        team = team.replace('12', 'Liverpool')
        team = team.replace('13', 'Man city')
        team = team.replace('14', 'Man United')
        team = team.replace('15', 'Newcastle')
        team = team.replace('16', 'Nottingham Forest')
        team = team.replace('17', 'Sunderland')
        team = team.replace('18', 'Tottenham')
        team = team.replace('19', 'Westham')
        team = team.replace('20', 'Wolves')
        team_shirt = team
        team_shirt = team_shirt.replace('Fulham','https://fantasy.premierleague.com/dist/img/shirts/standard/shirt_54-66.webp')
        team_shirt = team_shirt.replace('Liverpool','https://fantasy.premierleague.com/dist/img/shirts/standard/shirt_14-66.webp')
        team_shirt = team_shirt.replace('Leeds','https://fantasy.premierleague.com/dist/img/shirts/standard/shirt_2-66.webp')
        team_shirt = team_shirt.replace('Man city','https://fantasy.premierleague.com/dist/img/shirts/standard/shirt_43-66.webp')
        team_shirt = team_shirt.replace('Man United','https://fantasy.premierleague.com/dist/img/shirts/standard/shirt_1-66.webp')
        team_shirt = team_shirt.replace('Newcastle','https://fantasy.premierleague.com/dist/img/shirts/standard/shirt_4-66.webp')
        team_shirt = team_shirt.replace('Nottingham Forest','https://fantasy.premierleague.com/dist/img/shirts/standard/shirt_17-66.webp')
        team_shirt = team_shirt.replace('Sunderland','https://fantasy.premierleague.com/dist/img/shirts/standard/shirt_56-66.webp')
        team_shirt = team_shirt.replace('Tottenham','https://fantasy.premierleague.com/dist/img/shirts/standard/shirt_6-66.webp')
        team_shirt = team_shirt.replace('Westham','https://fantasy.premierleague.com/dist/img/shirts/standard/shirt_21-66.webp')
        team_shirt = team_shirt.replace('Wolves','https://fantasy.premierleague.com/dist/img/shirts/standard/shirt_39-66.webp')

        badge = badge.replace('Fulham','https://resources.premierleague.com/premierleague/badges/t54.svg')
        badge = badge.replace('Liverpool','https://resources.premierleague.com/premierleague/badges/t14.svg')
        badge = badge.replace('Leeds','https://resources.premierleague.com/premierleague/badges/t2.svg')
        badge = badge.replace('Man city','https://resources.premierleague.com/premierleague/badges/t43.svg')
        badge = badge.replace('Man United','https://resources.premierleague.com/premierleague/badges/t1.svg')
        badge = badge.replace('Newcastle','https://resources.premierleague.com/premierleague/badges/t4.svg')
        badge = badge.replace('Nottingham Forest','https://resources.premierleague.com/premierleague/badges/t17.svg')
        badge = badge.replace('Sunderland','https://resources.premierleague.com/premierleague/badges/t56.svg')
        badge = badge.replace('Tottenham','https://resources.premierleague.com/premierleague/badges/t6.svg')
        badge = badge.replace('Westham','https://resources.premierleague.com/premierleague/badges/t21.svg')
        badge = badge.replace('Wolves','https://resources.premierleague.com/premierleague/badges/t39.svg')
    
    
    #for game week 8 alone the teams in the above array have their games postponed
    if team in postponed_games:
        postponed = 'Yes'
    else:
        postponed = 'No'

    stats = [name,form_ict_index,photo,total_points,transfers_in,status,team,now_cost,position,team_shirt,postponed,news, news_added, transfers_in_event,transfers_out_event,selected_by_percent,points_per_game, in_dreamteam,cost_change_event, webname, ict_index]

    # only add players not managers
    if position != '5':
        all_players.append(stats)
    
    
    # Ensure it's a manager
    if i.get("element_type") == 5: 
        manager_data =  {
        "first_name": i.get("first_name"),
        "second_name": i.get("second_name"),
        "element_type": i.get("element_type"),
        "mng_win": i.get("mng_win", 0),
        "mng_draw": i.get("mng_draw", 0),
        "mng_loss": i.get("mng_loss", 0),
        "mng_underdog_win": i.get("mng_underdog_win", 0),
        "influence_rank": i.get("influence_rank", 1000),
        "creativity_rank": i.get("creativity_rank", 1000),
        "threat_rank": i.get("threat_rank", 1000),
        "ict_index_rank": i.get("ict_index_rank", 1000),
        "now_cost": i.get("now_cost")/10,
        "points_per_game": float(i.get("points_per_game", "0.0")),
        "selected_by_percent": float(i.get("selected_by_percent", "0.0")),
        "transfers_in": i.get("transfers_in", 0),
        "transfers_out": i.get("transfers_out", 0)
        }
        manager_list.append(manager_data)


all_players = np.array(all_players)
dataset = pd.DataFrame({
    'name': all_players[:, 0],
    'form_ict_index': all_players[:,1].astype(float),
    'photo': all_players[:, 2],
    'total_points': all_players[:,3],
    'transfer_in': all_players[:,4],
    'status': all_players[:,5],
    'team': all_players[:,6],
    'now_cost': all_players[:,7].astype(float),
    'position': all_players[:,8],
    'team_shirt': all_players[:,9],
    'postponed': all_players[:,10],
    'news': all_players[:, 11],
    'news_added': all_players[:, 12],
    'transfer_in_event': all_players[:, 13],
    'transfer_out_event': all_players[:, 14],
    'selected_by_percent': all_players[:, 15].astype(float),
    'points_per_game': all_players[:,16],
    'in_dreamteam': all_players[:,17],
    'cost_change_event': all_players[:,18],
    'webname' : all_players[:,19],
    'ict_index': all_players[:,20]
})


dataset = dataset.sort_values(by=['form_ict_index'], ascending=False)


def calculate_manager_score(manager):
    performance_score = (manager["mng_win"] * 3 + manager["mng_draw"]) / max(1, (manager["mng_win"] + manager["mng_draw"] + manager["mng_loss"])) * 10
    tactical_strength = (1000 - manager["influence_rank"] + 1000 - manager["creativity_rank"] + 1000 - manager["ict_index_rank"]) / 3000 * 10
    cost_effectiveness = (manager["points_per_game"] / max(1, manager["now_cost"])) * 100
    popularity_score = (float(manager["selected_by_percent"]) + (manager["transfers_in"] - manager["transfers_out"]) / 1000)

    # Weighted Score
    weighted_score = (0.4 * performance_score) + (0.3 * tactical_strength) + (0.2 * cost_effectiveness) + (0.1 * popularity_score)
    
    return pd.Series([performance_score, tactical_strength, cost_effectiveness, popularity_score, weighted_score])



""" commenting this about because apparently we dont have managers anymore
def get_managers():
    #converting the list to a pandas dataframe 
    manager_list_df = pd.DataFrame(manager_list)
    #pprint("This is the list of managers")
    #pprint(manager_list_df)

    # Apply the function to each row and create new columns
    manager_list_df[["Performance_Score", "Tactical_Strength", "Cost_Effectiveness", "Popularity_Score", "Weighted_Score"]] = manager_list_df.apply(calculate_manager_score, axis=1)

    # Sort by Weighted Score
    manager_list_df = manager_list_df.sort_values(by="Weighted_Score", ascending=False)

    return manager_list_df
"""

def get_current_time():
    now = datetime.today()

    current_time = now.strftime('%Y-%m-%d %H:%M:%S')
    time = current_time
    time = datetime.strptime(time,'%Y-%m-%d %H:%M:%S')
    month_name = str(time.strftime('%B'))
    year = str(time.strftime('%Y'))
    day = str(time.strftime('%d'))
    time2 = time.strftime('%H:%M:%S')
    day_name = pd.Timestamp(time)
    day_name = day_name.day_name() 
    full_date = day_name + ', '+day+ ' '+ month_name + ' ' + year

    return full_date


def get_percentage_of_manager(x):
    #GETTING GAME WEEK DEADLINE AND CHIP PLAYS
    # Make a get request to get the latest player data from the FPL API
    link = "https://fantasy.premierleague.com/api/bootstrap-static/"
    response = requests.get(link)

    # Convert JSON data to a python object
    data = json.loads(response.text)
    total = int(data['total_players'])
    percentage = int((x/total)*100)


    if percentage <=1:
        percentage = 1


    return percentage


# get a list of players not owned by a lot of people and are injury free
def get_differentials():
    players_list = []
    counter = 0

    for index,row in dataset.iterrows():
        if counter ==20 :
            break
        elif  row['selected_by_percent']<15.0 and row['status']=='a' and row['postponed']!='Yes':
                player_dict = {
                'name': row['name'],
                'webname' : row['webname'],
                'team': row['team'],
                'photo': row['photo'],
                'position': row['position'],
                'points_per_game': row['points_per_game'],
                'price': row['now_cost'],
                'selected': row['selected_by_percent'],
                }
                players_list.append(player_dict)
                counter = counter +1

    df = pd.DataFrame(players_list)


    return df


# get the most transferred in players
def get_most_transferred_in():
    players_list = []
    datasets = dataset.sort_values(by=['transfer_in_event'], ascending=False)

    counter = 0
    for index,row in datasets.iterrows():
        if counter ==15:
            break

        player_dict = {
        'name': row['name'],
        'webname' : row['webname'],
        'team': row['team'],
        'position': row['position'],
        'photo': row['photo'],
        'points_per_game': row['points_per_game'],
        'price': row['now_cost'],
        'percent': row['selected_by_percent'],
        'fake_count': row['transfer_in_event'],
        'count': '{:,}'.format(int(row['transfer_in_event'])),
        'postponed': row['postponed']
        }
        players_list.append(player_dict)
        counter = counter +1

    df = pd.DataFrame(players_list)
    df = df.sort_values(by=['fake_count'], ascending=False)
    return df

# get the most transferred out players
def get_most_transferred_out():
    players_list = []
    datasets = dataset.sort_values(by=['transfer_out_event'], ascending=False)

    counter = 0
    for index,row in datasets.iterrows():
        if counter ==15:
            break

        player_dict = {
        'name': row['name'],
        'team': row['team'],
        'webname' : row['webname'],
        'photo': row['photo'],
        'position': row['position'],
        'points_per_game': row['points_per_game'],
        'price': row['now_cost'],
        'percent': row['selected_by_percent'],
        'fake_count': row['transfer_out_event'],
        'count': '{:,}'.format(int(row['transfer_out_event'])),
        'postponed': row['postponed']
        }
        players_list.append(player_dict)
        counter = counter +1

    df = pd.DataFrame(players_list)
    df = df.sort_values(by=['fake_count'], ascending=False)
    return df

def get_most_selected():
    players_list = []
    datasets = dataset.sort_values(by=['selected_by_percent'], ascending=False)

    counter = 0
    for index,row in datasets.iterrows():
        if counter ==15:
            break

        player_dict = {
        'name': row['name'],
        'webname' : row['webname'],
        'team': row['team'],
        'photo': row['photo'],
        'position': row['position'],
        'points_per_game': row['points_per_game'],
        'price': row['now_cost'],
        'percent': row['selected_by_percent']
        }
        players_list.append(player_dict)
        counter = counter +1

    df = pd.DataFrame(players_list)
    return df



# get all the latest injury and price changes news for all players

def get_news():
    #dataset = dataset.sort_values(by=['name'], ascending=False)
    news_list = []
    price_change_list = []

    now = datetime.today()

    current_time = now.strftime('%Y-%m-%d')
    current_time = datetime.strptime(current_time,'%Y-%m-%d')

    month_name2 = str(current_time.strftime('%B'))
    year2 = str(current_time.strftime('%Y'))
    day2 = str(current_time.strftime('%d'))

    day_name2 = pd.Timestamp(current_time)
    day_name2 = day_name2.day_name() 
    full_date2 = day_name2 + ', '+day2+ ' '+ month_name2 + ' ' + year2

    for index,row in dataset.iterrows():
        if row['news']!='' and 'loan' not in row['news'] and 'Transferred' not in row['news'] and 'left' not in row['news']:

            time = row['news_added']
            time = time.split('T',1)
            time = time[0]
            time = datetime.strptime(time,'%Y-%m-%d')
            month_name = str(time.strftime('%B'))
            year = str(time.strftime('%Y'))
            day = str(time.strftime('%d'))

            day_name = pd.Timestamp(time)
            day_name = day_name.day_name() 
            full_date = day_name + ', '+day+ ' '+ month_name + ' ' + year
           
            
            #print(type(time))
            #time = time.strptime("%b %d %Y %H:%M:%S")
            news = {'time': full_date,
                'sorting_time': time,
            'news': row['news'],
            'name': row['webname'],
            'photo': row['photo'],
            'team': row['team']}
        

            news_list.append(news)
        if row['cost_change_event']!=0:
            
            if row['cost_change_event']==1: 
                news = {
                'time' : full_date2,
                 'sorting_time': current_time,
                'news': str(row['now_cost']),
                'name': row['webname'],
                'photo': row['photo'],
                'team': row['team'],
                'price_change': 'risen'
                }
            else:
                news = {
                'time' : full_date2,
                 'sorting_time': current_time,
                'news': str(row['now_cost']),
                'name': row['webname'],
                'photo': row['photo'],
                'team': row['team'],
                'price_change': 'fallen'
                }

            news_list.append(news)
    news_df = pd.DataFrame(news_list)
    news_df = news_df.sort_values(by=['sorting_time'], ascending=False)
    return news_df


#Picks a dream team
def get_dream_team():
    dream = {'GK':[],
            'DEF':[],
            'MID':[],
            'FOW':[],
            'team_value':[],
            'ict_form':[],
            'captain': None
            }

    GK = 0
    DEF = 0
    MID = 0
    FOW = 0
    teams = []
    ict_form = 0
    captain =  {'name':None,
            'ict_form_index': 0}
    for index,row in dataset.iterrows():
            if row['position']=='FOW' and row['in_dreamteam']==True:
                if row['form_ict_index'] >= captain['ict_form_index']:
                    captain['ict_form_index'] = row['form_ict_index']
                    captain['name'] = row['name']

                new_row = {'name': row['name'],
                            'now_cost': row['now_cost'],
                            'transfer_in_event':'{:,}'.format(int(row['transfer_in_event'])),
                            'transfer_out_event': '{:,}'.format(int(row['transfer_out_event'])),
                            'selected_by_percent': row['selected_by_percent'],
                            'in_dreamteam': row['in_dreamteam'],
                            'points_per_game': row['points_per_game'],
                            'photo': row['photo'],
                            'team_shirt': row['team_shirt'],
                            'team': row['team']}
                dream['FOW'].append(new_row)
                teams.append(row['team'])

                
            if row['position']=='MID'  and row['in_dreamteam']==True:
                if row['form_ict_index'] >= captain['ict_form_index']:
                    captain['ict_form_index'] = row['form_ict_index']
                    captain['name'] = row['name']
                new_row = {'name': row['name'],
                            'now_cost': row['now_cost'],
                            'transfer_in_event':'{:,}'.format(int(row['transfer_in_event'])),
                            'transfer_out_event': '{:,}'.format(int(row['transfer_out_event'])),
                            'selected_by_percent': row['selected_by_percent'],
                            'in_dreamteam': row['in_dreamteam'],
                            'points_per_game': row['points_per_game'],
                            'photo': row['photo'],
                            'team_shirt': row['team_shirt'],
                            'team': row['team']}
                dream['MID'].append(new_row)
                teams.append(row['team'])
                
                
            if row['position']=='GK'  and row['in_dreamteam']==True:
                if row['form_ict_index'] >= captain['ict_form_index']:
                    captain['ict_form_index'] = row['form_ict_index']
                    captain['name'] = row['name']
                new_row = {'name': row['name'],
                            'now_cost': row['now_cost'],
                            'transfer_in_event':'{:,}'.format(int(row['transfer_in_event'])),
                            'transfer_out_event': '{:,}'.format(int(row['transfer_out_event'])),
                            'selected_by_percent': row['selected_by_percent'],
                            'in_dreamteam': row['in_dreamteam'],
                            'points_per_game': row['points_per_game'],
                            'photo': row['photo'],
                            'team_shirt': row['team_shirt'],
                            'team': row['team']}
                dream['GK'].append(new_row)
                
                teams.append(row['team'])
                
            if row['position']=='DEF'  and row['in_dreamteam']==True:
                if row['form_ict_index'] >= captain['ict_form_index']:
                    captain['ict_form_index'] = row['form_ict_index']
                    captain['name'] = row['name']
                new_row = {'name': row['name'],
                            'now_cost': row['now_cost'],
                            'transfer_in_event':'{:,}'.format(int(row['transfer_in_event'])),
                            'transfer_out_event': '{:,}'.format(int(row['transfer_out_event'])),
                            'selected_by_percent': row['selected_by_percent'],
                            'in_dreamteam': row['in_dreamteam'],
                            'points_per_game': row['points_per_game'],
                            'photo': row['photo'],
                            'team_shirt': row['team_shirt'],
                            'team': row['team']}
                dream['DEF'].append(new_row)
            
                teams.append(row['team'])
              
    
    dream['captain'] = captain
    return dream



def add_ranking_score(df, team_fix, mode='long'):
    # team_fix: dict of {team_name: difficulty_score}
    # 1. Team-level fixture score (lower = easier)
    df['team_fixture'] = df['team'].map(team_fix).fillna(5.0)   # worst case

    # 2. form = form * ict_index (already computed at import)
    df['form'] = df['form_ict_index'].astype(float)

    # 3. Normalise to 0-1
    col_min, col_max = df['form'].min(), df['form'].max()
    df['norm_form'] = (df['form'] - col_min) / (col_max - col_min) if col_max > col_min else 0.0

    # 4. Fixture ease = 5 - difficulty (higher = easier)
    df['fixture_ease'] = 5.0 - df['team_fixture']
    fix_min, fix_max = df['fixture_ease'].min(), df['fixture_ease'].max()
    df['norm_fixture'] = (df['fixture_ease'] - fix_min) / (fix_max - fix_min) if fix_max > fix_min else 0.0

    # 5. Weighted composite score
    #    Short term: form dominates, fixture is a small tiebreaker
    #    Long term:  fixture run deserves more weight over 6 games
    if mode == 'short':
        df['ranking_score'] = 0.85 * df['norm_form'] + 0.15 * df['norm_fixture']
    else:
        df['ranking_score'] = 0.65 * df['norm_form'] + 0.35 * df['norm_fixture']

    return df

def build_formation(df, formation="442", budget=100.0, max_per_team=3):
    # Normalize formation string (accepts "442" or "4-4-2")
    if "-" not in formation and len(formation) == 3:
        formation = "-".join(list(formation))  # "442" → "4-4-2"
    
    try:
        gk_str, def_str, mid_str, fwd_str = formation.replace('-', ' ').split()
        req = {
            'GK':  int(gk_str),
            'DEF': int(def_str),
            'MID': int(mid_str),
            'FOW': int(fwd_str)
        }
    except Exception:
        raise ValueError("formation must be like '1-3-5-2' or '442'")

    # ---- Sort by our new ranking score ----------------------------------
    sorted_df = df.sort_values('ranking_score', ascending=False).reset_index(drop=True)

    # ---- State -----------------------------------------------------------
    squad = {pos: [] for pos in req}
    remaining = budget
    team_cnt = Counter()
    total_form = 0.0
    captain = {'webname': None, 'form': 0.0}

    # ---- Helper ----------------------------------------------------------
    def add_player(row, pos):
        nonlocal remaining, total_form, captain
        player = {
            'webname': row['webname'],
            'now_cost': row['now_cost'],
            'transfer_in_event': '{:,}'.format(int(row['transfer_in_event'])),
            'transfer_out_event': '{:,}'.format(int(row['transfer_out_event'])),
            'selected_by_percent': row['selected_by_percent'],
            'in_dreamteam': row['in_dreamteam'],
            'points_per_game': row['points_per_game'],
            'photo': row['photo'],
            'team_shirt': row['team_shirt'],
            'team': row['team']
        }
        squad[pos].append(player)
        remaining -= row['now_cost']
        total_form += row['form']
        team_cnt[row['team']] += 1

        # Captain = highest raw form in squad
        if row['form'] > captain['form']:
            captain['webname'] = row['webname']
            captain['form'] = row['form']

    # ---- Main loop -------------------------------------------------------
    needed = {pos: req[pos] for pos in req}
    for _, row in sorted_df.iterrows():
        if remaining < row['now_cost']:
            continue
        if row['status'] != 'a' or row['postponed'] == 'Yes':
            continue
        if team_cnt[row['team']] >= max_per_team:
            continue

        pos = row['position']
        if needed.get(pos, 0) > 0:
            add_player(row, pos)
            needed[pos] -= 1

        # Stop when squad is full
        if all(v == 0 for v in needed.values()):
            break

    # ---- Finalise --------------------------------------------------------
    squad['team_value'] = budget - remaining
    squad['ict_form'] = total_form
    squad['captain'] = captain

    return squad

fixtures_data = fd.get_fixtures()

# Maps raw FPL team ID (1-20) → whether that team has a fixture next GW
team_id_to_has_fixture = {i + 1: d['has_next_fixture'] for i, d in enumerate(fixtures_data)}

team_fix_short = {d['team']: d['next_game_difficulty'] for d in fixtures_data}

def _avg_difficulty(next_7_list, n=6):
    slice_ = next_7_list[:n]
    diffs = [g['difficulty'] if isinstance(g, dict) else 5 for g in slice_]
    return round(sum(diffs) / len(diffs), 2) if diffs else 5.0

team_fix_long = {d['team']: _avg_difficulty(d['next_7']) for d in fixtures_data}

dataset_short = add_ranking_score(dataset.copy(), team_fix_short, mode='short')
dataset_long  = add_ranking_score(dataset.copy(), team_fix_long,  mode='long')

_datasets = {'short': dataset_short, 'long': dataset_long}

def get_442(mode='long'):
    return build_formation(_datasets.get(mode, dataset_long), "1-4-4-2")

def get_532(mode='long'):
    return build_formation(_datasets.get(mode, dataset_long), "1-5-3-2")

def get_451(mode='long'):
    return build_formation(_datasets.get(mode, dataset_long), "1-5-4-1")

def get_433(mode='long'):
    return build_formation(_datasets.get(mode, dataset_long), "1-4-3-3")

def get_352(mode='long'):
    return build_formation(_datasets.get(mode, dataset_long), "1-3-5-2")

def get_343(mode='long'):
    return build_formation(_datasets.get(mode, dataset_long), "1-3-4-3")

def get_search_dataset():
    result = []
    for i in data['elements']:
        pos = str(i['element_type'])
        pos = pos.replace('1', 'GK').replace('2', 'DEF').replace('3', 'MID').replace('4', 'FOW')
        if pos == '5':
            continue

        team = str(i['team'])
        if len(team) == 1:
            team = (team.replace('1', 'Arsenal').replace('2', 'Aston Villa')
                        .replace('3', 'Burnley').replace('4', 'Bournemouth')
                        .replace('5', 'Brentford').replace('6', 'Brighton')
                        .replace('7', 'Chelsea').replace('8', 'Crystal Palace')
                        .replace('9', 'Everton'))
        elif len(team) == 2:
            team = (team.replace('10', 'Fulham').replace('11', 'Leeds')
                        .replace('12', 'Liverpool').replace('13', 'Man City')
                        .replace('14', 'Man United').replace('15', 'Newcastle')
                        .replace('16', 'Nottm Forest').replace('17', 'Sunderland')
                        .replace('18', 'Tottenham').replace('19', 'West Ham')
                        .replace('20', 'Wolves'))

        photo = i['photo'].replace('jpg', 'png')
        form_ict = round(float(i['form']) * float(i['ict_index']), 2)

        result.append({
            'webname': i['web_name'],
            'team': team,
            'position': pos,
            'status': i['status'],
            'photo': photo,
            'cost': i['now_cost'] / 10,
            'points_per_game': float(i['points_per_game']),
            'ict_index': float(i['ict_index']),
            'form_ict_index': form_ict,
            'goals_scored': i['goals_scored'],
            'assists': i['assists'],
            'expected_goals': float(i['expected_goals']),
            'expected_assists': float(i['expected_assists']),
            'has_next_fixture': team_id_to_has_fixture.get(i['team'], True),
        })
    return result