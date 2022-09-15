import requests
from bs4 import BeautifulSoup
from pprint import pprint


def test():
    return 'hello'
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
        row_headings['xga'] = all_rows_data[12]
        row_headings['goal_keeper'] = all_rows_data[18]
        all_teams.append(row_headings)

    return all_teams



