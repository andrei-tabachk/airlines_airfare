import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import pandas as pd

from flask import Flask, jsonify, render_template

###data setup
engine = create_engine("sqlite://airfare_decrease.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# save reference to table
Base.classes.routes

Routes = Base.classes.routes

app = Flask(__name__)

@app.route("/")
def main():
    """List all available api routes."""
    return ('index.html')

@app.route("/")
def airfare():