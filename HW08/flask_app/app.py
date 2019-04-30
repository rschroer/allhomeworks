import sqlite3
from flask import Flask, jsonify
from datetime import datetime as dt
import pandas as pd

#################################################
# Database Setup
#################################################

# Import the DB using sqlite3
conn = sqlite3.connect("../Resources/hawaii.sqlite")



#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tob<br/>"
        f"/api/v1.0/<start> and /api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation/")
def precipitation():
    conn = sqlite3.connect("../Resources/hawaii.sqlite")
    cur = conn.cursor()
    cur.execute("SELECT date, prcp FROM measurement")
    result= cur.fetchall()
    precip_dict= {}
    {precip_dict.setdefault(key, []).append(precip) for key, precip in result}
    return(jsonify(precip_dict))

@app.route("/api/v1.0/stations")
def stations():
    conn = sqlite3.connect("../Resources/hawaii.sqlite")
    cur = conn.cursor()
    cur.execute("SELECT station, name, latitude, longitude, elevation FROM station")
    results=cur.fetchall()
    stations_list=[]
    for result in results:
        stations_list.append(dict(station=result[0],name=result[1],lattitude=result[2],longitude=result[3],elevation=result[4]))
    return(jsonify(stations_list))

@app.route("/api/v1.0/tob/")
def tob():
    conn = sqlite3.connect("../Resources/hawaii.sqlite")
    cur = conn.cursor()

    #Find the highest date in the DB
    cur.execute("SELECT MAX(date) FROM measurement")
    max_date=cur.fetchall()
    #Convert to a string
    date_str=max_date[0][0]
    #Convert to a date format
    date_dt=dt.strptime(date_str,'%Y-%m-%d')
    #Subtract a year to find the date for the query
    new_date=date_dt.replace(date_dt.year-1)
    #convert back to string
    new_str=new_date.strftime('%Y-%m-%d')
    #query for the data
    cur.execute(f"SELECT date, tobs FROM measurement WHERE date > '{new_str}'")
    result= cur.fetchall()
    tobs_dict= {}
    {tobs_dict.setdefault(key, []).append(tobs) for key, tobs in result}
    return(jsonify(tobs_dict))

if __name__ == "__main__":
    app.run(debug=True)
