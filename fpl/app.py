from flask import Flask, render_template, request, url_for, flash, jsonify, redirect
import fpl
from pprint import pprint
import bible
import team_stats
import gameweek_info as gi
import livescores as ls
import fixture_difficulty as fd
import setpieceinfo as spi
import manager_info as mi
import json
import os




app = Flask(__name__)
app.secret_key = 'fpl'




    


#Home page
@app.route("/", methods=["GET", "POST"])
def home():

    verse = bible.get_verse()

    players_to_watch = fd.players_to_watch()
    differentials = fpl.get_differentials()
    gameweek_info = gi.get_info()
    fixtures = fd.get_fixtures()
    header = fd.get_fixtures_header()
    transfer_in = fpl.get_most_transferred_in()
    transfer_out = fpl.get_most_transferred_out()
    selected = fpl.get_most_selected()

    assistant_manager_chip = fpl.get_managers()
    #pprint(assistant_manager_chip)

    



    return render_template("home.html", verse=verse, differentials=differentials, gameweek_info=gameweek_info, fixtures=fixtures, headers=header,managers_df=assistant_manager_chip, transfer_in=transfer_in, transfer_out=transfer_out, selected=selected, players_to_watch =players_to_watch)
  
#gets a livescore for the current gw
@app.route("/livescore", methods=["GET", "POST"])
def livescore():
    # pprint(ls.get_livescore())
    length_of_games = len(ls.get_livescore()['Game_results'])
    # pprint(ls.get_livescore()['Game_results'])

    return render_template("livescore.html", livescore=ls.get_livescore(), length=length_of_games)



# get the best players with value for money for all formations 

@app.route("/formations", methods=["GET", "POST"])
def formations():
    f442 = fpl.get_442()
    f451 = fpl.get_451()
    f532 = fpl.get_532()
    f433 = fpl.get_433()
    f352 = fpl.get_352()
    f343 = fpl.get_343()

    dream = fpl.get_dream_team()
   

    verse = bible.get_verse()
    formations = []
    row = {

    }
    row['name'] = '442'
    row['value'] = round(f442['team_value'], 2)
    row['ict_form'] = round(f442['ict_form'], 2)
    row['budget'] = round(100 - f442['team_value'], 2)
    formations.append(row)

    row = {

    }
    row['name'] = '451'
    row['value'] = round(f451['team_value'], 2)
    row['ict_form'] = round(f451['ict_form'], 2)
    row['budget'] = round(100-f451['team_value'], 2)
    formations.append(row)

    row = {

    }
    row['name'] = '433'
    row['value'] = round(f433['team_value'], 2)
    row['ict_form'] = round(f433['ict_form'], 2)
    row['budget'] = round(100 - f433['team_value'], 2)
    formations.append(row)

    row = {

    }
    row['name'] = '532'
    row['value'] = round(f532['team_value'], 2)
    row['ict_form'] = round(f532['ict_form'], 2)
    row['budget'] = round(100 - f532['team_value'], 2)
    formations.append(row)

    row = {

    }
    row['name'] = '352'
    row['value'] = round(f352['team_value'], 2)
    row['ict_form'] = round(f352['ict_form'], 2)
    row['budget'] = round(100 - f352['team_value'], 2)
    formations.append(row)

    row = {

    }
    row['name'] = '343'
    row['value'] = round(f343['team_value'], 2)
    row['ict_form'] = round(f343['ict_form'], 2)
    row['budget'] = round(100 - f343['team_value'], 2)
    formations.append(row)

    return render_template('formations.html', f442=f442, formations=formations, f451=f451, f433=f433, f352=f352, f532=f532, f343=f343, dream=dream)

# shows how to use the app
@app.route("/help", methods=["GET", "POST"])
def help():

    return render_template("help.html")



# put in the manager pin and get info about the manager 

@app.route("/manager_info", methods=["GET", "POST"])
def manager_info():
    # pprint()
    result = {}

    if request.method == 'POST':
        pin = request.form['pin']
        result = mi.get_manager_info(pin)

        if result == {}:
            #print('Empty')
            flash('The Pin is incorrect, Please try again!')
            return render_template('manager_info_login.html')
        else:
            return render_template('manager_info.html', m_info=result)

    return render_template("manager_info_login.html", m_info=result)


@app.route("/stats", methods=["GET", "POST"])
def stats():
    # print(stats.get_xga())
    #teams_data = stats.get_xga()
    # pprint(team_stats.get_expected_g())
    # pprint(fd.get_fixtures()[0])

    # pprint(team_stats.get_expected_a())

    #table =  team_stats.get_league_table()

    return render_template("stats.html", xg=team_stats.get_expected_g(), xa=team_stats.get_expected_a(), table=team_stats.get_league_table(), teams_data=team_stats.get_expected_ga())

@app.route("/coming_soon", methods=["GET", "POST"])
def coming_soon():
  
    return render_template("coming_soon.html")

# shows latest player news (injury, price changes)
@app.route("/news", methods=["GET", "POST"])
def news():
    # pprint(fpl.get_news())

    return render_template("news.html", news=fpl.get_news(), current_date_time=fpl.get_current_time())


if __name__ == "__main__":

    # debug = true so we do not need to re run the server anytime we make changes
    app.run(debug=True)
