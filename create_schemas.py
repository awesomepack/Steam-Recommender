'''
create_schemas.py does the following:
* Creates a database named steam_recommender if it does not exist within a local instance of PostgreSQL
* Creates schemas for our set of csv data in steam_recommender

requirements:
* in lines 24 and 27 you need to specify the file paths to the csv source files
* import your Postgres credentials for connection to Postgres

 '''

# Importing dependencies
import psycopg2
import sqlalchemy #version 1.4.7
import pandas as pd
import os
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists , create_database
from sqlalchemy import Table , Column , Integer , String , MetaData , Float , JSON
from credentials import password , user_name

# Connect to PostgreSQL using Pscopg2
postgresEngine = create_engine(f'postgresql+psycopg2://{user_name}:{password}@localhost/Steam_Recommender' , echo = True)

# if the database steam_recommender does not exist , create it
if not database_exists(postgresEngine.url):
    create_database(postgresEngine.url)

def make_table(file, key):
    tablename = file.split(os.path.sep)[-1][:-4]
    pd.read_csv(file).to_sql(tablename, postgresEngine, if_exists = 'replace', index = False)
    with postgresEngine.connect() as con:
        con.execute(f'ALTER TABLE "{tablename}" ADD PRIMARY KEY ("{key}");')

datafolder = 'data'

for filename in os.listdir(datafolder):
    print(f'Making: {filename} table')
    if filename.endswith('.csv'):
        if filename.startswith("metacritic"):
            # make_table(os.path.join(datafolder, filename), 'name')
            continue
        else:
            make_table(os.path.join(datafolder, filename), 'appid')
    else:
        continue