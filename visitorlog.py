from flask import Blueprint,request
from sqlalchemy.sql import text
from db import db
import datetime

visitorlog_blueprint = Blueprint('visitorlog_blueprint',_name_)

#define route to API , API for add-visitors
@visitorlog_blueprint.route('/add-visitors',methods=['POST'])
def addvisitors():
    gender=request.form['gender']
    age_group=request.form['age-group']
    comment=request.form['comments']
    currentDate= datetime.datetime.today().strftime('%Y-%m-%d')

    sql = text('INSERT INTO visitor_log (gender,age_group,comment,date) VALUES ('+gender+','+age_group+',"'+comment+'","'+currentDate+'")')
    db.engine.execute(sql)
    return "Data Logged Successfully"
