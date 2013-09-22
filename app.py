import os
from flask import Flask, render_template, send_from_directory, Response, url_for, request
import json

#----------------------------------------
# initialization
#----------------------------------------

app = Flask(__name__)

app.config.update(
	DEBUG = False,
)

app.config["SECRET_KEY"] = 'fba1bd7e21e898d924584a6e4f04cc65275ab5516c589b40'

### marker for flask app generator - keep this line

#----------------------------------------
# controllers
#----------------------------------------

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/apply")
def apply():
	return render_template('apply.html')

#----------------------------------------
# handlers
#----------------------------------------

@app.route('/favicon.ico')
def favicon():
	return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

#----------------------------------------
# launch
#----------------------------------------

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)