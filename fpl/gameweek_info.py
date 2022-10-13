import requests
import json
import numpy as np
import pandas as pd
import datetime
from datetime import datetime
from pprint import  pprint
import livescores as ls

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
    events_df = events_df.replace({np.nan: None})


    


    '''
    month_name = str(time.strftime('%B'))
    year = str(time.strftime('%Y'))
    day = str(time.strftime('%d'))
    time2 = time.strftime('%H:%M:%S')
    day_name = pd.Timestamp(time)
    day_name = day_name.day_name() 
    full_date = day_name + ', '+day+ ' '+ month_name + ' ' + year

    print(full_date)
    '''
    #events_df.to_csv(index=False, path_or_buf='data2.csv')

    current_gameweek = {'Gameweek': '',
                        'deadline_time': '',
                        'chip_plays': '',
                        'most_captained':'',
                        'most_vice_captained':'',
                        'top_element': ''
    }

    for index,row in events_df.iterrows():
        if str(row['finished']).lower()=='false':
            current_gameweek['Gameweek'] = row['name']
            
            current_gameweek['deadline_time'] =  str(row['deadline_time']).strip('Timestamp')
            day = pd.Timestamp(current_gameweek['deadline_time'])
            hour = str(day.hour+1)
            minutes = str(day.minute)
            full_date = str(pd.to_datetime(current_gameweek['deadline_time']).date())
            #print(full_date)
            #print(hour + ':'+minutes)
            #print(current_gameweek['deadline_time'])
            current_gameweek['deadline_time'] = day.day_name() + ' ' + full_date + ' '+hour+':'+minutes
            current_gameweek['chip_plays'] = row['chip_plays']

            if row['most_captained']!=None:
                current_gameweek['most_captained'] = ls.get_player_name(int(row['most_captained']))
                current_gameweek['most_vice_captained'] = ls.get_player_name(int(row['most_vice_captained']))
                current_gameweek['top_element'] = ls.get_player_name(int(row['top_element_info']['id'])) +' with ' + str(row['top_element_info']['points']) + ' points'
            break
    for x in current_gameweek['chip_plays']:
        x['num_played'] = '{:,}'.format(int(x['num_played']))
        if x['chip_name'] =='bboost':     
            x['chip_name'] = 'Bench Boost'
        elif x['chip_name']=='freehit':
            x['chip_name'] = 'Free Hit'
        elif x['chip_name']=='wildcard':
            x['chip_name'] = 'Wildcard'
        elif x['chip_name']=='3xc':
            x['chip_name'] = 'Triple Captain'

    return current_gameweek
