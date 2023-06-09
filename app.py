import numpy as np
import pandas as pd
from pathlib import Path

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import Column, String, Float, Integer
import pandas as pd

from flask import Flask, jsonify, render_template

###data setup


# reflect an existing database into a new model
#Base = automap_base()
Base = declarative_base()
database_path = Path("airfare_decrease.sqlite")
engine = create_engine(f"sqlite://{database_path}")
# reflect the tables
Base.metadata.create_all(engine)

# save reference to table
Base.classes.routes

Routes = Base.classes.routes

# Create your  class
class Airfare(Base):
    __tablename__ = 'airfare_decrease_table'
    id = Column(Integer, primary_key=True)
    Year = Column(Integer)
    quarter = Column(Integer)
    city1 = Column(String)
    city2 = Column(String)
    cur_passenger = Column(Float)
    cur_fare = Column(Float)
    ly_fare = Column(Float)
    ly_passenger = Column(Float)
    amount_change = Column(Float)
    percent_change = Column(Float)
    amount_change_pax = Column(Float)
    percent_change_pax = Column(Float)
    Latitude1 = Column(Float)
    Longitude1 = Column(Float)
    Latitude2 = Column(Float)
    Longitude2 = Column(Float)

#session
session = Session(bind=engine)

### flask set up
app = Flask(__name__)


### flask routes
@app.route("/")
def main():
    """List all available api routes."""
    return ('index.html')


@app.route("/api.v1.0/airfare")
def routes():

if __name__ == '__main__':
    app.run(debug=True)
