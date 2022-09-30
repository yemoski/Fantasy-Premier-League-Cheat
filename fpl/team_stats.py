import requests
from bs4 import BeautifulSoup
from pprint import pprint
import numpy as np
import pandas as pd


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
            'l': '',
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
        row_headings['xga'] = float(all_rows_data[12])
        row_headings['goal_keeper'] = all_rows_data[18]
        all_teams.append(row_headings)



    all_teams = pd.DataFrame(all_teams)

    all_teams = all_teams.sort_values(by=['xga'], ascending=True)


    return all_teams


def get_expected_g():

    # Grab the html code from the webpage
    url = 'https://www.fotmob.com/leagues/47/stats/season/17664/players/expected_goals'
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    data = soup.find_all('table')[0]
    data = data.find_all('tbody')


    for row in data:
        rows = row.find_all('tr')



    all_players_data = []
    for i in range(0,15):
        all_rows_data = []
        row_heading = {
            'rankings': '',
            'name': '',
            'xg': '',
            'goals': '',
            'p':''
        }
        if i==0:
            for x in rows[i]:
                all_rows_data.append(x.get_text())
            #print(all_rows_data)
            row_heading['rankings'] = 1
            row_heading['name'] = all_rows_data[3].replace('Goals','')
            row_heading['name'] = row_heading['name'].replace(':','')
            row_heading['goals'] = [int(s) for s in row_heading['name'].split() if s.isdigit()][0]
            row_heading['name'] = row_heading['name'].replace(str(row_heading['goals']),'')
            row_heading['xg'] = all_rows_data[4]

            if float(row_heading['goals']) > float(row_heading['xg']):
                row_heading['p'] = 'overperforming'
            else:
                row_heading['p'] = 'underperforming'

        else:
            for x in rows[i]:
                all_rows_data.append(x.get_text())
            row_heading['rankings'] = all_rows_data[0]
            row_heading['name'] = all_rows_data[2].replace('Goals', '')
            row_heading['name'] = row_heading['name'].replace(':', '')
            row_heading['goals'] = [int(s) for s in row_heading['name'].split() if s.isdigit()][0]
            row_heading['name'] = row_heading['name'].replace(str(row_heading['goals']), '')
            row_heading['xg'] = all_rows_data[3]

            if float(row_heading['goals']) > float(row_heading['xg']):
                row_heading['p'] = 'overperforming'
            else:
                row_heading['p'] = 'underperforming'


        all_players_data.append(row_heading)
    return all_players_data











