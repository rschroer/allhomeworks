import sqlite3
from flask import Flask, jsonify
from datetime import datetime as dt
import pandas as pd

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
        "<h1>API Home and Instructions</h1>"
        "<h2>Precipitation by Days</h2>"
        "<b1>/api/v1.0/precipitation</b1>"
        "<h2>List of Station</h2>"
        "<b1>/api/v1.0/stations</b1>"
        "<h2>Observable Temperature by Day</h2>"
        "<b1>/api/v1.0/tob<b1>"
        "<h2>Temperature Statistics for Date Range</h2>"
        "<b1>/api/v1.0/&#x3C;start&#x3E; and /api/v1.0/&#x3C;start&#x3E;/&#x3C;end&#x3E;<b1>"
    )

@app.route("/api/v1.0/precipitation/")
def precipitation():
    # connect to the db
    conn = sqlite3.connect("../Resources/hawaii.sqlite")
    cur = conn.cursor()
    # select date and precipitation from the db
    cur.execute("SELECT date, prcp FROM measurement")
    result= cur.fetchall()
    # create and add results into the dictionary
    precip_dict= {}
    {precip_dict.setdefault(key, []).append(precip) for key, precip in result}
    return jsonify(precip_dict)

@app.route("/api/v1.0/stations")
def stations():
    # connect to the db
    conn = sqlite3.connect("../Resources/hawaii.sqlite")
    cur = conn.cursor()
    #select the station data
    cur.execute("SELECT station, name, latitude, longitude, elevation FROM station")
    results=cur.fetchall()
    stations_list=[]
    # add the results to a list of dictionaries
    for result in results:
        stations_list.append(dict(station=result[0],name=result[1],lattitude=result[2],longitude=result[3],elevation=result[4]))
    return jsonify(stations_list)

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

@app.route("/api/v1.0/<start>")
def temp_past(start):
    try:
        ##This date conversion verifies that the url is properly formatted
        min_date=dt.strptime(start,'%Y-%m-%d')
        ## Connect to db
        conn = sqlite3.connect("../Resources/hawaii.sqlite")
        cur = conn.cursor()

        ## find min and max date on db
        cur.execute("SELECT MIN(date),MAX(date) FROM measurement")
        db_result=cur.fetchall()
        #Convert to a string
        min_str=db_result[0][0]
        max_str=db_result[0][1]

        # Check to see if the date ranges are out of bounds
        if start < min_str:
            results={"error": f"{start} is less than the earliest database date of {min_str}"}
        elif start > max_str:
            results={"error": f"{start} is greater than the latest database date of {max_str}"}
        else:
            #select the aggretate temperatures of the dates greater than start date
            cur.execute(f"SELECT MIN(tobs),MAX(tobs),AVG(tobs) FROM measurement WHERE date >= {start}")
            temp_results=cur.fetchall()
            #format the results for the average of those dates
            results={"start":start,
                     "end":max_str,
                     "TMIN":temp_results[0][0],
                     "TMAX":temp_results[0][1],
                     "TAVG":"{0:.1f}".format(temp_results[0][2])}
        return jsonify(results),200
    except: 
        #return an error if there's a date typo
        results={"error": f"{start} is not date format of YYYY-MM-DD or an API path"}
        return jsonify(results),404
    
@app.route("/api/v1.0/<start>/<end>")
def temp_range(start,end):
    try:
        min_date=dt.strptime(start,'%Y-%m-%d')
        max_date=dt.strptime(end,'%Y-%m-%d')

        ## Connect to db
        conn = sqlite3.connect("../Resources/hawaii.sqlite")
        cur = conn.cursor()

        ## find min and max date on db
        cur.execute("SELECT MIN(date),MAX(date) FROM measurement")
        db_result=cur.fetchall()
        #Convert to a string
        min_str=db_result[0][0]
        max_str=db_result[0][1]

        # For date error handling, I have 3 categories, if the start is earlier than the 
        # first db date, if the end is greater than the last db date, and if the start is 
        # greater than the end.
        if start > end:
            results={"error":f"Start date {start} is greater than end date {end}."}
        elif start < min_str:
            results={"error": f"{start} is less than the earliest database date of {min_str}"}
        elif end > max_str:
            results={"error": f"{end} is greater than the latest database date of {max_str}"}
                
        else:
            # find min max and rage of temp for those dates
            cur.execute(f"SELECT MIN(tobs),MAX(tobs),AVG(tobs) FROM measurement WHERE date >= '{start}' AND date <= '{end}' AND tobs IS NOT NULL")
            temp_results=cur.fetchall()
            # return the results
            results={"start":start,
                     "end":end,
                     "TMIN":temp_results[0][0],
                     "TMAX":temp_results[0][1],
                     "TAVG":"{0:.1f}".format(temp_results[0][2])
                    }
        return jsonify(results),200
    except: 
        #return an error if there's a date typo
        results={"error": f"{start} is not date format of YYYY-MM-DD or an API path"}
        return jsonify(results),404

if __name__ == "__main__":
    app.run(debug=True)
