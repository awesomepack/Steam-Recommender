'''
The helper.py script contains helper functions that make Loading data from our Postgres instance easier
'''

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from credentials import password , user_name
import pandas as pd
from sqlalchemy import join
from sqlalchemy.sql import select


def model_data(UserName , PassWord ):

   

    # Connect to the Steam_Recommender Database using UserName and PassWord
    postgresEngine = create_engine(f'postgresql+psycopg2://{UserName}:{PassWord}@localhost:5432/Steam_Recommender')

    # Establish auotmap base
    Base = automap_base(bind = postgresEngine)

    # Reflect tables in the steam recommender database
    Base.prepare( postgresEngine , reflect = True)

    # Pass the target tables to variables
    SteamData = Base.classes.Steam_Data
    SteamSpy = Base.classes.Steamspy_Data

    # Open session with postgresEngine
    session = Session(postgresEngine)

    # join SteamData and SteamSpy using SQL Alchemy
    query = session.query(SteamData , SteamSpy).join(SteamSpy, SteamData.steam_appid == SteamSpy.appid)
    
    # Transform query results into DF
    df = pd.read_sql(query.statement , session.bind)

    return df