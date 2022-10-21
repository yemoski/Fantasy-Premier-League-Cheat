import requests
from bs4 import BeautifulSoup
from pprint import pprint
import numpy as np
import pandas as pd
import json


def get_league_table():
    # Grab the html code from the webpage
    url = 'https://fbref.com/en/comps/9/Premier-League-Stats'
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    data = soup.find_all('table')[0]
    


  

    all_rows = []


    for row in data.find_all('tbody'):
        rows = row.find_all('tr')




    all_teams = []


    for i in range(0,20):
        all_rows_data = []
        row_headings = {
            'rk': '',
            'squad': '',
            'mp': '',
            'w': '',
            'd': '',
            'l': '',
            'points': '',
            'xga': '',
            'goal_keeper': ''

        }
        for x in rows[i]:
            all_rows_data.append(x.get_text())
        row_headings['rk'] = all_rows_data[0]
        row_headings['squad'] = all_rows_data[1]
        row_headings['mp'] = all_rows_data[2]
        row_headings['w'] = all_rows_data[3]
        row_headings['d'] = all_rows_data[4]
        row_headings['l'] = all_rows_data[5]
        row_headings['points'] = int(all_rows_data[9])
        row_headings['xga'] = float(all_rows_data[12])
        row_headings['goal_keeper'] = all_rows_data[18]
        all_teams.append(row_headings)



    all_teams = pd.DataFrame(all_teams)

    all_teams = all_teams.sort_values(by=['points'], ascending=False)


    return all_teams

def get_expected_ga():
    # Grab the html code from the webpage
    url = 'https://fbref.com/en/comps/9/Premier-League-Stats'
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    data = soup.find_all('table')[0]
    


  

    all_rows = []


    for row in data.find_all('tbody'):
        rows = row.find_all('tr')




    all_teams = []


    for i in range(0,20):
        all_rows_data = []
        row_headings = {
            'rk': '',
            'squad': '',
            'mp': '',
            'w': '',
            'd': '',
            'ga': '',
            'l': '',
            'p':'',
            'points': '',
            'xga': '',
            'goal_keeper': ''

        }
        for x in rows[i]:
            all_rows_data.append(x.get_text())
        row_headings['rk'] = all_rows_data[0]
        row_headings['ga'] = int(all_rows_data[7])
        row_headings['squad'] = all_rows_data[1]
        row_headings['mp'] = all_rows_data[2]
        row_headings['w'] = all_rows_data[3]
        row_headings['d'] = all_rows_data[4]
        row_headings['l'] = all_rows_data[5]
        row_headings['points'] = all_rows_data[9]
        row_headings['xga'] = float(all_rows_data[12])
        row_headings['goal_keeper'] = all_rows_data[18]

        if float(row_headings['ga']) > float(row_headings['xga']):
                row_headings['p'] = 'underperforming'
        else:
            row_headings['p'] = 'overperforming'

        all_teams.append(row_headings)



    all_teams = pd.DataFrame(all_teams)
    #pprint(all_teams)

    all_teams = all_teams.sort_values(by=['xga'], ascending=True)


    return all_teams


def get_expected_g():

    base_url = 'https://understat.com/league'
    leagues = ['La_liga', 'EPL', 'Bundesliga', 'Serie_A', 'Ligue_1', 'RFPL']

    url = base_url + '/' + leagues[1] + '/2022'
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "lxml")

    # Based on the structure of the webpage, I found that data is in the JSON variable, under 'script' tags
    scripts = soup.find_all('script')

    string_with_json_obj = ''

    # Find data for players
    for el in scripts:
        if 'playersData' in str(el):
            string_with_json_obj = str(el).strip()

    # print(string_with_json_obj)
    # strip unnecessary symbols and get only JSON data
    ind_start = string_with_json_obj.index("('") + 2
    ind_end = string_with_json_obj.index("')")
    json_data = string_with_json_obj[ind_start:ind_end]
    json_data = json_data.encode('utf8').decode('unicode_escape')
    data = {}
    data = json.loads(json_data)

    df = pd.DataFrame(data)
    new_df = []
    count = 0
    df['xG'] = df['xG'].astype(float)
    df = df.sort_values(by=['xG'], ascending=False)
    for index, row in df.iterrows():
        if count ==15:
            break
        new_row = {
            'name': row['player_name'],
            'p': '',
            'goals': row['goals'],
            'xg': round(float(row['xG']), 1)
        }

        if float(row['goals']) > float(row['xG']):
            new_row['p'] = 'overperforming'
        else:
            new_row['p'] = 'underperforming'
        new_df.append(new_row)
        count = count + 1

    xg = pd.DataFrame(new_df)
    xg = xg.sort_values(by=['xg'], ascending=False)
    

    return xg




def get_expected_a():
    base_url = 'https://understat.com/league'
    leagues = ['La_liga', 'EPL', 'Bundesliga', 'Serie_A', 'Ligue_1', 'RFPL']
    

    url = base_url+'/'+leagues[1]+'/2022'
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "lxml")

    # Based on the structure of the webpage, I found that data is in the JSON variable, under 'script' tags
    scripts = soup.find_all('script')

    string_with_json_obj = ''

    # Find data for players
    for el in scripts:
        if 'playersData' in str(el):
            string_with_json_obj = str(el).strip()

    # print(string_with_json_obj)
    # strip unnecessary symbols and get only JSON data
    ind_start = string_with_json_obj.index("('") + 2
    ind_end = string_with_json_obj.index("')")
    json_data = string_with_json_obj[ind_start:ind_end]
    json_data = json_data.encode('utf8').decode('unicode_escape')
    data = {}
    data = json.loads(json_data)
    
    
    
    df = pd.DataFrame(data)
    new_df = []
    counter = 0
    df = df.sort_values(by=['xA'], ascending=False)
    for index,row in df.iterrows():
        new_row = {
        'name' : row['player_name'],
        'p': '',
        'assist': row['assists'],
        'xa' :round(float(row['xA']),1)
        }




        if float(row['assists']) > float(row['xA']):
                new_row['p'] = 'overperforming'
        else:
            new_row['p'] = 'underperforming'
        new_df.append(new_row)
        counter = counter + 1

    xa = pd.DataFrame(new_df)
    xa = xa.sort_values(by=['xa'], ascending=False)
    xa = xa.iloc[0:15]



    return xa
    



    """xa = df[['player_name','assists','xA']]
    xa['xA']=xa['xA'].astype(float)
    xa = xa.sort_values(by=['xA'], ascending=False)
    xa = xa.loc[0:15]
    pprint(xa)
    """
    


