import requests
import json
import numpy as np
import pandas as pd
import datetime
from pprint import  pprint

def get_info():
    # Make a get request to get the latest player data from the FPL API
    link = "https://fantasy.premierleague.com/api/bootstrap-static/"
    response = requests.get(link)

    # Convert JSON data to a python object
    data = json.loads(response.text)

    events = data['events']

    events_df = pd.DataFrame(events)


    events_df['deadline_time'] = pd.to_datetime(events_df['deadline_time'])
    events_df['deadline_time'] = events_df['deadline_time'].dt.tz_localize(None)

    events_df.to_csv(index=False, path_or_buf='data2.csv')

    current_gameweek = {'Gameweek': '',
                        'deadline_time': '',
                        'chip_plays': '',
                        'most_selected':'',
                        'most_transferred_in':'',
                        'most_captained':'',
                        'most_vice_captained':'',
    }

    for index,row in events_df.iterrows():
        if str(row['finished']).lower()=='false':
            current_gameweek['Gameweek'] = row['name']
            current_gameweek['deadline_time'] =  str(row['deadline_time']).strip('Timestamp')
            current_gameweek['chip_plays'] = row['chip_plays']
            #current_gameweek['most_selected'] = row['most_selected']
            #current_gameweek['most_transferred_in'] = row['most_transferred_in']
            #current_gameweek['most_captained'] = row['most_captained']
            #current_gameweek['most_vice_captained'] = row['most_vice_captained']
            break
    for x in current_gameweek['chip_plays']:
        if x['chip_name'] =='bboost':
            x['chip_name'] = 'Bench Boost'
        elif x['chip_name']=='freehit':
            x['chip_name'] = 'Free Hit'
        elif x['chip_name']=='wildcard':
            x['chip_name'] = 'Wildcard'
        elif x['chip_name']=='3xc':
            x['chip_name'] = 'Triple Captain'

    return current_gameweek
