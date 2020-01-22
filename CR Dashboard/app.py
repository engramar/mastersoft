from flask import Flask, render_template, g, request, session, redirect, url_for
import sqlite3
from os import path

app = Flask(__name__) 

#Database helper
ROOT = path.dirname(path.realpath(__file__))
def connect_db():
    sql = sqlite3.connect(path.join(ROOT, "ISSUES.sqlite"))
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.route('/') 
def index(): 
    db = get_db()
    details_cur = db.execute('select ID, ISSUE_ID, PARENT_ID, ETA, BUS_IMPACT, DEV_EFFORT, SUMMARY, CONFLUENCE, STATUS, ASSIGNEE, CREATED, TIME_TO_ETA from ISSUES ORDER BY ID')                              
    details = details_cur.fetchall()
    return_values = []
    for detail in details:
        detail_dict = {}
        detail_dict['ISSUE_ID'] = detail['ISSUE_ID']
        detail_dict['PARENT_ID'] = detail['PARENT_ID']
        #detail_dict['BUS_IMPACT'] = detail['BUS_IMPACT']
        #detail_dict['DEV_EFFORT'] = detail['DEV_EFFORT']
        detail_dict['SUMMARY'] = detail['SUMMARY']
        detail_dict['CONFLUENCE'] = detail['CONFLUENCE']
        detail_dict['STATUS'] = detail['STATUS']
        detail_dict['ASSIGNEE'] = detail['ASSIGNEE']
        detail_dict['CREATED'] = detail['CREATED']
        detail_dict['ETA'] = detail['ETA']        
        detail_dict['TIME_TO_ETA'] = detail['TIME_TO_ETA']
        return_values.append(detail_dict)  
    return render_template('index.html', return_values=return_values)
 
if __name__ == '__main__': 
    app.run(debug=True) 