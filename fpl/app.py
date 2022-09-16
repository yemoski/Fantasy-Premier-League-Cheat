from flask import Flask, render_template, request, url_for,flash,jsonify
import fpl
from pprint import pprint
import bible
import team_stats
import gameweek_info

app = Flask(__name__)
app.secret_key = 'fpl'




@app.route("/", methods = ["GET", "POST"])
def home():
	f442 = fpl.get_442()
	f451 = fpl.get_451()
	f532 = fpl.get_532()
	f433 = fpl.get_433()
	f352 = fpl.get_352()
	f343 = fpl.get_343()
	#pprint(f433)
	#pprint(f352)
	#pprint(f442)
	#pprint(gameweek_info.get_info())

	

	
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



	#print(formations)

	
	


	return render_template("main.html",f442=f442, verse=verse,formations= formations, f451=f451, f433=f433, f352=f352, f532=f532, f343=f343, gameweek_info =gameweek_info.get_info() )


@app.route("/help", methods = ["GET", "POST"])
def help():


	return render_template("help.html")


@app.route("/stats", methods = ["GET", "POST"])
def stats():
	#print(stats.get_xga())
	#teams_data = stats.get_xga()
	#print(team_stats.get_expected_ga())


	return render_template("stats.html" , teams_data = team_stats.get_expected_ga() )


	
if __name__ == "__main__":

	app.run(debug=True) #debug = true so we do not need to re run the server anytime we make changes