from flask import Flask   # import flask,Flask Framework
from flask_cors import CORS
from db import db
from visitorlog import visitorlog_blueprint
from dashboard import dashboard_blueprint


#call instance of flask
app = Flask(_name_)
CORS(app)

#Database configuration
username = 'root'
password = ''
userpass = 'mysql+pymysql://' + username + ':' + password + '@'
server = '127.0.0.1'  #SERVER IP ADDRESS WHERE SQL RUNS
dbname = '/walmart_visitor_counter'

#UNIVERSAL RESOURCE INDICATOR
app.config['SQLALCHEMY_DATABASE_URI'] = userpass + server + dbname
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db.init_app(app) # to connect db. where you pass all config option to do instance

#Register the blueprint
app.register_blueprint(visitorlog_blueprint)
app.register_blueprint(dashboard_blueprint)


@app.route('/')
def hello_world():
    return 'Hello World'

if _name_ == '_main_':
    app.debug=True
    app.run()
