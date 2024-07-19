import requests
import json
import numpy as np
import pandas as pd
import calendar
import datetime
from pprint import  pprint
import re

def get_notes():
    link = " https://fantasy.premierleague.com/api/team/set-piece-notes/"
    response = requests.get(link)
    all_distict_teams = ['Arsenal','Aston Villa','Bournemouth','Brentford','Brighton','Chelsea','Crystal Palace','Everton','Fulham','Leicester','Leeds','Liverpool','Man city','Man United','Newcastle','Nottingham Forest','Southampton','Tottenham','Westham','Wolves']


    # Convert JSON data to a python object
    data = json.loads(response.text)
    #pprint(data)
    all_info = []
    for x in data['teams']:
        notes = []

        team_shirt = all_distict_teams[int(x['id'])-1]
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


        if not x['notes']:
            x['notes'].append({'info_message': 'Sorry, No information for this team at the moment.'})
        for y in x['notes']:
            notes.append(y['info_message'])
        #info['notes'] = notes

        info = {
            'team_name': all_distict_teams[int(x['id'])-1],
            'notes' : notes,
            'team_logo': team_shirt
        }

        all_info.append(info)

    return all_info