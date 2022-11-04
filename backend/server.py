# Import flask and datetime module for showing date and time
from flask import Flask, render_template, request, redirect
import json
import datetime

x = datetime.datetime.now()

# Initializing flask app
app = Flask(__name__)


# Route for seeing a data
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ProcessUserinfo/<string:userinfo>', methods=['POST'])
def ProcessUserinfo(userinfo):
    userinfo = json.loads(userinfo)
    name=userinfo
    print()
    print(name)
    print()
    return('/')
# def get_time():

# 	# Returning an api for showing in reactjs
# 	return {
# 		'Name':"geek",
# 		"Age":"22",
# 		"Date":x,
# 		"programming":"python"
# 		}

	
# Running app
if __name__ == '__main__':
	app.run(debug=True)