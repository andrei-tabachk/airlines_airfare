import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import pandas as pd

from flask import Flask, jsonify, render_template

###data setup
engine = create_engine("C:\Users\andre\OneDrive\Documents\Columbia University - Class Work\Repositories\airlines_airfare\airfare_decrease.sqlite")

