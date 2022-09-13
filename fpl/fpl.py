import requests
import json
import numpy as np
import pandas as pd
import datetime


# Make a get request to get the latest player data from the FPL API
link = "https://fantasy.premierleague.com/api/bootstrap-static/"
response = requests.get(link)

# Convert JSON data to a python object
data = json.loads(response.text)

#print(data)
all_players = []
for i in data['elements']:
    name = i['first_name'] + " " + i['second_name']
    team = str(i['team'])
    team_shirt = str(i['team'])
    form_ict_index = float(i['form']) * float(i['ict_index'])
    photo = i['photo']
    total_points = i['total_points']
    transfers_in = i['transfers_in']
    status = i['status']
    now_cost = i['now_cost']/10
    position = str(i['element_type'])
    position = position.replace('1',"GK")
    position = position.replace('2',"DEF")
    position = position.replace('3',"MID")
    position = position.replace('4',"FOW")

    photo = photo.replace('jpg','png')
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
        team_shirt = team

        team_shirt = team_shirt.replace('Arsenal','https://fantasy.premierleague.com/dist/img/shirts/standard/shirt_3-66.webp')
        team_shirt = team_shirt.replace('Aston Villa','https://fantasy.premierleague.com/dist/img/shirts/standard/shirt_7-66.webp')
        team_shirt = team_shirt.replace('Bournemouth','https://fantasy.premierleague.com/dist/img/shirts/standard/shirt_91-66.webp')
        team_shirt = team_shirt.replace('Brentford','https://fantasy.premierleague.com/dist/img/shirts/standard/shirt_94-66.webp')
        team_shirt = team_shirt.replace('Brighton','https://fantasy.premierleague.com/dist/img/shirts/standard/shirt_36-66.webp')
        team_shirt = team_shirt.replace('Chelsea','https://fantasy.premierleague.com/dist/img/shirts/standard/shirt_8-66.webp')
        team_shirt = team_shirt.replace('Crystal Palace','https://fantasy.premierleague.com/dist/img/shirts/standard/shirt_31-66.webp')
        team_shirt = team_shirt.replace('Everton','https://fantasy.premierleague.com/dist/img/shirts/standard/shirt_11-66.webp')
        team_shirt = team_shirt.replace('Fulham','https://fantasy.premierleague.com/dist/img/shirts/standard/shirt_54-66.webp')
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
        team_shirt = team
        team_shirt = team_shirt.replace('Leicester','https://fantasy.premierleague.com/dist/img/shirts/standard/shirt_13-66.webp')
        team_shirt = team_shirt.replace('Leeds','https://fantasy.premierleague.com/dist/img/shirts/standard/shirt_2-66.webp')
        team_shirt = team_shirt.replace('Liverpool','https://fantasy.premierleague.com/dist/img/shirts/standard/shirt_14-66.webp')
        team_shirt = team_shirt.replace('Man city','https://fantasy.premierleague.com/dist/img/shirts/standard/shirt_43-66.webp')
        team_shirt = team_shirt.replace('Man United','https://fantasy.premierleague.com/dist/img/shirts/standard/shirt_1-66.webp')
        team_shirt = team_shirt.replace('Newcastle','https://fantasy.premierleague.com/dist/img/shirts/standard/shirt_4-66.webp')
        team_shirt = team_shirt.replace('Nottingham Forest','https://fantasy.premierleague.com/dist/img/shirts/standard/shirt_17-66.webp')
        team_shirt = team_shirt.replace('Southampton','https://fantasy.premierleague.com/dist/img/shirts/standard/shirt_20-66.webp')
        team_shirt = team_shirt.replace('Tottenham','https://fantasy.premierleague.com/dist/img/shirts/standard/shirt_6-66.webp')
        team_shirt = team_shirt.replace('Westham','https://fantasy.premierleague.com/dist/img/shirts/standard/shirt_21-66.webp')
        team_shirt = team_shirt.replace('Wolves','https://fantasy.premierleague.com/dist/img/shirts/standard/shirt_39-66.webp')


    postponed_games = ['Man United','Leeds', 'Crystal Palace', 'Brighton', 'Chelsea','Liverpool']
    #for game week 8 alone the teams in the above array have their games postponed
    if team in postponed_games:
        postponed = 'Yes'
    else:
        postponed = 'No'

    stats = [name,form_ict_index,photo,total_points,transfers_in,status,team,now_cost,position,team_shirt,postponed]
    all_players.append(stats)


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
    'postponed': all_players[:,10]


})

dataset = dataset.sort_values(by=['form_ict_index'], ascending=False)
#dataset.to_csv(index=False, path_or_buf='data.csv')


def get_442():


    f442 = {'GK':[],
            'DEF':[],
            'MID':[],
            'FOW':[],
            'team_value':[],
            'ict_form':[],
            'captain': None
            }

    budget = 100
    GK = 0
    DEF = 0
    MID = 0
    FOW = 0
    teams = []
    ict_form = 0
    captain =  {'name':None,
            'ict_form_index': 0}
    for index,row in dataset.iterrows():
        if teams.count(row['team']) < 3 and row['postponed']=='No':
            if row['position']=='FOW' and FOW<=1 and row['status']=='a' and budget>row['now_cost']:
                if row['form_ict_index'] >= captain['ict_form_index']:
                    captain['ict_form_index'] = row['form_ict_index']
                    captain['name'] = row['name']

                new_row = {'name': row['name'],
                            'now_cost': row['now_cost'],
                            'photo': row['photo'],
                            'team_shirt': row['team_shirt'],
                            'team': row['team']}
                f442['FOW'].append(new_row)
                budget -=row['now_cost']
                ict_form += row['form_ict_index']
                
                teams.append(row['team'])

                FOW = FOW +1
            if row['position']=='MID' and MID<=3 and row['status']=='a' and budget>row['now_cost']:
                if row['form_ict_index'] >= captain['ict_form_index']:
                    captain['ict_form_index'] = row['form_ict_index']
                    captain['name'] = row['name']
                new_row = {'name': row['name'],
                            'now_cost': row['now_cost'],
                            'photo': row['photo'],
                            'team_shirt': row['team_shirt'],
                            'team': row['team']}
                f442['MID'].append(new_row)
                budget -=row['now_cost']
                teams.append(row['team'])
                ict_form += row['form_ict_index']
                MID = MID +1
            if row['position']=='GK' and GK<1 and row['status']=='a' and budget>row['now_cost']:
                if row['form_ict_index'] >= captain['ict_form_index']:
                    captain['ict_form_index'] = row['form_ict_index']
                    captain['name'] = row['name']
                new_row = {'name': row['name'],
                            'now_cost': row['now_cost'],
                            'photo': row['photo'],
                            'team_shirt': row['team_shirt'],
                            'team': row['team']}
                f442['GK'].append(new_row)
                budget -=row['now_cost']
                ict_form += row['form_ict_index']
                teams.append(row['team'])
                GK = GK +1
            if row['position']=='DEF' and DEF<=3 and row['status']=='a' and budget>row['now_cost']:
                if row['form_ict_index'] >= captain['ict_form_index']:
                    captain['ict_form_index'] = row['form_ict_index']
                    captain['name'] = row['name']
                new_row = {'name': row['name'],
                            'now_cost': row['now_cost'],
                            'photo': row['photo'],
                            'team_shirt': row['team_shirt'],
                            'team': row['team']}
                f442['DEF'].append(new_row)
                budget -=row['now_cost']
                ict_form += row['form_ict_index']
                teams.append(row['team'])
                DEF = DEF +1
    f442['ict_form'] = ict_form
    f442['team_value'] = 100-budget
    f442['captain'] = captain
    return f442

def get_532():
    f532 = {'GK':[],
            'DEF':[],
            'MID':[],
            'FOW':[],
            'team_value':[],
            'ict_form':[],
            'captain':None
            }
    budget = 100
    GK = 0
    DEF = 0
    MID = 0
    FOW = 0
    teams = []
    ict_form = 0
    captain =  {'name':None,
            'ict_form_index': 0}
    for index,row in dataset.iterrows():
        if teams.count(row['team']) < 3 and row['postponed']=='No':
            if row['position']=='FOW' and FOW<=1 and row['status']=='a' and budget>row['now_cost']:
                if row['form_ict_index'] >= captain['ict_form_index']:
                    captain['ict_form_index'] = row['form_ict_index']
                    captain['name'] = row['name']
                new_row = {'name': row['name'],
                            'now_cost': row['now_cost'],
                            'photo': row['photo'],
                            'team_shirt': row['team_shirt'],
                            'team': row['team']}
                f532['FOW'].append(new_row)
                budget -=row['now_cost']
                teams.append(row['team'])
                ict_form += row['form_ict_index']
                FOW = FOW +1
            if row['position']=='MID' and MID<=2 and row['status']=='a' and budget>row['now_cost']:
                if row['form_ict_index'] >= captain['ict_form_index']:
                    captain['ict_form_index'] = row['form_ict_index']
                    captain['name'] = row['name']
                new_row = {'name': row['name'],
                            'now_cost': row['now_cost'],
                            'photo': row['photo'],
                            'team_shirt': row['team_shirt'],
                            'team': row['team']}
                f532['MID'].append(new_row)
                budget -=row['now_cost']
                teams.append(row['team'])
                ict_form += row['form_ict_index']
                MID = MID +1
            if row['position']=='GK' and GK<1 and row['status']=='a' and budget>row['now_cost']:
                if row['form_ict_index'] >= captain['ict_form_index']:
                    captain['ict_form_index'] = row['form_ict_index']
                    captain['name'] = row['name']
                new_row = {'name': row['name'],
                            'now_cost': row['now_cost'],
                            'photo': row['photo'],
                            'team_shirt': row['team_shirt'],
                            'team': row['team']}
                f532['GK'].append(new_row)
                budget -=row['now_cost']
                teams.append(row['team'])
                ict_form += row['form_ict_index']
                GK = GK +1
            if row['position']=='DEF' and DEF<=4 and row['status']=='a' and budget>row['now_cost']:
                if row['form_ict_index'] >= captain['ict_form_index']:
                    captain['ict_form_index'] = row['form_ict_index']
                    captain['name'] = row['name']
                new_row = {'name': row['name'],
                            'now_cost': row['now_cost'],
                            'photo': row['photo'],
                            'team_shirt': row['team_shirt'],
                            'team': row['team']}
                f532['DEF'].append(new_row)
                budget -=row['now_cost']
                teams.append(row['team'])
                ict_form += row['form_ict_index']
                DEF = DEF +1
    f532['ict_form'] =ict_form
    f532['team_value'] =  100-budget
    f532['captain'] = captain
    return f532
 

def get_451():


    f451 = {'GK':[],
            'DEF':[],
            'MID':[],
            'FOW':[],
            'team_value':[],
            'ict_form':[],
            'captain':None
            }
    budget = 100
    GK = 0
    DEF = 0
    MID = 0
    FOW = 0
    teams = []
    ict_form = 0
    captain =  {'name':None,
            'ict_form_index': 0}
    for index,row in dataset.iterrows():
        if teams.count(row['team']) < 3 and row['postponed']=='No':
            if row['position']=='FOW' and FOW<=0 and row['status']=='a' and budget>row['now_cost']:
                if row['form_ict_index'] >= captain['ict_form_index']:
                    captain['ict_form_index'] = row['form_ict_index']
                    captain['name'] = row['name']
                new_row = {'name': row['name'],
                            'now_cost': row['now_cost'],
                            'photo': row['photo'],
                            'team_shirt': row['team_shirt'],
                            'team': row['team']}
                f451['FOW'].append(new_row)
                budget -=row['now_cost']
                teams.append(row['team'])
                ict_form += row['form_ict_index']
                FOW = FOW +1
            if row['position']=='MID' and MID<=4 and row['status']=='a' and budget>row['now_cost']:
                if row['form_ict_index'] >= captain['ict_form_index']:
                    captain['ict_form_index'] = row['form_ict_index']
                    captain['name'] = row['name']
                new_row = {'name': row['name'],
                            'now_cost': row['now_cost'],
                            'photo': row['photo'],
                            'team_shirt': row['team_shirt'],
                            'team': row['team']}
                f451['MID'].append(new_row)
                budget -=row['now_cost']
                teams.append(row['team'])
                ict_form += row['form_ict_index']
                MID = MID +1
            if row['position']=='GK' and GK<1 and row['status']=='a' and budget>row['now_cost']:
                if row['form_ict_index'] >= captain['ict_form_index']:
                    captain['ict_form_index'] = row['form_ict_index']
                    captain['name'] = row['name']
                new_row = {'name': row['name'],
                            'now_cost': row['now_cost'],
                            'photo': row['photo'],
                            'team_shirt': row['team_shirt'],
                            'team': row['team']}
                f451['GK'].append(new_row)
                budget -=row['now_cost']
                teams.append(row['team'])
                ict_form += row['form_ict_index']
                GK = GK +1
            if row['position']=='DEF' and DEF<=3 and row['status']=='a' and budget>row['now_cost']:
                if row['form_ict_index'] >= captain['ict_form_index']:
                    captain['ict_form_index'] = row['form_ict_index']
                    captain['name'] = row['name']
                new_row = {'name': row['name'],
                            'now_cost': row['now_cost'],
                            'photo': row['photo'],
                            'team_shirt': row['team_shirt'],
                            'team': row['team']}
                f451['DEF'].append(new_row)
                budget -=row['now_cost']
                teams.append(row['team'])
                ict_form += row['form_ict_index']
                DEF = DEF +1
    f451['ict_form'] =ict_form
    f451['team_value'] =  100-budget
    f451['captain'] = captain
    return f451

def get_433():
    f433 = {'GK':[],
            'DEF':[],
            'MID':[],
            'FOW':[],
            'team_value':[],
            'ict_form':[],
            'captain':None
            }
    budget = 100
    GK = 0
    DEF = 0
    MID = 0
    FOW = 0
    teams = []
    ict_form = 0
    captain =  {'name':None,
            'ict_form_index': 0}
    for index,row in dataset.iterrows():
        if teams.count(row['team']) < 3 and row['postponed']=='No':
            if row['position']=='FOW' and FOW<=2 and row['status']=='a' and budget>row['now_cost']:
                if row['form_ict_index'] >= captain['ict_form_index']:
                    captain['ict_form_index'] = row['form_ict_index']
                    captain['name'] = row['name']
                new_row = {'name': row['name'],
                            'now_cost': row['now_cost'],
                            'photo': row['photo'],
                            'team_shirt': row['team_shirt'],
                            'team': row['team']}
                f433['FOW'].append(new_row)
                budget -=row['now_cost']
                teams.append(row['team'])
                ict_form += row['form_ict_index']
                FOW = FOW +1
            if row['position']=='MID' and MID<=2 and row['status']=='a' and budget>row['now_cost']:
                if row['form_ict_index'] >= captain['ict_form_index']:
                    captain['ict_form_index'] = row['form_ict_index']
                    captain['name'] = row['name']
                new_row = {'name': row['name'],
                            'now_cost': row['now_cost'],
                            'photo': row['photo'],
                            'team_shirt': row['team_shirt'],
                            'team': row['team']}
                f433['MID'].append(new_row)
                budget -=row['now_cost']
                teams.append(row['team'])
                ict_form += row['form_ict_index']
                MID = MID +1
            if row['position']=='GK' and GK<1 and row['status']=='a' and budget>row['now_cost']:
                if row['form_ict_index'] >= captain['ict_form_index']:
                    captain['ict_form_index'] = row['form_ict_index']
                    captain['name'] = row['name']
                new_row = {'name': row['name'],
                            'now_cost': row['now_cost'],
                            'photo': row['photo'],
                            'team_shirt': row['team_shirt'],
                            'team': row['team']}
                f433['GK'].append(new_row)
                budget -=row['now_cost']
                teams.append(row['team'])
                ict_form += row['form_ict_index']
                GK = GK +1
            if row['position']=='DEF' and DEF<=3 and row['status']=='a' and budget>row['now_cost']:
                if row['form_ict_index'] >= captain['ict_form_index']:
                    captain['ict_form_index'] = row['form_ict_index']
                    captain['name'] = row['name']
                new_row = {'name': row['name'],
                            'now_cost': row['now_cost'],
                            'photo': row['photo'],
                            'team_shirt': row['team_shirt'],
                            'team': row['team']}
                f433['DEF'].append(new_row)
                budget -=row['now_cost']
                teams.append(row['team'])
                ict_form += row['form_ict_index']
                DEF = DEF +1
    f433['ict_form'] =ict_form
    f433['team_value'] =  100-budget
    f433['captain'] = captain
    return f433



def get_352():
    f352 = {'GK':[],
            'DEF':[],
            'MID':[],
            'FOW':[],
            'team_value':[],
            'ict_form':[],
            'captain':None
            }
    budget = 100
    GK = 0
    DEF = 0
    MID = 0
    FOW = 0
    teams = []
    ict_form = 0
    captain =  {'name':None,
            'ict_form_index': 0}
    for index,row in dataset.iterrows():
        if teams.count(row['team']) < 3 and row['postponed']=='No':
            if row['position']=='FOW' and FOW<=1 and row['status']=='a' and budget>row['now_cost']:
                if row['form_ict_index'] >= captain['ict_form_index']:
                    captain['ict_form_index'] = row['form_ict_index']
                    captain['name'] = row['name']
                new_row = {'name': row['name'],
                            'now_cost': row['now_cost'],
                            'photo': row['photo'],
                            'team_shirt': row['team_shirt'],
                            'team': row['team']}
                f352['FOW'].append(new_row)
                budget -=row['now_cost']
                teams.append(row['team'])
                ict_form += row['form_ict_index']
                FOW = FOW +1
            if row['position']=='MID' and MID<=4 and row['status']=='a' and budget>row['now_cost']:
                if row['form_ict_index'] >= captain['ict_form_index']:
                    captain['ict_form_index'] = row['form_ict_index']
                    captain['name'] = row['name']
                new_row = {'name': row['name'],
                            'now_cost': row['now_cost'],
                            'photo': row['photo'],
                            'team_shirt': row['team_shirt'],
                            'team': row['team']}
                f352['MID'].append(new_row)
                budget -=row['now_cost']
                teams.append(row['team'])
                ict_form += row['form_ict_index']
                MID = MID +1
            if row['position']=='GK' and GK<1 and row['status']=='a' and budget>row['now_cost']:
                if row['form_ict_index'] >= captain['ict_form_index']:
                    captain['ict_form_index'] = row['form_ict_index']
                    captain['name'] = row['name']
                new_row = {'name': row['name'],
                            'now_cost': row['now_cost'],
                            'photo': row['photo'],
                            'team_shirt': row['team_shirt'],
                            'team': row['team']}
                f352['GK'].append(new_row)
                budget -=row['now_cost']
                teams.append(row['team'])
                ict_form += row['form_ict_index']
                GK = GK +1
            if row['position']=='DEF' and DEF<=2 and row['status']=='a' and budget>row['now_cost']:
                if row['form_ict_index'] >= captain['ict_form_index']:
                    captain['ict_form_index'] = row['form_ict_index']
                    captain['name'] = row['name']
                new_row = {'name': row['name'],
                            'now_cost': row['now_cost'],
                            'photo': row['photo'],
                            'team_shirt': row['team_shirt'],
                            'team': row['team']}
                f352['DEF'].append(new_row)
                budget -=row['now_cost']
                teams.append(row['team'])
                ict_form += row['form_ict_index']
                DEF = DEF +1
    f352['ict_form'] =ict_form
    f352['team_value'] =  100-budget
    f352['captain'] = captain
    return f352


def get_343():
    f343 = {'GK':[],
            'DEF':[],
            'MID':[],
            'FOW':[],
            'team_value':[],
            'ict_form':[],
            'captain':None
            }
    budget = 100
    GK = 0
    DEF = 0
    MID = 0
    FOW = 0
    teams = []
    ict_form = 0
    captain =  {'name':None,
            'ict_form_index': 0}
    for index,row in dataset.iterrows():
        if teams.count(row['team']) < 3 and row['postponed']=='No':
            if row['position']=='FOW' and FOW<=2 and row['status']=='a' and budget>row['now_cost']:
                if row['form_ict_index'] >= captain['ict_form_index']:
                    captain['ict_form_index'] = row['form_ict_index']
                    captain['name'] = row['name']
                new_row = {'name': row['name'],
                            'now_cost': row['now_cost'],
                            'photo': row['photo'],
                            'team_shirt': row['team_shirt'],
                            'team': row['team']}
                f343['FOW'].append(new_row)
                budget -=row['now_cost']
                teams.append(row['team'])
                ict_form += row['form_ict_index']
                FOW = FOW +1
            if row['position']=='MID' and MID<=3 and row['status']=='a' and budget>row['now_cost']:
                if row['form_ict_index'] >= captain['ict_form_index']:
                    captain['ict_form_index'] = row['form_ict_index']
                    captain['name'] = row['name']
                new_row = {'name': row['name'],
                            'now_cost': row['now_cost'],
                            'photo': row['photo'],
                            'team_shirt': row['team_shirt'],
                            'team': row['team']}
                f343['MID'].append(new_row)
                budget -=row['now_cost']
                teams.append(row['team'])
                ict_form += row['form_ict_index']
                MID = MID +1
            if row['position']=='GK' and GK<1 and row['status']=='a' and budget>row['now_cost']:
                if row['form_ict_index'] >= captain['ict_form_index']:
                    captain['ict_form_index'] = row['form_ict_index']
                    captain['name'] = row['name']
                new_row = {'name': row['name'],
                            'now_cost': row['now_cost'],
                            'photo': row['photo'],
                            'team_shirt': row['team_shirt'],
                            'team': row['team']}
                f343['GK'].append(new_row)
                budget -=row['now_cost']
                teams.append(row['team'])
                ict_form += row['form_ict_index']
                GK = GK +1
            if row['position']=='DEF' and DEF<=2 and row['status']=='a' and budget>row['now_cost']:
                if row['form_ict_index'] >= captain['ict_form_index']:
                    captain['ict_form_index'] = row['form_ict_index']
                    captain['name'] = row['name']
                new_row = {'name': row['name'],
                            'now_cost': row['now_cost'],
                            'photo': row['photo'],
                            'team_shirt': row['team_shirt'],
                            'team': row['team']}
                f343['DEF'].append(new_row)
                budget -=row['now_cost']
                teams.append(row['team'])
                ict_form += row['form_ict_index']
                DEF = DEF +1
    f343['ict_form'] =ict_form
    f343['team_value'] =  100-budget
    f343['captain'] = captain
    return f343