from flask import Flask, render_template, request, url_for,flash,jsonify
import fpl
from pprint import pprint
from freebible import bibles

app = Flask(__name__)
app.secret_key = 'fpl'


print()

@app.route("/", methods = ["GET", "POST"])
def home():
	f442 = fpl.get_442()
	pprint(f442)


	return render_template("index.html",f442=f442)



	
if __name__ == "__main__":

	app.run(debug=True) #debug = true so we do not need to re run the server anytime we make changes