from flask import Flask, render_template, request, url_for,flash,jsonify
import fpl
from pprint import pprint
import bible
import team_stats
import gameweek_info
import livescores as ls
import fixture_difficulty as fd


app = Flask(__name__)
app.secret_key = 'fpl'




@app.route("/", methods = ["GET", "POST"])
def home():

	

	
	verse = bible.get_verse()

	#print(fpl.get_most_transferred_in())
	

	return render_template("main.html", verse=verse, gameweek_info =gameweek_info.get_info(), fixtures = fd.get_fixtures(), headers = fd.get_fixtures_header(), transfer_in= fpl.get_most_transferred_in(), transfer_out = fpl.get_most_transferred_out())



@app.route("/livescore", methods = ["GET", "POST"])
def livescore():
	#pprint(ls.get_livescore())
	length_of_games = len(ls.get_livescore()['Game_results'])
	#pprint(ls.get_livescore()['Game_results'])

	return render_template("livescore.html", livescore=ls.get_livescore(), length=length_of_games)





@app.route("/formations", methods = ["GET", "POST"])
def formations():
	f442 = fpl.get_442()
	f451 = fpl.get_451()
	f532 = fpl.get_532()
	f433 = fpl.get_433()
	f352 = fpl.get_352()
	f343 = fpl.get_343()
	

	

	
	verse = bible.get_verse()
	formations = []
	row = {
	
	}
	row['name'] = '442'
	row['value'] = round(f442['team_value'],2)
	row['ict_form'] = round(f442['ict_form'],2)
	row['budget'] = round(100- f442['team_value'],2)
	formations.append(row)

	row = {
	
	}
	row['name'] = '451'
	row['value'] = round(f451['team_value'],2)
	row['ict_form'] = round(f451['ict_form'],2)
	row['budget'] = round(100-f451['team_value'],2)
	formations.append(row)

	row = {
	
	}
	row['name'] = '433'
	row['value'] = round(f433['team_value'],2)
	row['ict_form'] = round(f433['ict_form'],2)
	row['budget'] = round(100- f433['team_value'],2)
	formations.append(row)

	row = {
	
	}
	row['name'] = '532'
	row['value'] = round(f532['team_value'],2)
	row['ict_form'] = round(f532['ict_form'],2)
	row['budget'] = round(100- f532['team_value'],2)
	formations.append(row)

	row = {
	
	}
	row['name'] = '352'
	row['value'] = round(f352['team_value'],2)
	row['ict_form'] = round(f352['ict_form'],2)
	row['budget'] = round(100- f352['team_value'],2)
	formations.append(row)



	row = {
	
	}
	row['name'] = '343'
	row['value'] = round(f343['team_value'],2)
	row['ict_form'] = round(f343['ict_form'],2)
	row['budget'] = round(100- f343['team_value'],2)
	formations.append(row)


	return render_template('formations.html',f442=f442,formations= formations, f451=f451, f433=f433, f352=f352, f532=f532, f343=f343)
@app.route("/help", methods = ["GET", "POST"])
def help():


	return render_template("help.html")


@app.route("/stats", methods = ["GET", "POST"])
def stats():
	#print(stats.get_xga())
	#teams_data = stats.get_xga()
	#pprint(team_stats.get_expected_g())
	#pprint(fd.get_fixtures()[0])
	




	return render_template("stats.html" , teams_data = team_stats.get_expected_ga(), xg=  team_stats.get_expected_g() )

@app.route("/news", methods = ["GET", "POST"])
def news():
	#pprint(fpl.get_news())


	return render_template("news.html" , news= fpl.get_news(), current_date_time = fpl.get_current_time())

	
if __name__ == "__main__":

	app.run(debug=True) #debug = true so we do not need to re run the server anytime we make changes