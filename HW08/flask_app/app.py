import sqlite3
from flask import Flask, jsonify
from datetime import datetime as dt

#################################################
# Database Setup
#################################################

# Import the DB using sqlite3
conn = sqlite3.connect("./Resources/hawaii.sqlite")
cur = conn.cursor()


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
        f"/api/v1.0/precipitation\n"
        f"/api/v1.0/stations\n"
        f"/api/v1.0/tob\n"
        f"/api/v1.0/<start> and /api/v1.0/<start>/<end>"
    )


