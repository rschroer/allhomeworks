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

if __name__ == "__main__":
    app.run(debug=True)
