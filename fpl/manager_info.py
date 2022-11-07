import requests
import json
import numpy as np
import pandas as pd
import calendar
import datetime
from pprint import  pprint
import re




def get_manager_info(pin):
    try:
        #GETTING GAME WEEK DEADLINE AND CHIP PLAYS
        # Make a get request to get the latest player data from the FPL API
        link = "https://fantasy.premierleague.com/api/entry/" +pin +"/"
        response = requests.get(link)

        # Convert JSON data to a python object
        data = json.loads(response.text)


        league_list = []
        for x in data['leagues']['classic']:
            league ={
                'name': x['name'],
                'id': x['id'],
                'rank': x['entry_rank'],
                'closed': x['closed']
            }
            league_list.append(league)
        manager_data = {
            'team_name': data['name'],
            'player_name': data['player_first_name'] + ' ' + data['player_last_name'],
            'player_country': data['player_region_name'],
            'favorite_team': data['favourite_team'],
            'current_gw': data['current_event'],
            'gw_points': data['summary_event_points'],
            'gw_rank': data['summary_event_rank'],
            'overall_points': data['summary_overall_points'],
            'overall_rank': data['summary_overall_rank'],
            'leagues': league_list
        }
    except:
        manager_data = {}

    return manager_data
